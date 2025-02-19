import streamlit as st

# App title
st.title("🌟 Murad Pitafi Enterprises - Careers Portal")

# Sidebar for navigation
st.sidebar.title("💼 Job Openings")
job_role = st.sidebar.radio("Select a Job Role", ("MLOps Engineer", "Machine Learning Engineer"))

# Job descriptions
jobs = {
    "MLOps Engineer": """  
    **Responsibilities:**  
    ✅ Deploy & monitor ML models in production  
    ✅ Build & optimize CI/CD pipelines for ML workflows  
    ✅ Strong skills in Docker, Kubernetes, & cloud platforms  

    **Requirements:**  
    📌 Bachelor's/Master’s degree in AI, Computer Science, or related field  
    📌 Experience with MLOps tools (Kubeflow, MLflow, Airflow)  
    📌 Proficiency in Python, DevOps, and Cloud Computing  
    """,

    "Machine Learning Engineer": """  
    **Responsibilities:**  
    ✅ Design & develop AI/ML models for real-world applications  
    ✅ Optimize models for accuracy, efficiency & scalability  
    ✅ Proficiency in Python, TensorFlow, & deep learning frameworks  

    **Requirements:**  
    📌 Bachelor's/Master’s degree in AI, Data Science, or related field  
    📌 Strong understanding of ML algorithms & deep learning  
    📌 Experience with cloud computing & distributed ML frameworks  
    """
}

# Display job description
st.subheader(f"📌 {job_role}")
st.markdown(jobs[job_role])

# Resume Upload Section
st.subheader("📤 Apply Now")
st.markdown("Upload your resume to apply for this position.")

# Resume upload
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    st.success("✅ Congratulations! Your application has been submitted successfully.")
    st.balloons()

# Footer
st.markdown("---")
st.markdown("© 2025 Murad Pitafi Enterprises | All Rights Reserved")
