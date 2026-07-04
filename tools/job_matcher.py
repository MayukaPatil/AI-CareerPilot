from langchain.tools import tool


@tool
def job_matcher(resume: str, job_description: str) -> str:
    """
    Compare a resume with a job description.
    """

    resume_lower = resume.lower()
    jd_lower = job_description.lower()

    keywords = [
        "python",
        "sql",
        "power bi",
        "tableau",
        "excel",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pandas",
        "numpy",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "statistics",
        "communication",
        "leadership"
    ]

    matched = []
    missing = []

    for skill in keywords:
        if skill in jd_lower:
            if skill in resume_lower:
                matched.append(skill)
            else:
                missing.append(skill)

    if len(matched) + len(missing) == 0:
        score = 0
    else:
        score = int(
            len(matched) /
            (len(matched) + len(missing))
            * 100
        )

    return f"""
# 📊 Resume vs Job Description

## Match Score

**{score}%**

---

## Matching Skills

{", ".join(matched) if matched else "None"}

---

## Missing Skills

{", ".join(missing) if missing else "None"}

---

## Suggestions

• Add the missing skills if you have experience.

• Customize your resume for this job.

• Highlight projects related to the matching skills.
"""