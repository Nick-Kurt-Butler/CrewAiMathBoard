from textwrap import dedent
from crewai import Agent
from tools import ToolBox

class Math_Agents():
    def __init__(self,problem):
        self.problem = problem

    def research_agent(self):
      return Agent(
        role="Research Specialist",
        goal=f'Conduct thorough research on the current state of the {self.problem}',
        tools=ToolBox.web_tools(),
        backstory=dedent(f"""\
          As a Research Specialist, your job is to find detailed information
					about the {self.problem}.  You should find the definition, relevent progress,
					current research, and potential future work happening on the {self.problem}.
                    All research should be relevant to someone trying to both learn about the {self.problem}
                    and make progress on the {self.problem} themselves."""),
        verbose=True
      )

    def subject_matter_expert_agent(self):
      return Agent(
        role='Subject Matter Expert',
        goal=f"""Check for logical incongruities of gathered research on the {self.problem} and make it clear, concise and accurate. Rigorously Review
                The accuracy and content of the others research and contributions.  Do research yourself to make sure the other's information is correct.
                All agents need to look to you for advice and guidance.  Make sure the webite include literally all the information discussed and researched
                by the other agents.
                """,
        tools=ToolBox.web_tools(),
        backstory=dedent(f"""\
            You are the world's leading expert on the {self.problem}.
                    You know all the failures and successes of the research on the {self.problem}.
                    As the expert on this subject you are being employed to make sure any on the information
                    gathered from research or on the website is coherent and accurate.
            ."""),
        verbose=True
      )

    def web_developer_agent(self):
      return Agent(
        role='Full Stack Website Developer',
        goal=f"""Develop a fancy website using html, css, and pictures from the web embedded into the html.
                Included in the website should be an overview of the {self.problem}, a detailed account of the {self.problem} describing the current
                state of the problem, and message bored at the bottom from the individual math contributors.  This website should contain a
                substantial amount of information on the {self.problem}.
               """,
        tools=ToolBox.write_tools(),
        backstory=dedent("""\
            You are an expert full stack html coder.
            You are know for making unique and user friendly websites."""),
        verbose=True
      )

    def independent_math_contributor_agent(self):
      return Agent(
        role='Independent Math Contributor',
        goal=f'Contribute relevant and unique thoughts that will help in solving the {self.problem}',
        backstory=dedent(f"""\
            Assume that you are visiting a website which allows to you collaborate with others on the {self.problem}.
            Ask questions or suggest ideas for solving the {self.problem} problem.  Do not say generic things, rather
            strive to come up with unique and relevant ideas to solve the {self.problem}."""),
        verbose=True
      )
