import requests
from bs4 import BeautifulSoup
from fastmcp import FastMCP

servidor_mcp = FastMCP("mcp_noticias")

def ultimas_noticias() -> str:
    url = "https://news.google.com/rss?gl=BR&hl=pt-BR&ceid=BR:pt-419"
    site = requests.get(url)
    noticias = BeautifulSoup(site.text, "html.parser")
    noticias_texto = []
    for item in noticias.findAll("item")[:5]:
        titulo = item.title.text
        noticias_texto.append(titulo)
    return " ".join(noticias_texto)

@servidor_mcp.tool()
async def buscar_ultimas_noticias() -> str:
    return ultimas_noticias()

if __name__ == "__main__":
    servidor_mcp.run(transport="sse")