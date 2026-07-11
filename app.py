import re
import streamlit as st

from styles import load_css

from tools.pdf_reader import extract_resume_text
from tools.resume_feedback import resume_feedback
from tools.ats_checker import ats_checker
from tools.interview_generator import interview_generator
from tools.cover_letter import cover_letter
from tools.job_matcher import job_matcher

from services.router import detect_intent
from agent.langgraph_workflow import career_graph


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# SAFE SESSION STATE INIT
# ==========================

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "resume" not in st.session_state:
    st.session_state["resume"] = None

if "assistant_reply" not in st.session_state:
    st.session_state["assistant_reply"] = ""

if "ats_score" not in st.session_state:
    st.session_state["ats_score"] = "--"

if "job_match" not in st.session_state:
    st.session_state["job_match"] = "--"

if "resume_review" not in st.session_state:
    st.session_state["resume_review"] = "--"

load_css()


# ==================================================
# SESSION STATE
# ==================================================

defaults = {
    "messages": [],
    "ats_score": "--",
    "job_match": "--",
    "resume_score": "--",
    "assistant_reply": ""
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("# 🚀 CareerPilot AI")

    st.caption(
    "AI Resume Analyzer • ATS Checker • Job Match • Interview Prep • Career Assistant"
)

    st.divider()

    uploaded_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

    job_description = st.text_area(
        "📋 Job Description",
        height=200,
        placeholder="Paste the job description here..."
    )


# ==================================================
# SAVE RESUME
# ==================================================

if uploaded_file is not None:

    if (
        "resume" not in st.session_state
        or st.session_state.get("uploaded_name") != uploaded_file.name
    ):

        resume_text = extract_resume_text(uploaded_file)

        st.session_state["resume"] = resume_text
        st.session_state["uploaded_name"] = uploaded_file.name

        st.success("✅ Resume uploaded successfully!")


# ==================================================
# HERO
# ==================================================

st.title("🚀 CareerPilot AI")
st.caption("AI Resume Analyzer • ATS • Job Match • Interview Prep")


# ==================================================
# DASHBOARD
# ==================================================


st.header("📊 Dashboard")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        label="⭐ ATS Score",
        value=st.session_state["ats_score"],
        delta=None
    )

with c2:
    st.metric(
        label="🎯 Job Match",
        value=st.session_state["job_match"],
        delta=None
    )

with c3:
    st.metric(
        label="📄 Resume Review",
        value=st.session_state["resume_review"],
        delta=None
    )
#🎯 Job Match
#📄 Resume Review

st.write("")


# ==================================================
# FEATURES
# ==================================================
st.subheader("✨ Features")
st.divider()

c1,c2 = st.columns(2)

with c1:
    st.info("""
✅ ATS Checker

✅ Resume Review

✅ Skill Gap Analysis
""")

with c2:
    st.info("""
✅ Job Match

✅ Cover Letter

✅ Interview Questions
""")

# ==================================================
# QUICK ACTIONS
# ==================================================

st.markdown("## ⚡ Quick Actions")
st.divider()





a, b, c, d = st.columns(4)

# ---------------- Resume Review ----------------
with a:
    if st.button("📄 Resume Review", use_container_width=True):

        if "resume" not in st.session_state:
            st.warning("Upload resume first")
        else:
            result = resume_feedback.invoke(
                {"resume": st.session_state["resume"]}
            )

            st.session_state["assistant_reply"] = result
            st.session_state["resume_score"] = "Reviewed ✅"

# ---------------- ATS Score ----------------
with b:
    if st.button("⭐ ATS Score", use_container_width=True):

        if "resume" not in st.session_state:
            st.warning("Upload resume first")
        else:
            result = ats_checker.invoke(
                {"resume": st.session_state["resume"]}
            )

            import re
            match = re.search(r"(\d+)", result)

            if match:
                score = match.group(1)
                st.session_state["ats_score"] = f"{score}%"

            st.session_state["assistant_reply"] = result

# ---------------- Interview ----------------
with c:
    if st.button("🎤 Interview Prep", use_container_width=True):

        if "resume" not in st.session_state:
            st.warning("Upload resume first")
        else:
            result = interview_generator.invoke(
                {"resume": st.session_state["resume"]}
            )

            st.session_state["assistant_reply"] = result

# ---------------- Cover Letter ----------------
with d:
    if st.button("💼 Cover Letter", use_container_width=True):

        if "resume" not in st.session_state:
            st.warning("Upload resume first")

        elif not job_description.strip():
            st.warning("Paste job description first")

        else:
            result = cover_letter.invoke({
                "resume": st.session_state["resume"],
                "job_description": job_description
            })

            st.session_state["assistant_reply"] = result


# ==================================================
# SHOW TOOL OUTPUT
# ==================================================

if st.session_state["assistant_reply"]:

    st.markdown("---")

    with st.chat_message("assistant"):

        st.markdown(st.session_state["assistant_reply"])

    st.download_button(
        "📥 Download Report",
        data=st.session_state["assistant_reply"],
        file_name="careerpilot_report.txt",
        mime="text/plain"
    )

st.divider()

# ==================================================
# AI CAREER CHAT
# ==================================================

st.markdown("## 💬 AI Career Assistant")
st.caption("Ask anything about your resume, ATS score, interview preparation, or career.")

# Show previous chat messages
for message in st.session_state["messages"]:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
question = st.chat_input(
    "Ask me anything about your resume, ATS score, interview preparation, or career..."
)

if question:

    # Resume check
    if "resume" not in st.session_state:
        st.warning("📄 Please upload your resume first using the sidebar.")
        st.stop()

    resume = st.session_state["resume"]

    # Detect intent (optional, but keeping your logic)
    intent = detect_intent(question)

    # Save user message
    st.session_state["messages"].append({
        "role": "user",
        "content": question
    })

    # Show user message
    with st.chat_message("user"):
        st.markdown(question)

    # ---------------- AI RESPONSE ----------------

    prompt = f"""
Resume:
{resume}

Question:
{question}
"""

    result = career_graph.invoke({"question": prompt})

    answer = result["answer"]

    # Save assistant message
    st.session_state["messages"].append({
        "role": "assistant",
        "content": answer
    })

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(answer)

        # -----------------------------------
        # Resume Review
        # -----------------------------------

        if intent == "review":

            answer = resume_feedback.invoke(
                {
                    "resume": resume
                }
            )

            st.session_state["resume_score"] = "Reviewed ✅"

        # -----------------------------------
        # ATS
        # -----------------------------------

        elif intent == "ats":

            answer = ats_checker.invoke(
                {
                    "resume": resume
                }
            )

            import re

            match = re.search(r"(\d+)", answer)

            if match:
                st.session_state["ats_score"] = match.group(1) + "%"

        # -----------------------------------
        # Interview
        # -----------------------------------

        elif intent == "interview":

            answer = interview_generator.invoke(
                {
                    "resume": resume
                }
            )

        # -----------------------------------
        # Cover Letter
        # -----------------------------------

        elif intent == "cover_letter":

            if job_description.strip():

                answer = cover_letter.invoke(
                    {
                        "resume": resume,
                        "job_description": job_description
                    }
                )

            else:

                answer = "⚠️ Please paste the Job Description in the sidebar."

        # -----------------------------------
        # Job Match
        # -----------------------------------

        elif (
            "job match" in question.lower()
            or "match my resume" in question.lower()
            or "compare resume" in question.lower()
        ):

            if job_description.strip():

                answer = job_matcher.invoke(
                    {
                        "resume": resume,
                        "job_description": job_description
                    }
                )

                import re

                match = re.search(r"(\d+)", answer)

                if match:
                    st.session_state["job_match"] = match.group(1) + "%"

            else:

                answer = "⚠️ Please paste the Job Description."

        # -----------------------------------
        # General AI Chat
        # -----------------------------------

        else:

            prompt = f"""
You are CareerPilot AI.

Resume:
{resume}

User Question:
{question}
"""

            result = career_graph.invoke({"question": prompt})

            answer = result["answer"]

        # Save assistant response
        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(answer)

            

if "assistant_reply" in st.session_state:
    st.markdown(st.session_state["assistant_reply"])

    st.markdown("---")

st.caption(
    "🚀 CareerPilot AI • Built with Streamlit, LangChain, LangGraph & Groq | © 2026"
)

