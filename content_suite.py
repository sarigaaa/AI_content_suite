import streamlit as st
import os
from groq import Groq

# 1. Configuration
# Retrieves the key you set in your terminal (export GROQ_API_KEY='...')
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_marketing_content(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert marketing assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def main():
    st.set_page_config(page_title="AI Content Suite", page_icon="✨")
    st.sidebar.title("✨ AI Content Suite")
    
    # Tool Selection
    tool = st.sidebar.selectbox("Choose a tool", 
        ["🏠 Home", "📢 Ad Generator", "📧 Email Subjects", "✍️ Blog Intro", "📦 Product Description"]
    )

    # 2. Logic encapsulated within each tool block
    if tool == "🏠 Home":
        st.title("✨ AI Content Suite")
        st.markdown("Welcome! Select a tool from the sidebar to start generating.")

    elif tool == "📢 Ad Generator":
        st.header("📢 Ad Generator")
        with st.form("ad_form"):
            product = st.text_input("Product Name")
            audience = st.text_input("Target Audience")
            platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Facebook"])
            submitted = st.form_submit_button("Generate Ad")
            
        if submitted:
            prompt = f"Write a {platform} ad for {product} targeting {audience}."
            with st.spinner("Crafting..."):
                result = generate_marketing_content(prompt)
                st.write(result)
                st.download_button("📥 Download", result, "ad.txt")

    elif tool == "📧 Email Subjects":
        st.header("📧 Email Subject Lines")
        with st.form("email_form"):
            topic = st.text_input("Email topic")
            submitted = st.form_submit_button("Generate")
            
        if submitted:
            prompt = f"Write 10 compelling email subject lines about: {topic}."
            with st.spinner("Generating..."):
                result = generate_marketing_content(prompt)
                st.write(result)
                st.download_button("📥 Download", result, "subjects.txt")

    elif tool == "✍️ Blog Intro":
        st.header("✍️ Blog Intro Writer")
        with st.form("blog_form"):
            topic = st.text_input("Blog topic")
            submitted = st.form_submit_button("Generate")
            
        if submitted:
            prompt = f"Write a 3-paragraph blog intro about: {topic}."
            with st.spinner("Writing..."):
                result = generate_marketing_content(prompt)
                st.write(result)
                st.download_button("📥 Download", result, "intro.txt")

    elif tool == "📦 Product Description":
        st.header("📦 Product Description")
        with st.form("product_form"):
            name = st.text_input("Product name")
            submitted = st.form_submit_button("Generate")
            
        if submitted:
            prompt = f"Write an SEO-friendly product description for: {name}."
            with st.spinner("Writing..."):
                result = generate_marketing_content(prompt)
                st.write(result)
                st.download_button("📥 Download", result, "desc.txt")

if __name__ == "__main__":
    main()