from fastmcp import FastMCP
from fastmcp.prompts.prompt import UserMessage, AssistantMessage
import yfinance as yf

mcp = FastMCP("FinanceiroMCP", request_timeout=60)

@mcp.tool()
def obter_preco_acao(ticker: str) -> float:
    """
    Retorna o preço atual da ação especificada pelo ticker
    """
    try:
        acao = yf.Ticker(ticker)
        preco = acao.info.get("currentPrice")
        if preco is None:
            raise ValueError("Preço não disponível")
        return preco
    except Exception as e:
        if "Too Many Requests" in str(e):
            raise ValueError("Limite de requisições atingido. Por favor, aguarde alguns minutos e tente novamente.")
        raise ValueError(f"Erro ao obter o preço da ação: {e}")
    
@mcp.resource("acao://{ticker}")
def informacoes_acao(ticker: str) -> dict:
    """
    Retorna informações básicas da ação, como nome, setor e país.
    """
    try:
        acao = yf.Ticker(ticker)
        info = acao.info
        return {
            "nome": info.get("longName", "N/A"),
            "setor": info.get("sector", "N/A"),
            "pais": info.get("country", "N/A")
        }
    except Exception as e:
        raise ValueError(f"Erro ao obter informações da ação: {e}")
    
@mcp.prompt()
def relatorio_financeiro(ticker: str) -> str:
    """
    Gera um relatório com o nome da empresa, setor,
    país e preço atual da ação
    """
    try:
        acao = yf.Ticker(ticker)
        info = acao.info
        nome = info.get("longName", "N/A"),
        setor = info.get("sector", "N/A"),
        pais = info.get("country", "N/A"),
        preco = info.get("currentPrice", 0.0)
        
        return (
            f"Empresa: {nome}\n"
            f"Setor: {setor}\n"
            f"País: {pais}\n"
            f"Preço Atual R$: {preco}\n"
            
        )
    except Exception as e:
        return f"Erro ao gerar o relatório financeiro para o ticker: {ticker}: {e}"