from fastapi import FastAPI
import uvicorn
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
#Initialize model
model = ChatGroq(model = "Gemma2-9b-It" , groq_api_key=groq_api_key)

#Create prompt template
system_template = "Who is the equivalent cricket player to {player} in today's era?"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}"),
    ]
)

#Create output parser
parser = StrOutputParser()

##create chain
chain = prompt_template | model | parser

#App definition
app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A server for Langchain applications using Groq.",
)

add_routes(
    app,
    chain,
    path='/chain'
)

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port = 8000)