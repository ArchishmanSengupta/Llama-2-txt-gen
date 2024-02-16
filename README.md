## App Overview
The `Llama2 txt-gen app` is designed to generate topic summaries based on user-provided inputs. Here's a breakdown of how the app functions:

1. **User Inputs:**
   - **Topic Name:** Users input the name of the topic they want summarized.
   - **Word Limit:** Users specify the maximum word count for the summary.
   - **Target Audience:** Users select the intended audience for the summary from options like students, professionals, or researchers.

2. **LLama-2-7B-Chat-GGML Integration:**
   - The provided inputs are sent as a prompt to the `Llama-2-7B-Chat-GGML` model.
   - The model generates a response based on the prompt and the provided inputs.

3. **Display of Generated Summary:**
   - The generated summary response is displayed within the app for the user to review.

![App Screenshot](https://github.com/ArchishmanSengupta/Llama-2-txt-gen/assets/71402528/6b9aec1d-8ef3-4f98-ba84-db8d5e6b32e6)

### Prompt Template
The app utilizes a prompt template to structure the input provided to the LLama-2 model. The template is as follows:

```
"""
Write a detailed explanation for {audience} on the topic of {input_topic} within {word_limit} words.
"""
```

Users can customize the prompt template according to their preferences, ensuring the generated summary meets their specific requirements.

## Pre-Requisites
1. Before running the application, make sure you have installed the following Python packages:
- `sentence-transformers`
- `ctransformers`
- `langchain`
- `streamlit`

2. You can install these packages using pip:
```
pip install sentence-transformers ctransformers langchain streamlit
```

3. Download the Llama-2-7B-Chat-GGML LLM from HuggingFace [here](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

## Sample Response from Input Parameters
- **Input Text:** "investing and trading for beginners"
- **Number of Words:** 60
- **Target Audience:** "students"

LLM Response:
```
Investing and trading are ways to grow your money by buying and selling assets, such as stocks or real estate. It's important to understand the risks and rewards before getting started. Research and learn about different investment options, set clear goals, and start small to minimize risk. As you gain experience and confidence, you can gradually increase your investments and expand into new areas. Remember, investing and trading are long-term strategies that require patience and discipline.
```
### Generated Response on Streamlit:
![Sample Response Screenshot](https://github.com/ArchishmanSengupta/Llama-2-txt-gen/assets/71402528/b7a848df-1b79-46bb-b88b-d93ac6f02fdf)
