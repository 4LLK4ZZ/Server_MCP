import asyncio, sys, os

async def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from utils.mcp_util import McpUtil
    client = McpUtil()
    
    try:
        await client.initialize_with_sse("http://localhost:8000/sse")
        print("=== Execução da Tool: add(a = 12, b = 5) === ")
        result = await client.call_tool("add", {"a": 12, "b": 5})
        soma = "".join([c.text for c in result.content if c.type == "text"])
        print(f"Resultado da soma: {soma}")
        
        result = await client.get_resource("greeting://John")
        text = result.contents[0].text
        print(f"Greeting: {text}")
        
        result = await client.get_resource("db://users/456/email")
        email = result.contents[0].text
        print(f"Email User 456: {email}")
        
        result = await client.invoke_prompt("greeting", {"name": "John"})
        response = result.messages[0].content.text
        print(f"Response Prompt: {response}")
    
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())