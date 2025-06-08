import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="SNG - Home Page",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Content
st.markdown(
    """
    <div style="text-align: center; padding: 50px;">
        <h1 style="font-size: 60px; color: #4CAF50;">Welcome to SNG🌟 Text Analyzer</h1>
        <p style="font-size: 24px; color: white;">An automated system to create a more peaceful online environment, without any impurites.</p>
        <br><br>
        <a href="main">
            <button style="padding: 15px 30px; font-size: 20px; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer;">
                Explore Now
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)