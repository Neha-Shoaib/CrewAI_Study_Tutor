# 🎓 AI Study Tutor Agent

An interactive, AI-powered study assistant built with **CrewAI**, **Groq** (`llama-3.3-70b-versatile`), and **Streamlit**. The tutor breaks complex concepts down step-by-step, performs exact arithmetic using custom agent tools, and tests student comprehension with interactive check-in questions.

---

## 🚀 Features

- **Step-by-Step Pedagogy**: Explains complex topics with intuitive real-world analogies and clear, incremental breakdowns.
- **Accurate Math Tool**: Equipped with a custom `CalculatorTool` so the agent evaluates mathematical expressions safely without LLM hallucination.
- **Short-Term Memory**: Streamlit session state preserves recent conversational context across questions.
- **Ultra-Fast Inference**: Uses Groq-hosted open-weights models for near-instant responses.
- **No Local Setup Required**: Designed to be created entirely on GitHub's web editor and deployed directly to Render.

---

## 📁 Project Structure

```plaintext
study-tutor/
├── app.py             # Streamlit chat interface and session memory
├── tutor_crew.py      # CrewAI Agent, Task, and LLM configuration
├── tools.py
