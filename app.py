from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

os.environ["GROQ_API_KEY"] = "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"

model = ChatGroq(model="llama3-8b-8192")

app = FastAPI()

# Mount the static directory to serve the HTML, CSS, and JS files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define the request body
class MessageRequest(BaseModel):
    content: str

# Define the response model
class MessageResponse(BaseModel):
    response: str

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Medical assistant. Answer all questions related to medical queries."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Create the prompt chain
chain = prompt | model

@app.post("/chat", response_model=MessageResponse)
async def chat(request: MessageRequest):
    human_message = HumanMessage(content=request.content)
    response = chain.invoke({"messages": [human_message]})
    return MessageResponse(response=response.content)

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Example usage
# response = chain.invoke({"messages": [HumanMessage(content="hi! I'm feeling sick")]})
# print(response.content)
