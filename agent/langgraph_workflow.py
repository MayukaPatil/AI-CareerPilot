from typing import TypedDict

from services.router import detect_intent

from langgraph.graph import StateGraph, END

from services.llm_service import ask_llm


class CareerState(TypedDict):
    question: str
    answer: str
    intent: str

def router_node(state: CareerState):

    intent = detect_intent(state["question"])

    return {
        "intent": intent
    }    


def chatbot_node(state: CareerState):

    answer = ask_llm(state["question"])

    return {
        "answer": answer
    }


builder = StateGraph(CareerState)

builder.add_node("router", router_node)
builder.add_node("chatbot", chatbot_node)

builder.set_entry_point("router")

builder.add_edge("router", "chatbot")
builder.add_edge("chatbot", END)

career_graph = builder.compile()