import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
llm = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def style_transfer(target_style, original_text):
    # Check if inputs are empty
    if not target_style or not original_text:
        return "Target style or original text is empty. Please provide both."

    # Define the prompt
    prompt = f"Translate the following text: '{original_text}' into the style of this text: '{target_style}'.Make sure to retain the meaning of the text."

    response = llm.chat.completions.create(
        model="local-model", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to do literary style transfer."},
            {"role": "user", "content": prompt},
        ],
    )

    # Extract the stylized text from the response
    stylized_text = response.choices[0].message.content


    return stylized_text

def main():
    st.title("Literary Style Transfer")
    target_style = st.text_input("Enter a text sample in your target style:")
    original_text = st.text_input("Enter the text to be stylized:")
    if st.button("Transfer Style"):
        stylized_text = style_transfer(target_style, original_text)
            #st.write(stylized_text)
        st.code(stylized_text, language='text'
        )
# def main():
#     st.title("Literary Style Transfer")

#     with st.container():  # Create a container for better layout
#         st.markdown("## Input")  # Add a heading for clarity

#         target_style = st.text_input("Enter a text sample in your target style:")
#         original_text = st.text_input("Enter the text to be stylized:")

#         if st.button("Transfer Style"):
#             stylized_text = style_transfer(target_style, original_text)

#             with st.container():  # Create a container for the output
#                 st.markdown("## Stylized Text")  # Add a heading for the output

#                 # Display the stylized text in a wide box with copying enabled
#                 st.code(stylized_text, language="", width=800, copy=True)

if __name__=="__main__":
    main()
