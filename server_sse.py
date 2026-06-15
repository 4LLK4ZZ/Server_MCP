from fastmcp import FastMCP

server = FastMCP("mcp-teste-sse")

@server.tool()
async def bom_dia(nome_usuario: str, id_usuario: int) -> str:
    return f"Olá, {nome_usuario} (ID: {id_usuario})"

if __name__ == "__main__":
    server.run(transport="sse")