from crewai import Crew, Task, Agent

def safe_kickoff(crew):
    try:
        return crew.kickoff()
    except Exception as e:
        print("[Warning] Skipping execution due to:", e)
        return {
            "analysis": "Mock analysis: unable to run real AI.",
            "solution": "Mock solution: check your setup or API."
            }
def run_agents(user_input):
    # Agent 1: pour l'analyse de prb
    analysis_agent = Agent(
        name="AnalysisAgent",
        role="Problem Analyzer",
        goal="Analyze the user's problem clearly",
        backstory="Expert in understanding student problems and identifying weaknesses."
    )

    # Agent 2: solution de prb
    solution_agent = Agent(
        name="SolutionAgent",
        role="Solution Generator",
        goal="Provide a clear and useful solution",
        backstory="Expert in giving practical solutions and study plans."
    )

    # Task 1:analyse
    task1 = Task(
        name="AnalysisTask",
        description=f"Analyze this problem: {user_input}",
        expected_output="Clear analysis of the problem"
    )

    # Task 2:solution
    task2 = Task(
        name="SolutionTask",
        description=f"Based on the analysis, give a solution for: {user_input}",
        expected_output="Step-by-step solution"
    )

    # Crew
    crew = Crew(
        name="SmartCrew",
        tasks=[task1, task2],
        agents=[analysis_agent, solution_agent]
    )

    return safe_kickoff(crew)


if __name__ == "__main__":
    result = run_agents("I can't understand math")
    print(result)