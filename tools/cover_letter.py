from langchain.tools import tool
from services.llm_service import ask_llm


@tool
def cover_letter(resume: str, job_description: str) -> str:
    """
    Generate a professional cover letter.
    """

    prompt = f"""
You are an expert HR recruiter.

Using the following resume and job description,
write a professional one-page cover letter.

Resume:
{resume}

Job Description:
{job_description}

Requirements:
- Professional tone
- Mention matching skills
- Explain why the candidate fits the role
- Keep it concise
"""

    return ask_llm(prompt)