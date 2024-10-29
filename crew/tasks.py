from crewai import Task
from agents import blockchain_instructor
from tools import tool

# Blockchain Education Task - Guiding Students in Blockchain Fundamentals
blockchain_instructor_task = Task(
    description=(
        '''
        As a blockchain instructor, your task is to guide students with a basic understanding of JavaScript and blockchain 
        through foundational blockchain concepts. Focus on providing explanations of key topics such as smart contracts, dApp 
        development, consensus mechanisms, and blockchain security. Your guidance should be clear and practical, aiming to 
        increase the student's confidence in these areas.

        You are expected to provide examples in JavaScript where applicable, such as basic smart contract snippets or dApp 
        templates. Additionally, offer project ideas or exercises that allow students to apply their learning and recommend 
        online resources or communities to further support their journey.
        '''
    ),
    expected_output=(
        '''
        1. A structured learning path covering key blockchain topics, including smart contracts, dApps, and consensus mechanisms.
        2. JavaScript-based examples or code snippets to demonstrate blockchain concepts.
        3. Practical exercises or mini-project ideas for students to implement.
        4. Suggested resources and communities for continued learning and support.
        '''
    ),
    tools=[tool],  
    agent=blockchain_instructor,
    output_file='blockchain_education_output.md'
)
