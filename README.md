# Math Research Collaboration Project

## Overview

This project is designed to facilitate collaborative research on complex mathematical problems using a team of specialized agents. The agents work together to conduct research, verify information, develop a website, and contribute unique insights. The project is structured to handle multiple iterations of tasks to ensure thorough and accurate results.

## Project Structure

### 1. Tasks

The [`tasks.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2FP3120851%2Fmath_board%2Ftasks.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/P3120851/math_board/tasks.py") file defines various tasks that agents need to perform. Each task is associated with a specific role and has a detailed description and expected output.

- **Research Task**: Conduct comprehensive research on the given problem.
- **Subject Matter Expert Task**: Ensure the accuracy and clarity of the research.
- **Web Developer Task**: Create a website to present the research findings.
- **Independent Math Contributor Task**: Contribute unique insights and collaborate with other agents.

### 2. Tools

The [`tools.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2FP3120851%2Fmath_board%2Ftools.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/P3120851/math_board/tools.py") file provides a set of tools that agents can use to perform their tasks. These tools include web search, finding similar webpages, getting webpage contents, and writing code to files.

### 3. Agents

The [`agents.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2FP3120851%2Fmath_board%2Fagents.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/P3120851/math_board/agents.py") file defines different types of agents, each with a specific role and set of tools. The agents include:

- **Research Specialist**
- **Subject Matter Expert**
- **Full Stack Website Developer**
- **Independent Math Contributor**

### 4. Main Script

The [`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2FP3120851%2Fmath_board%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/P3120851/math_board/main.py") file is the entry point of the project. It initializes the agents and tasks, sets up the context for each task, and runs the process for a defined number of iterations.

## How to Run

1. **Install Dependencies**: Ensure you have all necessary dependencies installed. You can use [`pip`](command:_github.copilot.openSymbolFromReferences?%5B%22pip%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2FP3120851%2Fmath_board%2Freadme.md%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2FP3120851%2Fmath_board%2Freadme.md%22%2C%22path%22%3A%22%2FUsers%2FP3120851%2Fmath_board%2Freadme.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A36%2C%22character%22%3A96%7D%7D%5D%5D "Go to definition") to install them.
   ```sh
   pip install -r requirements.txt
   ```

2. **Set Up Environment Variables**: Create a `.env` file with the necessary environment variables, such as [`EXA_API_KEY`](command:_github.copilot.openSymbolFromReferences?%5B%22EXA_API_KEY%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2FP3120851%2Fmath_board%2Freadme.md%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2FP3120851%2Fmath_board%2Freadme.md%22%2C%22path%22%3A%22%2FUsers%2FP3120851%2Fmath_board%2Freadme.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A41%2C%22character%22%3A109%7D%7D%5D%5D "Go to definition").

3. **Run the Main Script**: Execute the main script to start the process.
   ```sh
   python main.py
   ```

## File Descriptions

### Python Files

- **tasks.py**: Defines the tasks for the agents.
- **tools.py**: Provides tools for the agents to use.
- **agents.py**: Defines the agents and their roles.
- **main.py**: Main script to run the project.

### HTML and CSS Files

- **Rieman Hypothesis Output**
   - **GPT-3.5 Turbo**
      - **riemann_index.html**
      - **riemann_styles.css**
      - [`Riemann 3.5 site`](https://html-preview.github.io/?url=https://github.com/Nick-Kurt-Butler/CrewAiMathBoard/blob/main/Riemann/gpt3_5_turbo/index.html")
   - **GPT-4o**
      - **riemann_index.html**
      - **riemann_styles.css**
      - [`Riemann 4o site`](https://html-preview.github.io/?url=https://github.com/Nick-Kurt-Butler/CrewAiMathBoard/blob/main/Riemann/gpt4o/index.html")
- **Collatz Conjecture Output**
   - **GPT-3.5 Turbo**
      - **collatz_index.html**
      - **collatz_styles.css**
      - [`Collatz 3.5 site`](https://html-preview.github.io/?url=https://github.com/Nick-Kurt-Butler/CrewAiMathBoard/blob/main/Collatz/gpt3_5_turbo/index.html")
   - **GPT-4o**
      - **collatz_index.html**
      - **collatz_styles.css**
      - [`Collatz 4o site`](https://html-preview.github.io/?url=https://github.com/Nick-Kurt-Butler/CrewAiMathBoard/blob/main/Collatz/gpt4o/index.html")


## Example Usage

When you run the main script, you will be prompted to enter the mathematical problem you want to research. The agents will then perform their tasks in a sequential process, iterating multiple times to refine the results.

```sh
What is the math problem you would like to research?
Collatz Conjecture
```

## Comparison of Models: Collatz Conjecture vs. Riemann Hypothesis

### Collatz Conjecture

- **Research Depth**: The research on the Collatz Conjecture involved extensive computational verification and exploration of various mathematical approaches, including number theory and dynamical systems.
- **Website Development**: The website for the Collatz Conjecture provided a detailed overview, formal definitions, historical background, current state of the problem, and potential future work. It also included a discussion board for collaborative insights.
- **Agent Collaboration**: The agents effectively collaborated to verify the conjecture for large numbers and explore new mathematical frameworks.

### Riemann Hypothesis

- **Research Depth**: The research on the Riemann Hypothesis was more complex, involving advanced topics in analytic number theory, quantum mechanics, and random matrix theory. The agents conducted thorough research on the current state and historical background of the hypothesis.
- **Website Development**: The website for the Riemann Hypothesis included sections on the overview, historical background, significance, current research, and a discussion board. It provided a comprehensive resource for understanding the hypothesis and its implications.
- **Agent Collaboration**: The agents collaborated to gather detailed information, verify the accuracy of the research, and develop a visually complex website. The collaboration included contributions from independent math contributors and subject matter experts.

### Summary

Both models demonstrated effective collaboration and thorough research. However, the Riemann Hypothesis model required a deeper level of expertise and more complex research due to the nature of the problem. The Collatz Conjecture model focused more on computational verification and exploring new mathematical approaches. Both models successfully developed comprehensive websites to present their findings and facilitate further discussion.

## Performance Comparison: GPT-4 vs. GPT-3.5 Turbo

### GPT-4

- **Research Quality**: The GPT-4 model provided more accurate and in-depth research results. It was able to understand complex mathematical concepts and provide detailed explanations.
- **Collaboration Efficiency**: The agents using GPT-4 collaborated more effectively, resulting in a more cohesive and comprehensive final product.
- **Website Development**: The websites developed with GPT-4 were more detailed and user-friendly, with better-organized content and more interactive features.
- **Task Understanding**: There were times the agent made small errors when trying to run code through the tools, but the GPT-4 model was able to correct itself every time.

### GPT-3.5 Turbo

- **Research Quality**: The GPT-3.5 Turbo model provided good research results but lacked the depth and accuracy of GPT-4. It sometimes struggled with more complex mathematical concepts.
- **Collaboration Efficiency**: The agents using GPT-3.5 Turbo had some difficulties in collaboration, leading to a less cohesive final product.
- **Website Development**: The websites developed with GPT-3.5 Turbo were functional but lacked the polish and interactivity of those developed with GPT-4.
- **Task Understanding**: When the agent made an error trying to run code with the tools in tools.py, it would often get the syntax wrong and never correct itself. The result was the agents often could not use the tools it had access to and the result was a loss in information.

### Summary

The GPT-4 model significantly outperformed the GPT-3.5 Turbo model in terms of research quality, collaboration efficiency, and website development. The improvements in GPT-4 led to more accurate and detailed research, better collaboration among agents, and more user-friendly and interactive websites.
