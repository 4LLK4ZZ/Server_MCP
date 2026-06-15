import asyncio
from fastmcp import Client

URL_SERVIDOR = "http://localhost:8000/sse"
NOME_FERRAMENTA = "buscar_ultimas_noticias"

async def buscar_noticias():
    cliente = Client(URL_SERVIDOR)
    async with cliente:
        resultado = await cliente.call_tool(NOME_FERRAMENTA)
        print("\nÚltimas Notícias:")
        print(resultado)
        
if __name__ == "__main__":
    asyncio.run(buscar_noticias())