# Chat with Your Data

## Overview
This project is a Streamlit application that allows users to interact with their data through a chat interface. Users can add text data, browse documents, and engage in a chat with the uploaded data.

## Project Structure
```
chat-with-data
├── app.py               # Main entry point of the Streamlit application
├── pages
│   ├── AddText.py      # Implementation for the "Add Text" page
│   ├── Browse.py       # Implementation for the "Browse Documents" page
│   └── Chat.py         # Implementation for the "Chat" page
├── requirements.txt     # Lists dependencies for the project
├── .gitignore           # Specifies files to be ignored by Git
└── README.md            # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd chat-with-data
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
To run the Streamlit application, use the following command:
```
streamlit run app.py
```

## Usage
- **Add Text**: Navigate to this page to input and add text data.
- **Browse Documents**: Use this page to browse and select documents for interaction.
- **Chat**: Engage with the data through a chat interface.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.