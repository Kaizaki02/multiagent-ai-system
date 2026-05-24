from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search, scrape_url
from dotenv import load_dotenv
import os

load_dotenv()

#model initialization
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, api_key=os.getenv("GEMINI_API_KEY"))  


#agent initialization

#1st agent - search agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
    )

#2nd agent - reader agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
    )


writing_prompt = ChatPromptTemplate.from_messages([
    ("system", "you are an expert research writer.write clear,structured and concise research reports based on the information provided by the search and reader agents."),
    ("human","""Write a detailed research report on the topic below.
      Topic:{topic}
     Reseach Gathered:{research}

     structure the report as:
     - Introduction
     - Key Findings (minimum 3 well explained points)
     - Conclusion
    - References (list all the URLs used for research)    
     
Be detailed, factual and professional."""),

])

parser = StrOutputParser()

writer_chain = writing_prompt | llm | parser


critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a sharp and constructive research critic agent.Be honest and specific."),
    ("human","""review the research report below and evalute it strictly.
     
     report: {report}

     responf in this exact format:

     score: X/10 

     Strengths:
     
     - ...
     - ...
     
     areas to improve
     - ...
     - ...
     
     one line verdict:
     ...
     """),
])

critic_chain = critic_prompt | llm | parser