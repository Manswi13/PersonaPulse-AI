# 🎭 PersonaPulse-AI

### AI-Powered Personality-Based Chatbot

PersonaPulse-AI is an interactive AI chatbot that allows users to communicate with different AI personalities.

Built using **Python, Streamlit, LangChain, and Mistral AI**, the application dynamically adjusts its response style based on the personality selected by the user.

## 🚀 Features

- 🎭 **Multiple AI Personalities:** Choose between Angry, Funny, and Sad modes.
- 💬 **Interactive Chat Interface:** Communicate with the AI through a Streamlit-based interface.
- 🧠 **Context-Aware Conversations:** Maintains conversation history during the active session.
- 🔄 **Dynamic Personality Switching:** Automatically resets conversation history when switching personalities.
- 🗑️ **Clear Chat:** Allows users to reset their conversations.
- 🤖 **Mistral AI Integration:** Generates responses using a Mistral language model.

## 🛠️ Technologies Used

- **Python** — Application development
- **Streamlit** — Interactive user interface
- **LangChain** — LLM integration and conversation management
- **Mistral AI** — AI-powered response generation
- **Python-dotenv** — Environment variable management

## 📂 Project Structure

```text
PersonaPulse-AI/
├── UIchatbot.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Manswi13/PersonaPulse-AI.git
```

### 2. Navigate to the Project

```bash
cd PersonaPulse-AI
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project directory and add:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

### 5. Run the Application

```bash
streamlit run UIchatbot.py
```

## 🎯 How It Works

1. The user selects an AI personality from the sidebar.
2. The application creates a system message defining the selected personality.
3. The user enters a message through the chat interface.
4. LangChain sends the conversation to the Mistral AI model.
5. The AI generates a response based on the selected personality and conversation history.
6. Streamlit displays the response in the chat interface.

## 🔮 Future Enhancements

- Additional AI personalities
- Custom personality creation
- Persistent conversation history
- Voice-based interaction
- Improved user interface and personalization

## 👩‍💻 Project Purpose

PersonaPulse-AI demonstrates the integration of large language models with interactive web applications.

The project explores prompt engineering, LLM integration, conversational AI, and session-based chat management.