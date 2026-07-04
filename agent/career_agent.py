from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_groq import ChatGroq

from tools.resume_feedback import resume_feedback
from tools.ats_checker import ats_checker

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

agent = create_agent(
    model=model,
    tools=[
        resume_feedback,
        ats_checker
    ],
    system_prompt="""
You are an expert AI Career Assistant.

You help users with:

- Resume Review
- ATS Analysis
- Career Guidance

Whenever a tool can answer the question,
use the tool instead of answering yourself.

Always provide structured and professional responses.
"""
)