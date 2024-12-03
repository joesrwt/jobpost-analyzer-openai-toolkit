import streamlit as st
import openai
import PyPDF2
import json
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="LinkedIn Job Analyzer",
    page_icon="🔍",
    layout="centered"
)

# Sidebar for OpenAI API Key
st.sidebar.title("API Key Configuration")
user_api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
st.sidebar.markdown("Enter your OpenAI API key to proceed.")

# Main application
st.title("LinkedIn Job Post Analyzer & Resume Skill Matcher")
st.markdown("Analyze job posts, generate insights, prepare interview questions, and match resume skills with job requirements.")

# Example job description
job_example = """About The Job
Work closely with R&D engineering teams to build data analytics workflows and processes, develop statistics / physics / ML models that bring insights into value-added analytics. Develop GenAI models that transform complex data sets into clear, actionable insights.

Your Experience Includes
- Develop python rule-based and ML/DL model on time series data, image data, and parametric data.
- PyTorch or Tensorflow framework.
- Statistics models & ML algorithms such as multi-class classifications, decision trees, and deep learning.
- Image AI, computer vision, OpenCV, and TensorFlow.
- Data engineering skills including API, Airflow, Spark, Docker, and Kubernetes.
"""

# Input: Job description
st.subheader("Step 1: Input Job Description")
job_post_description = st.text_area(
    "Paste the job description here:",
    value=job_example,
    height=300
)

# Upload Resume PDF Section
st.subheader("Step 2: Upload Your Resume (Optional)")
uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

# Define prompts
job_post_prompt = """
You are an AI assistant. Extract the following from the given job description:
1. Insights: List the technical skills, soft skills, and candidate qualities required for the job.
2. Interview Questions: Generate a list of potential interview questions based on the job description.
Format the output as JSON with these keys: "Technical Skills", "Soft Skills", "Candidate Profile", "Interview Questions".
"""

resume_skill_match_prompt = """
You are an AI assistant. Given the following:
1. A list of technical skills extracted from a job description.
2. A resume (in plain text).
Identify:
- Which technical skills are present in the resume.
- Which technical skills are missing from the resume.
Return the result as a JSON object with keys: "Matched Skills" and "Missing Skills".
"""

# Analyze job description and match skills
if st.button("Analyze Job Description & Match Resume Skills"):
    if not user_api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif not job_post_description.strip():
        st.error("Please input a job description.")
    else:
        try:
            # Initialize OpenAI client
            client = openai.OpenAI(api_key=user_api_key)

            # Call OpenAI API to extract insights from the job post
            messages = [
                {"role": "system", "content": job_post_prompt},
                {"role": "user", "content": job_post_description}
            ]
            response_insight = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            insights = json.loads(response_insight['choices'][0]['message']['content'])

            # Display job insights
            st.subheader("Job Insights")
            st.write("### Technical Skills")
            st.table(pd.DataFrame({"Technical Skills": insights["Technical Skills"]}))
            st.write("### Soft Skills")
            st.table(pd.DataFrame({"Soft Skills": insights["Soft Skills"]}))
            st.write("### Candidate Profile")
            st.text_area("Candidate Profile", value=insights["Candidate Profile"], height=100, disabled=True)

            # Display interview questions
            st.write("### Potential Interview Questions")
            st.table(pd.DataFrame({"Interview Questions": insights["Interview Questions"]}))

            # Resume processing
            if uploaded_file:
                # Extract text from resume PDF
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                resume_text = " ".join(page.extract_text() for page in pdf_reader.pages)

                # Match skills between resume and job post
                messages_resume = [
                    {"role": "system", "content": resume_skill_match_prompt},
                    {
                        "role": "user",
                        "content": json.dumps({
                            "Technical Skills": insights["Technical Skills"],
                            "Resume": resume_text
                        })
                    }
                ]
                response_resume = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages_resume
                )
                skill_match = json.loads(response_resume['choices'][0]['message']['content'])

                # Display resume skill match results
                st.subheader("Resume Skill Match")
                st.write("### Matched Skills")
                st.table(pd.DataFrame({"Matched Skills": skill_match["Matched Skills"]}))
                st.write("### Missing Skills")
                st.table(pd.DataFrame({"Missing Skills": skill_match["Missing Skills"]}))
            else:
                st.warning("No resume uploaded. Please upload a resume to match skills.")

        except Exception as e:
            st.error(f"Error: {e}")

