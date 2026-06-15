from fastmcp import FastMCP
from fastmcp.prompts.prompt import UserMessage, AssistantMessage

mcp = FastMCP("Demo MCP")

@mcp.tool()
def add(a: int, b:int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.resource("db://users/{user_id}/email")
async def get_user_email(user_id: str) -> str:
    """Retrieves the email address for a given user ID."""
    # Replace with actual database lookup
    emails = {"123": "alice@example.com", "456": "bob@example.com"}
    return emails.get(user_id, "not_found@example.com")

@mcp.prompt()
def greeting(name: str) -> str:
    """Generates a personalized greeting message"""
    return f"Hello, {name}! How can I help you?"
    
@mcp.prompt()
def start_debug_session(error_msg: str) -> list:
    """Starts a help session for debugging"""
    return [
        UserMessage(f"I encountered the following error:\n {error_msg}"),
        AssistantMessage("Understood. Can you provide the full traceback and explain what you were trying to do?")
    ]
if __name__ == "__main__":
    mcp.run()