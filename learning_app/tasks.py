from crewai import Task
from agents import intent_extractor_agent, content_generator_agent

# Define Tasks
intent_extraction_task = Task(
    description='Extract learning intent and knowledge level from user query {user_query}',
    agent=intent_extractor_agent,
    expected_output=""" map the details in the following example format:
        'learning_topic': '<topic user wants to learn>',
        'knowledge_level': '<user's current knowledge level>',
        'additional_context': '<any additional context provided by the user>'
    """
)

content_generation_task =Task(
        description='Generate byte-sized learning content in a flashcard format based on the extracted intent',
        agent=content_generator_agent,
        expected_output="""
        Return the content as multiple flashcards in JSON format. 
        Each flashcard should contain a title and content field in markdown format with relevant emojis. 
        if there are multiple points use bullet markdown in the content
        """
    )
