from langchain.tools import tool
from tools.resume_parser import parse_resume


@tool
def ats_checker(resume: str) -> str:
    """
    ATS compatibility checker.
    """

    data = parse_resume(resume)

    skill_score = min(len(data["skills"]) * 3, 40)

    section_score = sum(data["sections"].values()) * 10

    contact_score = 20 if data["email"] and data["phone"] else 10

    quantified_score = 10 if data["quantified"] else 0

    github_score = 10 if data["github"] else 0

    linkedin_score = 10 if data["linkedin"] else 0

    total = min(
        skill_score
        + section_score
        + contact_score
        + quantified_score
        + github_score
        + linkedin_score,
        100
    )

    missing_sections = [
        name.capitalize()
        for name, present in data["sections"].items()
        if not present
    ]

    return f"""
# 🎯 ATS Report

## ATS Score

**{total}/100**

---

## Skills Found

{", ".join(data["skills"]) if data["skills"] else "None"}

---

## Missing Sections

{", ".join(missing_sections) if missing_sections else "None"}

---

## Contact Information

Email : {"✅" if data["email"] else "❌"}

Phone : {"✅" if data["phone"] else "❌"}

GitHub : {"✅" if data["github"] else "❌"}

LinkedIn : {"✅" if data["linkedin"] else "❌"}

---

## Suggestions

• Add more relevant technical skills.

• Include measurable achievements.

• Add GitHub and LinkedIn profiles.

• Customize your resume for every job.
"""