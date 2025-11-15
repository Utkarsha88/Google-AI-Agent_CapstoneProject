from agents.assignment_checker_agent import AssignmentCheckerAgent

API_KEY =  "your_api_key_here"

agent = AssignmentCheckerAgent(API_KEY)

payload = {
    "text": "Teh cat is on teh mat. this is secon pargraph."
}

output = agent.run(payload)
print(output)
