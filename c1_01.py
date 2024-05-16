import openai
import streamlit as st

# Function to interact with GPT-3.5 chatbot
def chat_with_gpt(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Streamlit app
def main():
    st.title("GPT-3.5 Chatbot")

    # Create a sidebar section for API key input
    st.sidebar.subheader("OpenAI API Key")
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

    # Main chatbot interface
    with st.form("user_input_form"):
        user_input = st.text_input("You:")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if user_input.lower() in ["quit", "exit", "bye"]:
            st.write("Goodbye!")
        else:
            if api_key:
                response = chat_with_gpt(user_input, api_key)
                st.write("Chatbot:", response)
            else:
                st.write("Please enter your OpenAI API Key.")

if __name__ == "__main__":
    main()
