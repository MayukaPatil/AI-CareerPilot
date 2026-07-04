from langchain.tools import tool
from tools.resume_parser import parse_resume


@tool
def resume_feedback(resume: str) -> str:
    """
    Analyze a resume and provide structured feedback.
    """

    data = parse_resume(resume)

    missing_sections = [
        section.capitalize()
        for section, present in data["sections"].items()
        if not present
    ]

    score = 100

    score -= len(missing_sections) * 8

    if not data["email"]:
        score -= 10

    if not data["phone"]:
        score -= 10

    if not data["github"]:
        score -= 5

    if not data["linkedin"]:
        score -= 5

    if not data["quantified"]:
        score -= 10

    score = max(score, 0)

    return f"""
# 📄 Resume Review Report

## Overall Score

**{score}/100**

---

## Contact Information

✅ Email: {"Yes" if data["email"] else "No"}

✅ Phone: {"Yes" if data["phone"] else "No"}

✅ LinkedIn: {"Yes" if data["linkedin"] else "No"}

✅ GitHub: {"Yes" if data["github"] else "No"}

---

## Skills Detected

{", ".join(data["skills"]) if data["skills"] else "No technical skills detected"}

---

## Missing Sections

{", ".join(missing_sections) if missing_sections else "None"}

---

## Recommendations

• Add measurable achievements.

• Improve project descriptions.

• Tailor resume for each job.

• Keep formatting clean.

• Highlight important technical skills.
"""