import streamlit as st
from prompts import *
from utils import extractPDF,sendRequest,createPDF

st.set_page_config(page_title='ResuMateAI', layout="wide")

st.title('ResuMateAI')
st.markdown('Optimize your resume for ATS with AI-driven insights and personalized feedback!')


st.sidebar.header('Navigation')
st.sidebar.markdown("""
    - **Job Description Input**: Paste the job description you're applying to.
    - **Resume Upload**: Upload your resume in PDF format for analysis.
    - **Analysis Options**: Use the buttons to get valuable insights and suggestions.
""")

with st.container():
    st.header("Job Description & Resume")
    jd_input = st.text_area(
        "Enter Job Description",
        placeholder="Paste the job description here.",
        key="text",
        height=150,
        help="Paste the job description for the position you're applying for."
    )

    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"], label_visibility="collapsed")
    if uploaded_file:
        st.success("Resume uploaded successfully!")

st.header("AI-Generated Insights & Feedback")
st.markdown(
    "<p style='font-size:14px; color:#777;'>Click on the buttons below to get actionable insights and recommendations.</p>",
    unsafe_allow_html=True
)