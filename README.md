# Gemini assistant

This project runs a LangChain assistant with Google's Gemini API through Google
AI Studio.

## Setup

1. Create an API key in Google AI Studio.
2. Set it as `GOOGLE_API_KEY` in your environment or in a `.env` file in the
   project directory:

   ```env
   GOOGLE_API_KEY=your_google_ai_studio_api_key
   ```

3. Install the project dependencies and run the assistant:

   ```powershell
   uv sync
   uv run python main.py
   ```