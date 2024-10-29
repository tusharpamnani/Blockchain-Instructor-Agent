from crewai import Crew, Process
from tasks import  blockchain_instructor_task
from agents import blockchain_instructor
from tools import tool

# Create a crew with the blockchain instructor agent
crew = Crew(
    agents=[blockchain_instructor],
    tasks=[blockchain_instructor_task],
    process=Process.sequential,
)

# Kick off the crew with an input topic for the blockchain instructor
result = crew.kickoff(inputs={'topic': 'getting started with smart contracts using JavaScript and blockchain basics'})
print(result)
