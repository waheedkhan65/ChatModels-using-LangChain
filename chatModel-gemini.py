from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash')

result = model.invoke("hello, what is the capital of pakistan?")

answer = result.content[0]["text"] if isinstance(result.content, list) else result.content

print(answer)