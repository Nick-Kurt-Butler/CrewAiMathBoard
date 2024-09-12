from dotenv import load_dotenv
from crewai import Crew,Process
from tasks import Math_Tasks
from agents import Math_Agents

def main():
    load_dotenv()

    math_problem = input("What is the math problem you would like to research?\n")

    tasks = Math_Tasks(math_problem)
    agents = Math_Agents(math_problem)

    # create agents
    research_agent = agents.research_agent()
    subject_matter_expert_agent = agents.subject_matter_expert_agent()
    web_developer_agent = agents.web_developer_agent()
    independent_math_contributor_agent1 = agents.independent_math_contributor_agent()
    independent_math_contributor_agent2 = agents.independent_math_contributor_agent()

    # create tasks
    research_task = tasks.research_task(research_agent)
    subject_matter_expert_task = tasks.subject_matter_expert_task(subject_matter_expert_agent)
    web_developer_task = tasks.web_developer_task(web_developer_agent)
    independent_math_contributor_task1 = tasks.independent_math_contributor_task(independent_math_contributor_agent1)
    independent_math_contributor_task2 = tasks.independent_math_contributor_task(independent_math_contributor_agent2)

    # context
    subject_matter_expert_task.context = [research_task]
    independent_math_contributor_task1.context = [research_task,subject_matter_expert_task]
    independent_math_contributor_task2.context = [research_task,subject_matter_expert_task]
    web_developer_task.context = [research_task,subject_matter_expert_task,independent_math_contributor_task1,independent_math_contributor_task2]

    multi_round_process = Process.sequential
    multi_round_process.iterations = 10  # Define the number of iterations

    crew = Crew(
      agents=[
        research_agent,
        subject_matter_expert_agent,
        web_developer_agent,
        independent_math_contributor_agent1,
        independent_math_contributor_agent2
      ],
      tasks=[
        research_task,
        subject_matter_expert_task,
        independent_math_contributor_task1,
        independent_math_contributor_task2,
        web_developer_task
      ],
      process=multi_round_process
    )

    result = crew.kickoff()

    print(result)

if __name__ == "__main__":
    main()
