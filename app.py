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

