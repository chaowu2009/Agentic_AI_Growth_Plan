from dataclasses import dataclass, field
from typing import List, Callable, Dict, Any, Optional
import json
from pydantic import BaseModel


@dataclass
class Message:
    """represents a chat message in the conversation history"""
    role: str   # [system, user, assistant , tool]
    content: str

@dataclass
class Tool:
    """represents a tool that the assistant can use to perform specific tasks"""
    name: str
    description: str
    func: Callable[..., Any]  # function that implements the tool's behavior
    parameters: Optional[Dict[str, Any]] = field(default_factory=dict)

@dataclass
class Action:
    """represents an action taken by the assistant, which can be either a tool call or a message response"""
    thought: str
    action_name: Optional[str] = None  # name of the tool being called, if applicable
    action_input: Optional[str] = None  # input parameters for the tool, if applicable

@dataclass
class AgentState:
    """Holds the current state and memory of the agent."""
    messages: List[Message] = field(default_factory=list)  # conversation history
    step_count: int = 0


