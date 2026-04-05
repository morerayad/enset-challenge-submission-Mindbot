def run_agents(user_input):
    # Mock analysis
    analysis = f"Analysis of your problem: '{user_input}' shows main difficulties and points to focus on."
    
    # Mock solution
    solution = f"Suggested solution: try breaking the problem into smaller steps and practice regularly."
    
    return {
        "analysis": analysis,
        "solution": solution
    }

if __name__ == "__main__":
    result = run_agents("I can't understand math")
    print(result)