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

            # Display insights in DataFrame
            st.markdown("### 📊 Job Insights")
            df_insights = pd.DataFrame({
                "Technical Skills": [", ".join(technical_skills)],
                "Soft Skills": [", ".join(soft_skills)],
            })
            st.table(df_insights)

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
