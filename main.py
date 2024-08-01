from dotenv import load_dotenv
import streamlit as st
load_dotenv()
from langchain_openai import OpenAI

llm = OpenAI()

st.title("This is a title")

content = st.text_input("시의 주제를 넣어라")
if st.button("write poet"):
    with st.spinner('Wait for it...'):
        result = llm.invoke(content + "에 대한 시를 작성해줘")
        st.write(result)

# result = llm.invoke("write me a poet about" + content)
# print(result)




#st.title('_Streamlit_ is :blue[cool] :sunglasses')

#title = st.text_input("enter the topic of poet")
#st.write("The topic of poet is", title)

# pip install langchain_community
# pip install langchain
# pip install openai
# pip install python-dotenv
# pip install -U langchain-openai
# pip install streamlit 