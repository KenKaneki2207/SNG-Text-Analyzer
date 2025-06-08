import streamlit as st

# Page Layout
st.set_page_config(
    page_title="SNG - How it works?",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state='collapsed'
)

# Center-align all content
st.markdown("""
    <style>
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #ffffff;
        color: #333333;
        text-align: center; /* Center-align all text */
    }
    .stTextInput > div > div > input, textarea {
        background-color: #f9f9f9;
        color: #333333;
        border: 1px solid #cccccc;
        margin: 0 auto; /* Center-align input fields */
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 0.375rem;
        padding: 0.5rem 1rem;
        margin: 0 auto; /* Center-align button */
        display: block;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h2>🌟 SNG Toxic Comment Detector</h2>", unsafe_allow_html=True)
st.markdown("Welcome to our Toxic Comment Detector.")


# Feature Images
st.markdown("### Key Features")
col1, col2 = st.columns(2)

with col1:
    st.image("images/network.jpg", caption="Feature 1: BERT Model Analysis ", use_container_width=True)

with col2:
    st.image("images/result.jpg", caption="Feature 2: Instant Results", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)


# How it Works
st.markdown("### How it Works?")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/step1.jpg", caption="Step 1: Write Comment", use_container_width=True)

with col2:
    st.image("images/step2.jpg", caption="Step 2: Comment analysis", use_container_width=True)

with col3:
    st.image("images/step3.jpg", caption="Step 3: Result (✅❌)", use_container_width=True)


st.markdown("<br>", unsafe_allow_html=True)


# Button to BERT model
st.markdown(
"""
<br></b>
<div style="text-align: center;">
    <a href="app" style="
        font-size: 20px;
        padding: 0.5em 1.5em;
        border-radius: 8px;
        border: none;
        background-color: #ffd872;
        color: black;
        text-decoration: none;
        display: inline-block;
        cursor: pointer;
    ">
        💬 Try It Out
    </a>
</div>
""",
unsafe_allow_html=True
)