# Blockchain Instructor Agent

This repository provides an agent-based solution for guiding college students with basic JavaScript and blockchain knowledge on their journey to becoming proficient in blockchain development. Using `CrewAI`, the system includes multiple agents such as a food researcher and writer, alongside a dedicated blockchain instructor agent. The blockchain instructor focuses on creating a structured learning path, offering practical exercises, code examples, and curated resources for students.

## Repository Structure

- **`crew/`** - Contains all the scripts related to `CrewAI` configuration, agent setup, and tasks.
- **`crew.py`** - The main script to launch the agent-based task flow.

## Features

1. **Blockchain Instructor Agent** - Provides guidance on blockchain fundamentals, smart contracts, and dApp development with JavaScript examples.
2. **Food Researcher & Writer Agents** - Also included as examples, these agents demonstrate how to gather and write content for culinary topics.
3. **Modular Task and Agent Setup** - Easily customizable tasks for different use cases.

## Setup

### Prerequisites

- Python 3.x
- Required Python packages (as listed in `requirements.txt`)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/tusharpamnani/Blockchain-Instructor-Agent.git
    cd Blockchain-Instructor-Agent
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for API keys and other configurations as needed.

### Usage

To start the `CrewAI` system with the blockchain instructor agent:

1. Navigate to the `Blockchain-Instructor-Agent/crew` directory:
    ```bash
    cd crew
    ```

2. Run the main script:
    ```bash
    python crew.py
    ```

This will initiate the `CrewAI` task flow with the specified agents and tasks, including the `blockchain_instructor_task`.

## Agent and Task Overview

### Blockchain Instructor Agent

The **Blockchain Instructor Agent** helps guide students through foundational blockchain concepts, focusing on practical JavaScript-based examples for learning smart contracts, dApps, and blockchain basics.

- **Task Description**: Provides a step-by-step learning path for blockchain, with code examples and project recommendations.
- **Expected Output**: Structured content for students to get started with blockchain development, including exercises, projects, and recommended resources.

### Food Researcher and Writer Agents

Example agents to demonstrate `CrewAI` functionalities, focusing on researching and writing content for culinary topics.

## Contributing

Contributions to improve the blockchain instructor agent or add new features are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.

