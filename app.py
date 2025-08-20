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