import asyncio
from pathlib import Path
from fastmcp import Client

# URL do servidor
url_servidor = "http://localhost:8000/sse"

cliente_mcp = Client(url_servidor)

async def testar_servidor(cliente: Client, nome_usuario: str, id_usuario: int) -> None:
    """Envia uma solicitação para o servidor MCP e imprime o resultado"""
    async with cliente:
        argumentos = {"nome_usuario": nome_usuario, "id_usuario": id_usuario}
        resultado = await cliente.call_tool("bom_dia", arguments=argumentos)
        print(f"Resultado obtido do servidor MCP: {resultado}")
        
if __name__ == "__main__":
    asyncio.run(testar_servidor(
        cliente=cliente_mcp,
        nome_usuario="Matheo",
        id_usuario=100
    ))