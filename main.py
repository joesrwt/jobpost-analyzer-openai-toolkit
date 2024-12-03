import PyPDF2
import openai
import streamlit as st

# Add file uploader for job post and resume
st.markdown("### 📄 Upload the Job Post")
uploaded_job_post = st.file_uploader("Upload the job post as PDF:", type=["pdf"])

st.markdown("### 📄 Upload Your Resume")
uploaded_resume = st.file_uploader("Upload your resume as PDF:", type=["pdf"])

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

# Step 1: Extract Key Skills from Job Post (Using GPT)
job_post_prompt = """
You are a resume analyzer. The task is to extract key technical skills mentioned in the job post. These skills may be specific technologies, programming languages, or tools relevant to the job position.

Here is the job post text:
[Job Post Text Here]

Output the key technical skills in bullet points.
"""

# Step 2: Analyze Resume for Missing Skills
resume_gap_analysis_prompt = """
You are an AI assistant that reads through resumes and identifies if the candidate has the required technical skills based on their experience. 
Given a resume and the skills required for the job, determine which of the skills are missing in the candidate’s work experience.

The technical skills required for the job are:
- [Skills List Here]

Here is the applicant's experience section:
[Resume Experience Text Here]

Output the missing skills, if any, and provide a brief explanation.
"""

# Analyze the job post if uploaded
if uploaded_job_post and uploaded_resume:
    try:
        # Extract text from uploaded PDF job post and resume
        job_post_text = extract_text_from_pdf(uploaded_job_post)
        resume_text = extract_text_from_pdf(uploaded_resume)
        
        # Display progress message
        st.markdown("🛠️ Analyzing the job post and your resume...")

        # Extract key skills from job post
        formatted_job_post_prompt = job_post_prompt.replace("[Job Post Text Here]", job_post_text)
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=formatted_job_post_prompt,
            max_tokens=500
        )

        job_post_skills = response.choices[0].text.strip().split("\n")
        st.markdown("### 📋 Key Technical Skills from the Job Post")
        st.text_area("Key Skills from the Job Post", value="\n".join(job_post_skills), height=150, disabled=True)

        # Analyze resume for missing skills based on extracted job post skills
        formatted_resume_prompt = resume_gap_analysis_prompt.replace("[Skills List Here]", "\n".join(job_post_skills))
        formatted_resume_prompt = formatted_resume_prompt.replace("[Resume Experience Text Here]", resume_text)

        # OpenAI API call to check for missing skills in the resume
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=formatted_resume_prompt,
            max_tokens=500
        )

        analysis_output = response.choices[0].text.strip()

        # Display missing skills analysis
        st.markdown("### 🔍 Missing Skills Analysis")
        st.text_area("Missing skills or experience gap analysis:", value=analysis_output, height=250, disabled=True)

    except Exception as e:
        st.error(f"⚠️ An error occurred: {str(e)}")
else:
    if not uploaded_job_post:
        st.info("Please upload the job post to begin the analysis.")
    if not uploaded_resume:
        st.info("Please upload your resume to begin the analysis.")
