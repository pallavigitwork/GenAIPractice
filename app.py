## Q&A Chatbot
 
 
from dotenv import load_dotenv
# take enviroment variables from .env
load_dotenv()
 
import streamlit as st
import os
import pathlib
import textwrap
 
# Importing Google GenAi
import google.generativeai as genai
 
from IPython.display import display
from IPython.display import Markdown
 
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
 
## Function to laod OPenAI model and get response
 
def get_gemini_response(question):
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(question)
  return response.text
 
## Initialize our streamlit app
 
st.set_page_config(page_title="Ask Question to Gemini By Pallavi")
 
st.header("Gemini Application")
 
input = st.text_input("Input: ", key="input")
 
 
submit = st.button("Have Questions? Ask away..")
 
# If ask button is clicked
 
if submit:
 
  response=get_gemini_response(input)
  st.subheader("The Response is ")
  st.write(response)
 