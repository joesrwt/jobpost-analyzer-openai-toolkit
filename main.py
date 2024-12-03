import streamlit as st
import openai
import json
import pandas as pd

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
        <h1 style="color: black;">📄 LinkedIn Job Post: Analyzer & Mock Interview Toolkit</h1>
        <p style="font-size: 18px; color: black;">
            Extract key technical and soft skills from detailed job post and mock interview questions!
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Example Job Description, Responsibilities, and Requirements
job_example = """About The Job
Work closely with R&D engineering teams to build data analytics workflows and processes, develop statistics / physics / ML models that bring insights into valueadded analytics. Develop GenAI models that transform complex data sets into clear, actionable insights.#internship

About You
Master degree or PhD degree graduate student in Computer Science Engineering, Electrical Engineering, Mechanical Engineering, Physics fields.
Passionate about data and analytics with AI/ML capabilities.
Ability to work independently with proven problem-solving skills and out-of-box thinking mindset.
Good communication and teamwork skills needed in collaborative cross functional team environment.
Design, develop and deliver data science solutions

Your Experience Includes
Develop python rule-based and ML/DL model on time series data, image data, and parametric data.
PyTorch or Tensorflow framework.
Statistics models & ML algorithms such as multi-class classifications, decision trees and deep learning. Image AI, computer vision, OpenCV and TensorFlow.

You Might Also Have
Data engineering skills including API, Airflow, Spark, Docker and Kubernetes.
Proficiency with Linux OS and terminal command line is a plus.
Version control such as Git or SVN.
Web based dashboard and visualization
"""

# Input 1: Job Information (description, responsibilities, requirements)
st.markdown("### 📝 Input Job Information (Job Description / Responsibilities / Requirements)")

# Display the example inside the text area as the default content (large input box)
job_post_description = st.text_area(
    "Paste the job description, responsibilities, and requirements here:",
    value=job_example,
    height=310  
)

# Prompt to analyze LinkedIn job post
job_post_prompt = """
You are an AI assistant that extracts technical skills, soft skills, and a summary of the key characteristics the company is looking for from LinkedIn job posts.
Given a LinkedIn job description, extract a summary in the following fields:
- "Technical Skills": Key technical skills required for the role, it can also be tools or programming languages
- "Soft Skills": Key soft skills required for the role.
- "Candidate Profile": A summary of the key traits or qualities the company is seeking in a candidate, such as personality traits or professional qualities, make it short and clear within 3 sentences.

Example output:
{
    "Technical Skills": ["Python", "Machine Learning", "Data Analysis", "SQL", "Hadoop", "NLP"],
    "Soft Skills": ["Collaboration", "Adaptability", "Communication"],
    "Candidate Profile": "The ideal candidate is a strategic thinker, innovative, data-driven, collaborative, and results-oriented, with excellent communication skills."
}
"""

# Input 2: Mock interview question
mock_interview_prompt = """
Based on the technical skills, soft skills, and candidate profile extracted from the LinkedIn job post, generate 3 example interview questions.
Questions should help the candidate prepare for real-life scenarios based on the job requirements. no need to show json file of the extracted information

Example output:
1. Technical Skills Question: 
Can you describe a project where you collected, cleaned, and transformed data from multiple sources for analysis? What tools did you use, and how did your analysis contribute to decision-making processes?
   
2. Soft Skills Question: 
How have you demonstrated your ability to collaborate with others in a team setting, using your strong English communication skills? Can you provide an example of a successful project where collaboration and effective communication played a crucial role?
   
3. Candidate Profile Question:
Tell me about a time when you had to think creatively to solve a data-related challenge. How did you approach the problem, connect the dots, and propose innovative solutions?
"""

# Custom CSS for button and output text colors
st.markdown(
    """
    <style>
        .stButton button {
            background-color: #90EE90;  /* Light Green */
            color: black;
        }
        .stTextArea textarea {
            color: black;  /* Black text for output */
        }
        .stMarkdown {
            color: black;  /* Black text for output */
        }
        .stMarkdown h2, .stMarkdown h3 {
            color: black;  /* Black color for titles */
        }
    </style>
    """, unsafe_allow_html=True)

# Submit button for generating insights and mock interview questions
if st.button("🚀 Analyze & Generate Insights"):
    if not user_api_key:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar to proceed.")
    elif not job_post_description.strip():
        st.error("⚠️ Please input the job description text.")
    else:
        # Initialize OpenAI client using the provided API key
        client = openai.OpenAI(api_key=user_api_key)

        # Call OpenAI API to extract insights from job post
        messages = [
            {"role": "system", "content": job_post_prompt},
            {"role": "user", "content": job_post_description}
        ]
        response_insight = client.chat.completions.create(
             model="gpt-3.5-turbo",
             messages=messages)
        # Parse insights
        insights = json.loads(response_insight.choices[0].message.content)
        technical_skills = insights.get("Technical Skills", [])
        soft_skills = insights.get("Soft Skills", [])
        candidate_profile = insights.get("Candidate Profile", "")

        # Display insights in tables
        st.markdown("### 📊 Job Insights")

        # Create a DataFrame for Technical Skills with checkboxes
        technical_skills_df = pd.DataFrame({"Technical Skills": technical_skills})
        technical_skills_df.index += 1  # Set index starting from 1
        
        # Add a column with checkboxes
        technical_skills_df["Skill Acquired"] = [st.checkbox(f"✔ {skill}", key=f"tech_{i}") for i, skill in enumerate(technical_skills)]

        # Create a DataFrame for Soft Skills with checkboxes
        soft_skills_df = pd.DataFrame({"Soft Skills": soft_skills})
        soft_skills_df.index += 1  # Set index starting from 1
        
        # Add a column with checkboxes
        soft_skills_df["Skill Acquired"] = [st.checkbox(f"✔ {skill}", key=f"soft_{i}") for i, skill in enumerate(soft_skills)]
        
        # Display the tables for Technical Skills and Soft Skills
        st.subheader("🔧 Technical Skills")
        st.table(technical_skills_df)

        st.subheader("🤝 Soft Skills")
        st.table(soft_skills_df)

        # Display Candidate Profile as text
        st.markdown("### 🏆 Ideal Candidate Profile")
        st.text_area(
            "Key traits of the ideal candidate:",
            value=candidate_profile,
            height=150,
            disabled=True  # Make it read-only
        )

        # Generate interview questions based on insights
        messages.append({
            "role": "system",
            "content": mock_interview_prompt,
        })
        response_questions = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Display questions in text area
        example_questions = response_questions.choices[0].message.content
        st.markdown("### 🗨️ Mock Interview Questions")
        st.text_area(
            "Example interview questions in 3 aspects:",
            value=example_questions,
            height=300,
            disabled=True
        )
