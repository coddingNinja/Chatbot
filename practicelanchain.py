from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
os.system("clear")
import streamlit as st
st.title("English Language Expert (AI Assistent) ")
st.markdown("Improve your grammer and vocablery and english communication skills")
api_key=os.getenv("api_key")
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.7, google_api_key=api_key)
memory=ConversationBufferMemory()
promt=PromptTemplate(
   input_variables=["history","input"],
   template='''
    You are a english teacher expert and helps students to learn or improve there english and grammer keep you response short and 
    Always:
    - Be friendly and supportive.
- Correct mistakes gently.
- Give examples when possible.
- Explain difficult words simply.

Conversation history:
{history}

Student: {input}
English Teacher AI: 

'''
)
if "messages" not in st.session_state :
    st.session_state.messages=[]

if "conversation" not in st.session_state:
    st.session_state.conversation=ConversationChain(
    llm=llm,
    memory=memory,
    prompt=promt,
    verbose=True
    )
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
user_input=st.chat_input("Ask me anything")
# print(os.getenv("api_key"))
if user_input :
    st.session_state.messages.append({"role":"user","content":user_input})   
    with st.chat_message("user"):
         st.markdown(user_input)
    reponse=st.session_state.conversation.invoke(user_input)
    st.session_state.messages.append({"role":"Assitant","content":reponse.get('response', '').strip()})
    with st.chat_message("Assistant"):
        st.markdown(reponse.get('response', '').strip())    
    




 