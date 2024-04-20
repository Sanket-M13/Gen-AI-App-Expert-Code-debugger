from openai import OpenAI
import google.generativeai as genai

import streamlit as st


f = open("open-ai-key.txt")
key = f.read()
genai.configure(api_key=key)

model=genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction="You are a Developer who has 30+ years of experince in MAANG+ companies who expertise in forntend & backend your role is to debug the code and give the optimised coding output ")

st.header("GenAI App : Expert Code Debugger🧑‍💻")

st.text("Who helps you with your code journey")

st.subheader("Enter Your Codes and Fix the Bugs🥳")



prompt = st.text_area("Enter your Code here :")


if st.button("DEBUG🐞") == True:
    

    response = model.generate_content(prompt)

    st.header("Review of Your Code🧐")

    st.write(response.text)
    