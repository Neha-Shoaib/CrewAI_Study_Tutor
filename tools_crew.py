import os
from crewai import Agent, Task, Crew, Process, LLM
from tools import calculate_expression

def get_groq_llm(api_key: str):
    """Initializes the Groq LLM for CrewAI."""
    return LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=api_key,
        temperature=0.5
    )

def run_study_tutor(user_query: str, history_context: str, api_key: str) -> str:
    """Runs a single-agent Study Tutor crew with memory context and tools."""
    llm = get_groq_llm(api_key)

    # Agent with dedicated persona and calculator tool
    tutor_agent = Agent(
        role="Adaptive Study Tutor",
        goal="Teach concepts with clarity, use analogies, and verify facts or math with tools.",
        backstory=(
            "You are a supportive, insightful academic study tutor. "
            "You explain complex topics step-by-step, use simple analogies, "
            "and end your explanations with 1 or 2 quick check-in questions to test understanding."
        ),
        tools=[calculate_expression],
        verbose=False,
        llm=llm,
        allow_delegation=False
    )

    # Task taking conversational history and current prompt
    study_task = Task(
        description=(
            "Review the session context and answer the student's latest question.\n\n"
            "Session Context:\n{context}\n\n"
            "Student's Current Question:\n{query}\n\n"
            "Instructions:\n"
            "1. If math or numerical logic is involved, use the CalculatorTool.\n"
            "2. Break down hard concepts into manageable steps.\n"
            "3. Ask 1-2 interactive check questions at the end."
        ),
        expected_output="A structured, easy-to-read explanation followed by quick practice questions.",
        agent=tutor_agent
    )

    # Crew execution
    crew = Crew(
        agents=[tutor_agent],
        tasks=[study_task],
        process=Process.sequential
    )

    result = crew.kickoff(inputs={
        "context": history_context if history_context else "No prior history.",
        "query": user_query
    })
    
    return str(result)
