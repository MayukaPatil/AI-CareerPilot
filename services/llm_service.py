from langchain_core.messages import HumanMessage

from agent.career_agent import agent


def ask_llm(prompt: str):

    try:
        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        return response["messages"][-1].content

    except Exception as e:
        return (
            "⚠️ The AI service is temporarily unavailable or you've reached "
            "the API rate limit. Please wait a while and try again."
        )