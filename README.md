# 🚀 Servidores MCP


\

Coleção de servidores e clientes desenvolvidos com o **Model Context Protocol (MCP)** para integração de ferramentas, APIs e fontes de dados em aplicações de Inteligência Artificial.

## 📖 Visão Geral

Este projeto reúne exemplos práticos de implementação de servidores MCP e seus respectivos clientes, permitindo que modelos de IA acessem recursos externos de forma padronizada, escalável e reutilizável.

As integrações atualmente disponíveis incluem:

* 📰 Notícias
* 📚 Wikipedia
* 💰 Dados financeiros
* 📈 Consulta de cotações
* 🖼️ Processamento de imagens
* 📡 SSE (Server-Sent Events)

## ✨ Funcionalidades

* Implementação de múltiplos servidores MCP.
* Clientes de teste para validação das integrações.
* Comunicação via APIs REST.
* Streaming de eventos utilizando SSE.
* Integração com fontes externas de dados.
* Exemplos para estudo e desenvolvimento de agentes inteligentes.

---

## 📂 Estrutura do Projeto

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
```

---

## ⚙️ Pré-requisitos

Antes de iniciar, certifique-se de possuir:

* Python 3.10 ou superior
* pip
* Ambiente virtual (recomendado)

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd servidores-mcp
```

### 2. Crie um ambiente virtual

#### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando os Servidores

### 📰 Servidor de Notícias

```bash
python server_noticias.py
```

### 📚 Servidor Wikipedia

```bash
python server_wikipedia.py
```

### 💰 Servidor Financeiro

```bash
python finance_server.py
```

### 📡 Servidor SSE

```bash
python server_sse.py
```

### 📈 Servidor de Cotação

```bash
python server_cotacao.py
```

---

## 🧪 Clientes de Teste

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

---

## 🔧 Configuração MCP

Os servidores podem ser configurados através dos arquivos JSON disponibilizados no projeto.

### Exemplo

```json
{
  "server": {
    "command": "python",
    "args": ["server_noticias.py"]
  }
}
```

### Arquivos disponíveis

* `mcp_cotacao.json`
* `mcp_noticias.json`
* `mcp_wiki.json`

---

## 🛠️ Tecnologias Utilizadas

* Python
* Model Context Protocol (MCP)
* AsyncIO
* Requests
* Server-Sent Events (SSE)
* APIs REST
* Gradio

---

## 🎯 Objetivos

Este projeto tem como finalidade:

* Demonstrar a criação de servidores MCP.
* Integrar ferramentas externas com aplicações de IA.
* Disponibilizar exemplos de consumo de serviços via MCP.
* Servir como base para estudos e desenvolvimento de agentes inteligentes.
