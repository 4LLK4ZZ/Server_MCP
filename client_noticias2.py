import asyncio
from fastmcp import Client

URL_SERVIDOR = "http://localhost:8000/sse"
NOME_FERRAMENTA = "buscar_ultimas_noticias"

def processar_resultado(resultado):
    if isinstance(resultado, list) and resultado and hasattr(resultado[0], "text"):
        texto = resultado[0].text
    else:
        texto = str(resultado)
    
    noticias = texto.split(" - ")
    noticias_formatadas = []
    for i in range(len(noticias) - 1):
        partes = noticias[i].rsplit(",", 1)
        if len(partes) == 2:
            noticia = partes[0] + " - " + partes[1]
        else:
            noticia = noticias[i]
        noticias_formatadas.append(noticia.strip())
    noticias_formatadas.append(noticias[-1].strip())
    return noticias_formatadas

async def buscar_noticias():
    cliente = Client(URL_SERVIDOR)
    async with cliente:
        resultado = await cliente.call_tool(NOME_FERRAMENTA)
        noticias = processar_resultado(resultado)
        print("\nÚltimas Notícias:")
        for noticia in noticias:
            print(f"{noticia}")
        
if __name__ == "__main__":
    asyncio.run(buscar_noticias())