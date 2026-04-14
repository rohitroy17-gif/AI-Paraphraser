import streamlit as st
import google.generativeai as genai
#import os
#from dotenv import load_dotenv
import google.api_core.exceptions

#GEMINI_API_KEY="AIzaSyDkdWrdWK0xq5YvnVSN0PBRi_S2C-fKZHI"
# Load API key
#load_dotenv()
#api_key = os.getenv("GEMINI_API_KEY")
api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

# Model
model = genai.GenerativeModel("gemini-3-flash-preview")

st.title("AI Paraphraser")

text = st.text_area("Enter your text")

if st.button("Paraphrase"):
    if text:

        prompt = "Paraphrase this:\n" + text

        try:
            response = model.generate_content(prompt)
            st.success(response.text)

        except google.api_core.exceptions.ResourceExhausted:
            st.error("Too many requests! Try again later.")

        except Exception as e:
            st.error(e)

    else:
        st.warning("Please enter text")
