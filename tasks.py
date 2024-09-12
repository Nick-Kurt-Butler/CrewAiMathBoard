from textwrap import dedent
from crewai import Task

class Math_Tasks():
  def __init__(self,problem):
     self.problem = problem

  def research_task(self, agent):
    return Task(
      description=dedent(f"""\
        Conduct comprehensive research on the {self.problem}.  You need to research the best description of the
                {self.problem}, find why the problem is unsolved, look for the past and current research on the
                {self.problem}, and know what the future of the problem is.  Review all work with the subject matter expert."""),
      expected_output=dedent(f"""\
        A detailed research report on the {self.problem} that can be used by others to derive what the current state of
                the {self.problem} is."""),
      agent=agent,
      async_execution=True
    )

  def subject_matter_expert_task(self, agent):
    return Task(
			description=dedent(f"""\
                Make any information gathered on the {self.problem} clear, concise, and accurate.  Make sure there
                    are no inconsistencies in the research you come across. Review the work of all other agents rigorously.
				"""),
			expected_output=dedent(f"""\
                Given and input with information on the {self.problem}, a modified output that makes the information on the {self.problem}
                clear, concise, and accurate.  Make sure to review all information of all agents.  Make sure the research, discussion and
                website include correct and informative information.  Also make sure the website includes all information discussed"""),
			async_execution=True,
			agent=agent
		)

  def web_developer_task(self, agent):
    return Task(
			description=dedent(f"""\
                Create a visually complex website that contains all the infomation produced from the other agents in a coherent fashion.
                """),
			expected_output=dedent("""\
				A single html document written to file and a single css document written to file that is called by the html file.
                This website should have tons of html that includes all of the information discussed between the agents.
                """),
			agent=agent
		)

  def independent_math_contributor_task(self, agent):
    return Task(
			description=dedent(f"""\
                help expand the current mathematical and scientific knowledge on the {self.problem}.
                Work with others to bounce ideas on how to solve the {self.problem}. Collaborate with the other agents.
                document your discussion and give to the website creator to include in the discussion board section.
				"""),
			expected_output=dedent("""\
                Dialogue with other independent math contributors.  The dialogue should be reviewed by all other agents and
                include in the website discussion board.
			    """),
			agent=agent
		)
