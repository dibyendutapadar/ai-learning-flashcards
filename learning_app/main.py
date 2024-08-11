import streamlit as st
from crewai import Crew

from tasks import intent_extraction_task, content_generation_task

from agents import intent_extractor_agent, content_generator_agent
import json
from streamlit_carousel import carousel
# from db_setup import Session, User, Query, Response
# from utils import parse_user_input

# # Create a new session for DB interaction
# session = Session()

if 'first_result' not in st.session_state:
    st.session_state.first_result = ""

st.write("Personalized Learning App")

st.session_state.user_query = st.text_area("Describe what you want to learn and your current knowledge level:", key='learning_query_input')

if st.button('Submit', key='submit_query'):
    if st.session_state.user_query:
        st.write("Running first crew to extract intent and generate learning content...")
        
        # First Crew for extracting intent and generating content
        first_crew = Crew(
            agents=[intent_extractor_agent, content_generator_agent],
            tasks=[intent_extraction_task, content_generation_task],
            verbose=True
        )
        
        user_search_query = {'user_query': st.session_state.user_query}
        first_result = first_crew.kickoff(inputs=user_search_query)
        st.session_state.first_result = first_result
        # print("#######first_result#######")
        # print(st.session_state.first_result )
    else:
        st.write("Please enter a learning query.")



# Display the first result if available
if st.session_state.first_result:
    try:
        # Convert first_result to string and remove the surrounding triple backticks
        result_str = str(st.session_state.first_result)
        result_str = result_str.strip('`')

        # Parse the JSON string into a list of flashcards
        flashcards = json.loads(result_str)

        if 'current_index' not in st.session_state:
            st.session_state.current_index = 0

        # Display the current flashcard in a styled container
        flashcard = flashcards[st.session_state.current_index]

        st.header(flashcard['title'])
        st.markdown(flashcard['content'])

        # Navigation buttons
        col1, col2 = st.columns([.7, .3])
        if col1.button("Previous"):
            if st.session_state.current_index > 0:
                st.session_state.current_index -= 1
        if col2.button("Next"):
            if st.session_state.current_index < len(flashcards) - 1:
                st.session_state.current_index += 1

    except Exception as e:
        st.write(f"An error occurred: {e}")
    st.write("---")
