from langchain_cohere import ChatCohere, create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor
from langchain_core.messages import HumanMessage
from langchain.schema import HumanMessage, AIMessage, ChatMessage, FunctionMessage

from typing import Optional, Type
import json

from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool
from langchain.tools import BaseTool, format_tool_to_openai_function
from pydantic import BaseModel, Field
import os
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_community.utilities import SerpAPIWrapper


def check_weather(query: str):

    #api_cohere_key = 'BQtxZX9TZtECoTzDFkUZCwU4wu5WozhvrPtaBaxM'
    #api_weather = "6a06eace0b866351ea8fdd0401993aae"

    os.environ['COHERE_API_KEY'] = 'PKYJ9mWpadwNW8Oj44ftpOr6rKzBkzW6eT2iZhaC'
    os.environ["OPENWEATHERMAP_API_KEY"] = "6a06eace0b866351ea8fdd0401993aae"


    llm = ChatCohere(model = 'command-r-plus' , temperature=0)
    tools = load_tools(['openweathermap-api'], llm)
    agent_chain = initialize_agent(
        tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent_chain.run(
        query
    )

    return result


def search_query(query : str):

    os.environ['COHERE_API_KEY'] = 'BQtxZX9TZtECoTzDFkUZCwU4wu5WozhvrPtaBaxM'
    os.environ['SERPAPI_API_KEY'] = 'df69a05dca9849165cb10df886f7a238d110ae22c97d2fb582390e78e2b57f1f'

    custom_prompt = (
    "You are a knowledgeable assistant. When asked about any topic, provide a detailed and comprehensive response. "
    "Include background information, key points, significant achievements, relevant current events, and any controversies. "
    "Ensure your answer is well-rounded and informative."
    )

    llm = ChatCohere(model = 'command-r-plus' , temperature=0)
    tools = load_tools(["serpapi"] , llm)

    agent_chain = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION ,
    verbose=True,
    prompt=custom_prompt
    )
    
    result = agent_chain.run(
        query
    )

    return result