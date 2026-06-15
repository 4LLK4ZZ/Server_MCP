import asyncio
from pathlib import Path
from fastmcp import Client

# Caminho do servidor
caminho_servidor = Path(__file__).parent / "server.py"

cliente_mcp = Client(caminho_servidor)

async def testar_servidor(cliente: Client, nome_usuario: str, id_usuario: int):
    async with cliente:
        argumentos = {"nome_usuario": nome_usuario, "id_usuario": id_usuario}
        resultado = await cliente.call_tool("bom_dia", arguments=argumentos)
        print(f"Resultado obtido do servidor MCP: {resultado}")
        
if __name__ == "__main__":
    asyncio.run(testar_servidor(
        cliente=cliente_mcp,
        nome_usuario="John",
        id_usuario=50
    ))