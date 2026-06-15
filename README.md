````markdown
# Servidores MCP

Coleção de servidores e clientes desenvolvidos utilizando o protocolo MCP (Model Context Protocol) para integração de ferramentas, APIs e fontes de dados em aplicações de Inteligência Artificial.

## Sobre o Projeto

Este repositório reúne exemplos práticos de implementação de servidores MCP e seus respectivos clientes para diferentes domínios de informação, permitindo que modelos de IA acessem recursos externos de forma padronizada.

Atualmente o projeto contempla integrações com:

- Notícias
- Wikipedia
- Dados financeiros
- SSE (Server-Sent Events)
- Processamento de imagens
- Consulta de cotações

## Estrutura do Projeto

```text
.
├── utils/
│
├── client.py
├── client_noticias.py
├── client_noticias2.py
├── client_wikipedia.py
├── cliente_sse.py
│
├── finance_server.py
├── image_mcp.py
│
├── mcp_client.py
├── mcp_client_finance.py
├── mcp_client_gradio.py
│
├── mcp_server.py
├── server.py
│
├── server_cotacao.py
├── server_noticias.py
├── server_sse.py
├── server_wikipedia.py
│
├── mcp_cotacao.json
├── mcp_noticias.json
├── mcp_wiki.json
│
├── requirements.txt
└── .gitignore
````

## Requisitos

* Python 3.10 ou superior
* pip
* Ambiente virtual (recomendado)

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd servidores-mcp
```

Crie um ambiente virtual:

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

### Servidor de Notícias

```bash
python server_noticias.py
```

### Servidor Wikipedia

```bash
python server_wikipedia.py
```

### Servidor Financeiro

```bash
python finance_server.py
```

### Servidor SSE

```bash
python server_sse.py
```

### Servidor de Cotação

```bash
python server_cotacao.py
```

## Clientes de Teste

### Cliente Genérico

```bash
python client.py
```

### Cliente de Notícias

```bash
python client_noticias.py
```

### Cliente Wikipedia

```bash
python client_wikipedia.py
```

### Cliente SSE

```bash
python cliente_sse.py
```

### Cliente Financeiro

```bash
python mcp_client_finance.py
```

## Configuração MCP

As configurações dos servidores podem ser definidas através dos arquivos JSON disponíveis no projeto.

Exemplo:

```json
{
  "server": {
    "command": "python",
    "args": ["server_noticias.py"]
  }
}
```

Arquivos de configuração disponíveis:

* `mcp_cotacao.json`
* `mcp_noticias.json`
* `mcp_wiki.json`

## Tecnologias Utilizadas

* Python
* MCP (Model Context Protocol)
* AsyncIO
* Requests
* SSE (Server-Sent Events)
* APIs REST
* Gradio

## Objetivos

* Demonstrar a criação de servidores MCP.
* Integrar ferramentas externas com aplicações de IA.
* Disponibilizar exemplos de consumo de serviços via MCP.
* Servir como base para estudos e desenvolvimento de agentes inteligentes.
