
# Function takes user input and returns analysis and solution
def run_agents(user_input):
    # Create a simple analysis message
    analysis = f"Analysis of your problem: '{user_input}' shows main difficulties and points to focus on . "
    
    # Create a simple suggested solution for the user
    solution = f"Suggested solution: try breaking the problem into smaller steps and practice regularly . "
    
    return {
        "analysis": analysis,
        "solution": solution
    }
# it;s runs only when file is executed directly 
if __name__ == "__main__":
    result = run_agents(" I can't understand math ")
    print(result)