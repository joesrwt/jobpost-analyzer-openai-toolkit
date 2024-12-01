import streamlit as st
import openai
import pandas as pd
import json

# Set page configuration
st.set_page_config(
    page_title="LinkedIn Job Post Analyzer & Mock Interview Toolkit",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sidebar for OpenAI API Key
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/174/174857.png", width=100)
st.sidebar.title("⚙️ Settings")
user_api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password")
st.sidebar.markdown("Enter your OpenAI API key to analyze LinkedIn job postings.")

# Header for the app
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #6A5ACD;">📄 LinkedIn Job Post: Analyzer & Mock Interview Toolkit</h1>
        <p style="font-size: 18px; color: #696969;">
            Extract insights from LinkedIn job postings and prepare for your interview with AI assistance!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Example Job Description, Responsibilities, and Requirements
job_example = """
**About the Job:**  
As a Data Scientist, you will be responsible for leveraging your expertise in data analysis, statistical modeling, and machine learning to solve complex business problems and drive data-driven decision-making. You will collaborate with cross-functional teams to analyze large datasets, extract actionable insights, and develop predictive models that contribute to the company’s strategic goals. This role requires proficiency in programming, data wrangling, and visualization, along with the ability to communicate findings to both technical and non-technical stakeholders.

**Key Responsibilities:**  
- Collect, clean, and preprocess large datasets from various sources  
- Develop and implement machine learning models to solve business challenges  
- Perform statistical analysis and data visualization to identify trends and insights  
- Collaborate with business stakeholders to understand their needs and provide actionable recommendations  
- Continuously evaluate and improve the performance of models and algorithms  
- Communicate findings and insights to both technical and non-technical teams through clear reports and presentations

**Key Qualifications:**  
- Strong proficiency in Python, R, or other data analysis languages  
- Experience with machine learning libraries and frameworks such as TensorFlow, PyTorch, or Scikit-learn  
- Solid understanding of statistics, data analysis, and data visualization  
- Familiarity with big data technologies (e.g., Hadoop, Spark) is a plus  
- Strong problem-solving skills and ability to think critically about data  
- Excellent communication and collaboration skills to work with cross-functional teams
"""

# Input 1: Job Information (description, responsibilities, requirements)
st.markdown("### 📝 Input Job Information (Job Description / Responsibilities / Requirements)")

# Display the example inside the text area as the default content (large input box)
job_post_description = st.text_area(
    "Paste the job description, responsibilities, and requirements here:",
    value=job_example,
    height=300  # Making the input box larger by increasing the height
)

# Prompt to analyze LinkedIn job post
job_post_prompt = """
You are an AI assistant that extracts technical skills, soft skills, and a summary of the key characteristics the company is looking for from LinkedIn job posts.
Given a LinkedIn job description, provide a summary in JSON format with the following fields:
- "Technical Skills": Key technical skills required for the role.
- "Soft Skills": Key soft skills required for the role.
- "Candidate
