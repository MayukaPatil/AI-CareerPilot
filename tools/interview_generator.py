from langchain.tools import tool
from tools.resume_parser import parse_resume


@tool
def interview_generator(resume: str) -> str:
    """
    Generate interview questions based on detected skills.
    """

    data = parse_resume(resume)

    skills = data["skills"]

    if not skills:
        return """
Couldn't identify enough technical skills.

Please upload a more detailed resume.
"""

    questions = []

    for skill in skills:

        if skill == "python":
            questions.extend([
                "Explain Python decorators.",
                "Difference between list and tuple.",
                "What are generators?",
                "Explain *args and **kwargs."
            ])

        elif skill == "sql":
            questions.extend([
                "Difference between WHERE and HAVING.",
                "Explain Window Functions.",
                "Write a query for second highest salary.",
                "Difference between RANK and DENSE_RANK."
            ])

        elif skill == "power bi":
            questions.extend([
                "Difference between calculated column and measure.",
                "Explain STAR Schema.",
                "What is DAX?",
                "What are relationships?"
            ])

        elif skill == "machine learning":
            questions.extend([
                "Bias vs Variance.",
                "What is Overfitting?",
                "Explain Cross Validation.",
                "Difference between Bagging and Boosting."
            ])

        elif skill == "langchain":
            questions.extend([
                "What is Retrieval Augmented Generation (RAG)?",
                "What are AI Agents?",
                "Difference between Tools and Chains.",
                "What is LangGraph?"
            ])

        else:
            questions.append(
                f"Explain your experience using {skill}."
            )

    # Remove duplicates
    questions = list(dict.fromkeys(questions))

    result = "# 🎤 Personalized Interview Questions\n\n"

    for i, question in enumerate(questions, 1):
        result += f"{i}. {question}\n"

    return result