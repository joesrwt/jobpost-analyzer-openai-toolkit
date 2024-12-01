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
job_example = """About the job
The ideal candidate's favorite words are learning, data, scale, and agility. You will leverage your strong collaboration skills and ability to extract valuable insights from highly complex data sets to ask the right questions and find the right answers.

**Responsibilities**
Translate business issues into specific requirements to develop the analytics solutions
Develop Statistical / Machine Learning models e.g. Segmentation, Propensity, Recommendation, Optimization models to meet the business objectives for unsecured loan products
Explore and utilize variety of internal and external data (structured/unstructured/real time) to improve model performance
Coordinate with related teams to deploy models in Production with Model implementation process complied
Monitor model performance and propose the recommendations to calibrate or re-develop models to improve their performance
Provide & communicate analytics and model usages to business as well as the in-depth analysis to answer strategic queries
Collaborate and manage vendors to deliver the projects related to customer analytics and models

**Qualifications**

Bachelor’s or master’s degree in a quantitative field (e.g. Business Analytics, Computer Science, Statistics, other related fields)
2-5 years of experience working as a data scientist building models using machine learning
Experience with relevant programming languages: Python, PySpark, SQL
Ability to identify problems, formulate and articulate solutions, and defend assumptions
Logical thinking and a high degree of attention to detail
Ability to work with all levels of staff across all lines of business in the company
Creative, innovative, collaborative, and customer focused attitude
y, engineering or computing related degree. 
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
- "Technical Skills": Key technical skills required for the role can also be tools or programming language
- "Soft Skills": Key soft skills required for the role.
- "Candidate Profile": A summary of the key traits or qualities the company is seeking in a candidate, such as personality traits or professional qualities, make it short and clear within 3 sentences.

Example output:
{
    "Technical Skills": ["Python", "Machine Learning", "Data Analysis", "SQL", "Computer Vision", "NLP", "Hadoop", "Cloud Computing"],
    "Soft Skills": ["Collaboration", "Adaptability", "Communication"],
    "Candidate Profile": "The ideal candidate is a strategic thinker, innovative, data-driven, collaborative, and results-oriented, with excellent communication skills."
}
"""

# Input 2: Mock behavioral interview question
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
        response_questions = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Display behavioral questions in text area
        example_questions = response_questions.choices[0].message.content
        st.markdown("### 🗨️ Mock Behavioral Interview Questions")
        st.text_area(
            "Example behavioral interview questions:",
            value=example_questions,
            height=300,
            disabled=True
        )


