# 📚 Personalized Learning App

Welcome to the **Personalized Learning App**! This Streamlit application is designed to help you learn new topics at your own pace by generating customized learning content based on your input. 🚀

## 🎯 Key Features

- **Intent Extraction**: Understands your learning goals and current knowledge level.
- **Content Generation**: Produces byte-sized, flashcard-style learning content tailored to your needs.
- **Interactive Flashcards**: Navigate through the generated flashcards to absorb the knowledge at your own pace.

## 🛠️ How It Works

1. **Input Your Learning Query**: Describe what you want to learn and your current knowledge level.
2. **Run the First Crew**: The app will extract your intent and generate personalized learning content.
3. **Explore Flashcards**: Review the generated flashcards and navigate through them using the provided buttons.

## 📂 Code Structure

### `main.py`

- **User Input**: Captures the learning query from the user.
- **First Crew Execution**: Runs the intent extraction and content generation tasks using the `Crew` object.
- **Flashcard Display**: Shows the generated flashcards to the user, with navigation options.

### `agents.py`

- **Intent Extractor Agent**: Responsible for understanding and extracting key details from your query.
- **Content Generator Agent**: Generates concise and focused learning content based on your learning intent.

### `tasks.py`

- **Intent Extraction Task**: Extracts the learning intent and knowledge level from your query.
- **Content Generation Task**: Generates flashcards in a JSON format, with each flashcard containing a title and content in markdown.

## 🚀 Getting Started

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/personalized-learning-app.git
   cd personalized-learning-app

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

3. **Run the App**
   ```bash
   streamlit run main.py

add your Groq API to .stremlit/secrets.toml file in the following format
    ```
    [groq]
    api_key = 'api_key'
