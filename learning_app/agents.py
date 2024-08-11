from crewai import Agent
from langchain_groq import ChatGroq
import streamlit as st

# Initialize LLM
GROQ_API_KEY = st.secrets["groq"]["api_key"]

llm = ChatGroq(temperature=0, model_name="llama3-70b-8192", api_key=GROQ_API_KEY)

# Define Agents
intent_extractor_agent = Agent(
    role='Intent Extractor',
    goal='Extract learning intent and knowledge level from user query',
    backstory="You are responsible for understanding and extracting key details from learning-related queries.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

content_generator_agent = Agent(
    role='Content Generator',
    goal='Generate byte-sized learning content based on user intent and knowledge level',
    backstory="You create concise and focused learning materials tailored to the user's current knowledge level and desired learning topic.",
    verbose=True,
    llm=llm,
    allow_delegation=False
)
