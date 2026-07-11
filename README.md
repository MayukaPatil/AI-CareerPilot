# 🚀 CareerPilot AI

An AI-powered career assistant that helps job seekers improve resumes,
analyze ATS compatibility, prepare for interviews, generate cover letters,
and receive personalized career guidance using Large Language Models.

--------------------------------------------------

✨ Features

📄 Resume Review

⭐ ATS Score

🎯 Job Match Analysis

🎤 Interview Question Generator

💼 AI Cover Letter Generator

🤖 Career Assistant Chat

--------------------------------------------------

🛠 Tech Stack

Python

Streamlit

LangChain

LangGraph

Groq (Llama 3.3 70B)

PyMuPDF

dotenv

--------------------------------------------------

📂 Project Structure

app.py

services/

tools/

styles.py

.streamlit/

--------------------------------------------------

Future Improvements


- Multi-agent workflow

- Resume semantic search using RAG

- User authentication

- Cloud deployment

- Database support
--------------------------------------------------



 Architecture
 ---------------------------------------------------

```text
User
   │
   ▼
Streamlit Interface
   │
   ▼
LangGraph Workflow
   │
   ├── Resume Feedback
   ├── ATS Checker
   ├── Interview Generator
   ├── Cover Letter Generator
   └── Job Matcher
   │
   ▼
Groq Llama 3.3 70B
```


## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/MayukaPatil/AI-CareerPilot.git
```

Move into the project

```bash
cd AI-CareerPilot
```

Install dependencies

```bash
uv sync
```

Run the application

```bash
streamlit run app.py
```


## 📄 License

This project is intended for educational and portfolio purposes.



Developed by
Mayuka Patil
