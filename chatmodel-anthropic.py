
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-sonnet-4-5")

result = model.invoke("hello, what is the capital of pakistan?")

answer = (
    result.content[0]["text"]
    if isinstance(result.content, list)
    else result.content
)

print(answer)
