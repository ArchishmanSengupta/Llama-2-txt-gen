import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import Ctransformers

# Streamlit functions and user interface
st.set_page_config(
  page_title="Topic Expansion",
  page_icon="⚡️",
  layout="centered",
  initial_sidebar_state='collapsed',
)

st.header("Generate Topic Summary")

input_text = st.text_input("Enter the topic")

## create columns for number of words and target audience

col1,col2 = st.columns([5,5])

with col1:
  numberOfWords = st.text_input("Number of words")
with col2:
  targetAudience = st.selectbox("Writing the topic for", ('students', 'professionals', 'researchers'), index = 0)

submit = st.button("Generate")

