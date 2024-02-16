import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def generate_topic_summary(input_topic, word_limit, audience):
  
    # Initialize LLama 2 model
    llama_model = CTransformers(
        model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={'max_new_tokens': 256, 'temperature': 0.01}
    )
  
    # Define prompt template
    template = """
    Write a detailed explanation for {audience} on the topic of {input_topic} within {word_limit} words.
    """
  
    prompt = PromptTemplate(
        input_variables=["audience", "input_topic", "word_limit"],
        template=template
    )
  
    # Generate response from the LLama 2 Model
    response = llama_model(prompt.format(audience=audience, input_topic=input_topic, word_limit=word_limit))
  
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

input_topic = st.text_input("Enter the topic")

# Create columns for number of words and target audience
column1, column2 = st.columns([5, 5])

with column1:
    word_limit = st.text_input("Number of words")

with column2:
    audience = st.selectbox("Writing the topic for", ('students', 'professionals', 'researchers'), index=0)

submit = st.button("Generate")

# Final output
if submit:
    st.write(generate_topic_summary(input_topic, word_limit, audience))
