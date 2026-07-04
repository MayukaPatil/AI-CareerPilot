from langchain.tools import tool
from tools.resume_parser import parse_resume


ROLE_SKILLS = {
    "data analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "statistics",
        "pandas"
    ],

    "data scientist": [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pandas",
        "numpy",
        "scikit-learn"
    ],

    "ai engineer": [
        "python",
        "langchain",
        "langgraph",
        "machine learning",
        "docker",
        "aws",
        "git"
    ]
}


@tool
def skill_gap(resume: str, role: str) -> str:
    """
    Compare resume skills with a target role.
    """

    data = parse_resume(resume)

    current_skills = set(data["skills"])

    role = role.lower()

    if role not in ROLE_SKILLS:
        return f"Role '{role}' is not supported."

    required_skills = set(ROLE_SKILLS[role])

    missing = sorted(required_skills - current_skills)

    matched = sorted(current_skills & required_skills)

    score = int(
        len(matched) / len(required_skills) * 100
    )

    return f"""
# 🎯 Skill Gap Report

Target Role:
**{role.title()}**

---

## Match Score

**{score}%**

---

## Skills You Have

{", ".join(matched) if matched else "None"}

---

## Missing Skills

{", ".join(missing) if missing else "None"}

---

## Recommendation

Focus on learning the missing skills to improve your chances for this role.
"""