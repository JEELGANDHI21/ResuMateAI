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

with st.expander("Resume Analysis Options"):
    submit1 = st.button("Job Description Insights")
    submit2 = st.button("Skills Gap Analysis")
    submit3 = st.button("Resume Percentage Match")
    submit4 = st.button("ATS Compatibility Check")
    submit5 = st.button("Resume Feedback")
    submit6 = st.button("Generate Optimized Resume")
    submit7 = st.button("Generate Cover Letter")


def generate_response(prompt):
    if uploaded_file is not None:

        pdf_content = extractPDF(uploaded_file)

        response = sendRequest(jd_input, pdf_content, prompt)

        st.subheader("Generated Response:")
        st.write(response)
    else:
        st.warning("Please upload a resume to proceed!")


def generate_pdf(prompt):
    if uploaded_file is not None:

        pdf_content = extractPDF(uploaded_file)

        optimized_text = sendRequest(jd_input, pdf_content, prompt)

        input_filename = uploaded_file.name.split('.')[0]
        optimized_filename = createPDF(optimized_text, input_filename)

        if optimized_filename:
            with open(optimized_filename, "rb") as file:
                st.download_button("Click Here to Download Generated File", file, file_name=optimized_filename)
        else:
            st.error("There was an issue generating the optimized resume.")
    else:
        st.warning("Please upload a resume to proceed!")


if submit1:
    generate_response(prompt1)
elif submit2:
    generate_response(prompt2)
elif submit3:
    generate_response(prompt3)
elif submit4:
    generate_response(prompt4)
elif submit5:
    generate_response(prompt5)
elif submit6:
    generate_pdf(prompt6)
elif submit7:
    generate_pdf(prompt7)