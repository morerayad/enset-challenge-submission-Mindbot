from crewai import Agent, Task, Crew

def safe_kickoff(crew):
    try:
        return crew.kickoff()
    except Exception as e:
        print("Error:", e)
        return "Mock result: Hello! CrewAI is a framework for managing AI agents."

agent = Agent(
    role="Assistant",
    goal="Answer simple questions",
    backstory="You are a helpful AI assistant"
)

task = Task(
    description="Say hello and explain what CrewAI is in one sentence",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task]
)

result = safe_kickoff(crew)
print(result)