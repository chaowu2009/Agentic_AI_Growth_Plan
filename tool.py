import datetime
import re
from AgentClass import Tool
import json

def get_current_time(*args, **kwargs) -> str:
    """Returns the current UTC time."""
    return datetime.datetime.utcnow().isoformat() + "Z"

def calculate(expression: str) -> str:
    """Safely evaluates a basic mathematical expression."""
    # Safety Check: Only allow digits and basic math operators
    if not re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expression):
        return "Error: Expression contains invalid characters."
    try:
        return str(eval(expression)) 
    except Exception as e:
        return f"Error evaluating expression: {e}"

# Register the tools
time_tool = Tool(
    name="get_current_time",
    description="Returns the current time in UTC. Use this when you need to know what time it is.",
    func=get_current_time,
    parameters={}
)

math_tool = Tool(
    name="calculate",
    description="Evaluates a mathematical expression. Input must be a string like '2 + 2'.",
    func=calculate,
    parameters={"expression": "string"}
)

AVAILABLE_TOOLS = {t.name: t for t in [time_tool, math_tool]}