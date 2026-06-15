import asyncio, sys, os

async def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from utils.mcp_util import McpUtil
    client = McpUtil()
    try:
        await client.initialize_with_sse("http://localhost:8000/sse")
        result = await client.call_tool("obter_preco_acao",{
            "ticker": "BBAS3.SA"
        })
        print(f"Price :{result.content[0].text}")
        
        result = await client.get_resource("acao://BBAS3.SA")
        info = result.contents[0].text
        print(f"Info :{info}")
        
        result = await client.invoke_prompt("relatorio_financeiro",{
            "ticker": "BBAS3.SA"
        })
        print(f"Report", {result.messages[0].content.text})
        
    finally:
        await client.cleanup()
        
if __name__ == "__main__":
    asyncio.run(main())