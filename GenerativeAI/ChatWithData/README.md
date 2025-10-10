# Chat with Your Data 💬

A simple Streamlit application that allows you to store text data in a database and chat with it using a free LLM API (GROQ).

## Features ✨

- 📥 **Store Text Data**: Add and store text entries in a SQLite database
- 💬 **Chat Interface**: Ask questions about your stored data
- 🤖 **Free LLM API**: Uses GROQ's free API with Llama 3 model
- 📊 **Data Statistics**: View how many text entries you have stored
- 🔒 **Secure**: API keys stored in environment variables

## Setup 🚀

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get GROQ API Key

1. Visit [GROQ Console](https://console.groq.com/)
2. Sign up for a free account
3. Generate an API key

### 3. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API key
GROQ_API_KEY=your_actual_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

## Usage 📖

1. **Add Text**: Use the "Add Text" page to store text data
2. **Chat**: Use the "Chat" page to ask questions about your stored data
3. **Navigate**: Use the sidebar to switch between pages

## Project Structure 📁

```
ChatWithData/
├── app.py                 # Main Streamlit application
├── config/
│   └── settings.py        # Configuration and environment variables
├── database/
│   └── db_manager.py      # Database operations
├── pages/
│   ├── AddText.py         # Add text data page
│   └── Chat.py            # Chat interface page
├── services/
│   └── llm_service.py     # GROQ API integration
├── data/                  # SQLite database storage
├── .env.example           # Environment variables template
└── requirements.txt       # Python dependencies
```

## API Information 🔑

- **Provider**: GROQ
- **Model**: Llama 3 8B (llama3-8b-8192)
- **Free Tier**: Yes, with rate limits
- **Documentation**: [GROQ API Docs](https://console.groq.com/docs)

## Troubleshooting 🔧

- **API Key Error**: Make sure your `.env` file contains a valid GROQ API key
- **No Data**: Add some text using the "Add Text" page before chatting
- **Database Issues**: The SQLite database will be created automatically in the `data/` folder
