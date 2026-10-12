from langchain_huggingface import chatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.B-chat-v1.0",
    task= "text-generation"
)
model = ChatHuggingFace(llm= llm)

result = model.invoke("what is the capital of pakistan?")

print(result.content)
