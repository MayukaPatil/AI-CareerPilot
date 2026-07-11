import streamlit as st

def load_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* App background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef4ff 50%,
        #f8fbff 100%
    ) !important;
}

/* Main content should stay transparent */
[data-testid="stMain"] {
    background: transparent !important;
}

[data-testid="stMainBlockContainer"] {
    background: transparent !important;
}

.glass{
    background:rgba(255,255,255,0.88);
    backdrop-filter:blur(12px);
    -webkit-backdrop-filter:blur(12px);
    border-radius:20px;
    padding:30px;
    border:1px solid #d1d5db;
    box-shadow:0 10px 30px rgba(0,0,0,0.10);
    margin-bottom:18px;
}

    .stButton>button{
        width:100%;
        border-radius:20px;
        height:50px;
        background:#4f46e5;
        color:white;
        border:none;
    }
                
    .stApp {
    background: linear-gradient(
        135deg,
        #fbfcff,
        #f3f6ff,
        #eef4ff
    ) !important;
}

                
    /* Better headings */

h1 {
    font-size: 2.8rem !important;
    font-weight: 800 !important;
}

h2 {
    font-size: 2rem !important;
    font-weight: 700 !important;
}

h3 {
    font-size: 1.5rem !important;
    font-weight: 600 !important;
}

    </style>
    """, unsafe_allow_html=True)

