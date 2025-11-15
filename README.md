


# SMART-ASSIGNMENT-AGENT

**Real-time Assignment Checker & Improver using Google Gemini API**

---

## 📝 Project Overview

**Smart-Assignment-Agent** is a Python-based project designed to **analyze, check, and improve student assignments** automatically. It uses **Google Gemini API** as the LLM backend to:

- Detect spelling, grammar, and punctuation errors.
- Suggest improvements in clarity, context, and structure.
- Provide example revisions with enhanced context.
- Detect plagiarism and provide feedback.

This system is modular and organized for **easy extension** with additional agents or tools.

---

---

## ⚡ Features

- **Input Agent:** Cleans and splits assignment text.
- **Assignment Checker Agent:** Identifies errors and improvement areas.
- **Improver Agent:** Generates improved version of text using LLM.
- **Feedback Agent:** Provides suggestions for better content and context.
- **Orchestrator:** Integrates all agents and manages workflow.
- **LLM Client:** Interfaces with **Google Gemini API** using API key.

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd smart-assignment-agent
````

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Set your **Google Gemini API key** in `.env`:

```env
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

---

## 🚀 Usage

1. Test the **LLM Client**:

```bash
python src/llm/test_llm_real.py
```

2. Run **assignment checking**:

```bash
python -m src.agents.test_assignment_checker
```

3. Integrate all agents using the **orchestrator**:

```bash
python src/orchestrator.py
```

---

## 💡 Notes

* Make sure your Google Gemini API key has **access and quota enabled**.
* Each agent is modular; you can add new agents under `src/agents`.
* The orchestrator handles the **end-to-end workflow**.

---

## 📜 License

MIT License – Free for educational and personal use.

---

## 🔗 References

* [Google Generative AI (Gemini) Documentation](https://developers.generativeai.google/)
* [Python Requests Library](https://docs.python-requests.org/en/latest/)
* [Pydantic Documentation](https://docs.pydantic.dev/)


