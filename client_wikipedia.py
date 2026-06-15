import asyncio
import os
from typing import Any
import dotenv
from fastmcp import Client
from openai import OpenAI

# Constantes
URL_SERVIDOR = "http://localhost:8000/sse"
NOME_FERRAMENTA = "buscar_wikipedia"
MODELO_OPENAI = "gpt-4o-mini"

cliente_mcp = Client(URL_SERVIDOR)

def carregar_api_key() -> str:
    """Carrega a chave da API do OpenAI a partir do arquivo .env"""
    dotenv.load_dotenv()
    return os.environ["OPENAI_APIKEY"]

def montar_prompt(busca: str, resultado: str) -> str:
    """Gera uma instrução amigável para o modelo da OpenAI"""
    return(
        f"""
        Você é um assistente especializado em fornecer respostas concisas
        e amigáveis baseadas em conteúdo extraído da Wikipedia
        
        Tema da busca: {busca} 
        Resultado encontrado: {resultado}
        
        Com base nesse conteúdo, elabore uma explicação clara e interessante
        para o usuário como se estivesse explicando para alguém curioso pelo assunto.
        """
    )
    
async def testar_servidor(cliente: Client, busca: str) -> None:
    """Executa uma busca na Wikipedia via MCP e sintetiza a resposta com OpenAI"""
    api_key = carregar_api_key()
    
    async with cliente:
        resultado = await cliente.call_tool(
            NOME_FERRAMENTA, arguments={"busca": busca}
        )
        print(f"\n[Resultado da busca na Wikipedia]:\n{resultado}\n")
        
        prompt = montar_prompt(busca, resultado)
        openai_client = OpenAI(api_key=api_key)
        resposta = openai_client.responses.create(
            model=MODELO_OPENAI,
            instructions=prompt,
            input="Pode me explicar esse assunto?",
        )
        print("[Resposta Sintetizada pelo OpenAI]")
        print(resposta.output_text)
        
if __name__ == "__main__":
    asyncio.run(testar_servidor(
        cliente=cliente_mcp,
        busca="Sociedade Esportiva Palmeiras"
    ))