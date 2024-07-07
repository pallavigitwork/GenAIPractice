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
from PIL import Image

 
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function load gemini model get response

def get_gemini_response(input,image):
    model=genai.GenerativeModel('gemini-pro-vision')
    if input!='':
        response=model.generate_content(input,image)
    else:
        response=model.generate_content(image)
    return response.text

#initialise streamlit app
st.set_page_config(page_title="Question on Image to Gemini By Pallavi")
st.header("Gemini Image Application")
input = ""
#st.text_input("Input: ", key="input")
upload_file=st.file_uploader('Choose image..', type=['jpg','png'])
image=""
if upload_file is not None:
    image =Image.open(upload_file)
    st.image(image, caption="Upload Image..",use_column_width=True)

submit =st.button("Explain the image")

#if submit clicked ask gemini
if submit:
 
  response=get_gemini_response(input,image)
  st.subheader("The Answer is ")
  st.write(response)
