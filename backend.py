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

    COHERE_API_KEY = os.environ.get('cohere_api_key')
    OPENWEATHERMAP_API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")


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

    COHERE_API_KEY = os.environ.get('COHERE_API_KEY')
    SERP_API_KEY = os.environ.get("SERPAPI_API_KEY")

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