import requests
from fastmcp import FastMCP

servidor_mcp = FastMCP("mcp_cotacao")

def cotacao_moeda(moeda: str) -> str:
    if moeda == "Dólar":
        requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
        cotacao = requisicao.json()
        nome = cotacao["USDBRL"]["name"]
        data = cotacao["USDBRL"]["create_date"]
        valor = cotacao["USDBRL"]["bid"]
        mensagem = f"Cotação do {nome} em {data} é {valor} reais"
    elif moeda == "Euro":
        requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/EUR-BRL")
        cotacao = requisicao.json()
        nome = cotacao["EURBRL"]["name"]
        data = cotacao["EURBRL"]["create_date"]
        valor = cotacao["EURBRL"]["bid"]
        mensagem = f"Cotação do {nome} em {data} é {valor} reais"
    elif moeda == "Bitcoin":
        requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/BTC-BRL")
        cotacao = requisicao.json()
        nome = cotacao["BTCBRL"]["name"]
        data = cotacao["BTCBRL"]["create_date"]
        valor = cotacao["BTCBRL"]["bid"]
        mensagem = f"Cotação do {nome} em {data} é {valor} reais"
    else:
        mensagem = "Moeda não suportada. Use Dólar, Euro ou Bitcoin"
    return mensagem

@servidor_mcp.tool()
async def buscar_cotacao_moeda(moeda: str) -> str:
    """Retorna a cotação da moeda informada (Dólar, Euro ou Bitcoin) em reais."""
    return cotacao_moeda(moeda)
        
if __name__ == "__main__":
    servidor_mcp.run(transport="sse")