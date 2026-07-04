def detect_intent(question: str) -> str:

    question = question.lower()

    if any(word in question for word in [
        "ats",
        "resume score",
        "ats score",
        "keyword"
    ]):
        return "ats"

    if any(word in question for word in [
        "review",
        "feedback",
        "analyze resume",
        "improve resume"
    ]):
        return "review"

    if any(word in question for word in [
        "interview",
        "mock interview",
        "questions"
    ]):
        return "interview"

    if any(word in question for word in [
        "cover letter",
        "generate cover letter",
        "write cover letter"
    ]):
        return "cover_letter"

    return "chat"