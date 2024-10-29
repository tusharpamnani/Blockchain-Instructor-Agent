import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from crewai_tools import PDFSearchTool
from crewai_tools import TXTSearchTool



serper_api_key = os.getenv('SERPER_API_KEY')
tool = SerperDevTool()


