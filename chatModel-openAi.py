
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")

result = model.invoke("hello, what is the capital of pakistan?")

answer = (
    result.content[0]["text"]
    if isinstance(result.content, list)
    else result.content
)

print(answer)
