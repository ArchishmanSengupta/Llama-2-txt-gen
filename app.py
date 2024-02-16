import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def buildLlamaResponse(input_text,numberOfWords,targetAudience):
  
  ## Call Llama 2 model from local system
  llm = CTransformers(model = 'models/llama-2-7b-chat.ggmlv3.q8_0.bin', model_type='llama', config={
    'max_new_tokens':256,
    'temperature': 0.01,
  })
  
  ## Prompt Template
  template = """
  Write a detailed explaination for {targetAudience} on the topic of {input_text} within the word range of {numberOfWords}
  """
  
  prompt = PromptTemplate(input_variables=["target_audience","input_text","number_of_words"], template=template)
  
  
  ## Generate Response from the Llama 2 Model
  response = llm(prompt.format(targetAudience=targetAudience, input_text=input_text, numberOfWords=numberOfWords))
  
  print(response)
  return response
  
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

## Final output
if submit:
  st.write(buildLlamaResponse(input_text,numberOfWords,targetAudience))
