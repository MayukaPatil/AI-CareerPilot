import streamlit as st

def load_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, .stApp{
        font-family:'Inter',sans-serif;
    }

    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}

    .stApp{
        background:#f8fafc;
    }

    section[data-testid="stSidebar"]{
        background:#ffffff;
    }

    .glass{
        background:white;
        border-radius:18px;
        padding:20px;
        border:1px solid #e5e7eb;
        box-shadow:0 4px 18px rgba(0,0,0,.05);
    }

    .stButton>button{
        width:100%;
        border-radius:12px;
        height:50px;
        background:#4f46e5;
        color:white;
        border:none;
    }

    </style>
    """, unsafe_allow_html=True)