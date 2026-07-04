import re


TECH_SKILLS = [
    "python",
    "sql",
    "power bi",
    "tableau",
    "excel",
    "machine learning",
    "deep learning",
    "tensorflow",
    "keras",
    "pandas",
    "numpy",
    "scikit-learn",
    "streamlit",
    "flask",
    "langchain",
    "langgraph",
    "git",
    "github",
    "docker",
    "aws",
    "azure"
]


SECTIONS = [
    "education",
    "skills",
    "projects",
    "experience",
    "certifications",
    "achievements"
]


def parse_resume(resume: str):

    text = resume.lower()

    skills = [
        skill
        for skill in TECH_SKILLS
        if skill in text
    ]

    sections = {
        section: section in text
        for section in SECTIONS
    }

    email = bool(
        re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            resume
        )
    )

    phone = bool(
        re.search(
            r"\d{10}",
            resume.replace(" ", "")
        )
    )

    github = "github.com" in text

    linkedin = "linkedin.com" in text

    quantified = bool(
        re.search(
            r"\d+%|\d+\+",
            text
        )
    )

    return {
        "skills": skills,
        "sections": sections,
        "email": email,
        "phone": phone,
        "github": github,
        "linkedin": linkedin,
        "quantified": quantified
    }