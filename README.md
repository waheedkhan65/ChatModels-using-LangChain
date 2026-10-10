# Chat Models using LangChain

Small Python examples for calling OpenAI, Gemini, and Anthropic chat models with LangChain.

## Files

- `chatModel-openAi.py` uses `ChatOpenAI`
- `chatModel-gemini.py` uses `ChatGoogleGenerativeAI`
- `chatmodel-anthropic.py` uses `ChatAnthropic`

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the API keys your chosen script needs.

## Environment Variables

- OpenAI: `OPENAI_API_KEY`
- Gemini: `GOOGLE_API_KEY`
- Anthropic: `ANTHROPIC_API_KEY`

## Run

Use the script for the model you want to test:

```bash
python chatModel-openAi.py
python chatModel-gemini.py
python chatmodel-anthropic.py
```

Each script sends a simple prompt and prints the model response.