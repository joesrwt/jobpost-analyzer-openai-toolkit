curl -fsSL https://docs.grit.io/install | bash
grit install
grit apply openai

import streamlit as st
import pandas as pd
import json
from openai import OpenAI
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
job_example = """**About the Job:**  
Do you have a passion in Data Analyst?
Our Data Analyst Internship Programme has been crafted to simulate our Graduate Programme so that you can understand what a career in technology at London Stock Exchange Group (LSEG) would really be like.

At LSEG, we consider on providing opportunities equally as a priority, we strive to establish teams that are diverse and encourage coordinated working and sharing of ideas!
At LSEG Bangkok, you can be your best self. Our open and inclusive culture and collaborative communities connect colleagues from across the world, and a host of skill development programmes support our people's personal and professional growth.

**What your internship will include:**
We are looking for undergraduates student who will support our Data Analyst team in collecting, cleaning, and transforming data from different sources
Perform data analysis using your weapon of choice - either Tableau or Power BI
Perform data manipulation, analysis, and forecasting via MS Excel
Learn how to analyse and capture insights using real world data
Learn what service intelligence is and it's impact
Work with partners across the globe
Get to be part of world's leading fintech company

**What we are looking for:**
You will have an interest in technology demonstrated either via your academic studies, work experience, or extracurricular activities. For instance, you may be part of a Computing Society, have taught yourself how to code or have focused on technology as part of a university project.

Basic SQL, will be a good starting point to have for this internship
Although not a requirement if you understood Python, Power BI, and Tableau skills this would be a plus
A curiosity for data and an ability to analyse information to draw conclusions and propose solutions.
Individuals who are able to connect the dots and think creatively.
People who can collaborate with others, using their strong English communication skills in the process. (written and verbal)

To be apply, you must be a penultimate year student due to complete your degree 2026. You should have a good grade and studying a technology, engineering or computing related degree. 
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
- "Candidate Profile": A summary of the key traits or qualities the company is seeking in a candidate, such as work ethic, personality traits, or professional qualities.

Example output:
{
    "Technical Skills": ["Python", "Machine Learning", "Data Analysis", "SQL"],
    "Soft Skills": ["Collaboration", "Adaptability", "Communication"],
    "Candidate Profile": "The ideal candidate is a strategic thinker, innovative, data-driven, collaborative, and results-oriented, with excellent communication skills."
}
"""

# Input 2: Mock behavioral interview question
mock_interview_prompt = """
Based on the technical skills, soft skills, and candidate profile extracted from the LinkedIn job post, generate 3 example behavioral interview questions.
Questions should help the candidate prepare for real-life scenarios based on the job requirements.
"""

# Submit button for generating insights and mock interview questions
if st.button("🚀 Analyze & Generate Insights"):
    if not user_api_key:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar to proceed.")
    elif not job_post_description.strip():
        st.error("⚠️ Please input the job description text.")
    else:
        try:
            # Initialize OpenAI client
            openai.api_key = user_api_key

            # Call OpenAI API to extract insights from job post
            messages = [
                {"role": "system", "content": job_post_prompt},
                {"role": "user", "content": job_post_description}
            ]

            response_insights = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Parse insights
            insights = json.loads(response_insights["choices"][0]["message"]["content"])
            technical_skills = insights.get("Technical Skills", [])
            soft_skills = insights.get("Soft Skills", [])
            candidate_profile = insights.get("Candidate Profile", "")

            # Display insights in columns
            st.markdown("### 📊 Job Insights")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🔧 Technical Skills")
                st.write(", ".join(technical_skills))

            with col2:
                st.subheader("🤝 Soft Skills")
                st.write(", ".join(soft_skills))

            # Display Candidate Profile as text
            st.markdown("### 🏆 Ideal Candidate Profile")
            st.text_area(
                "Key traits of the ideal candidate:",
                value=candidate_profile,
                height=150,
                disabled=True  # Make it read-only
            )

            # Generate behavioral interview questions based on insights
            messages.append({
                "role": "system",
                "content": mock_interview_prompt,
            })
            response_questions = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Display behavioral questions in text area
            example_questions = response_questions["choices"][0]["message"]["content"]
            st.markdown("### 🗨️ Mock Behavioral Interview Questions")
            st.text_area(
                "Example behavioral interview questions:",
                value=example_questions,
                height=150,
                disabled=True  # Make it read-only
            )

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

# Footer
st.markdown(
    """
    <hr>
    <div style="text-align: center; color: #696969;">
        <p>Sorawit Huang 6542118426</p>
    </div>
    """,
    unsafe_allow_html=True,
)

