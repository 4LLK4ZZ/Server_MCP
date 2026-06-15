import asyncio, sys, os
import gradio as gr

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.mcp_util import McpUtil

async def get_price_gradio(ticker):
    client = McpUtil()
    try:
        await client.initialize_with_sse("http://localhost:8000/sse")
        result = await client.call_tool("obter_preco_acao", {"ticker": ticker})
        price = "".join([c.text for c in result.content if c.type == "text"]) 
        return f"Price {ticker} -> {price}"
    finally:
        await client.cleanup()
        
async def get_ticket_info(ticker):
    client = McpUtil()
    try:
        await client.initialize_with_sse("http://localhost:8000/sse")
        result = await client.get_resource(f"acao://{ticker}")
        info = result.contents[0].text
        return f"Info {ticker} ->:\n{info}"
    finally:
        await client.cleanup()
        
async def report_finance(ticker):
    client = McpUtil()
    try:
        await client.initialize_with_sse("http://localhost:8000/sse")
        result = await client.invoke_prompt("relatorio_financeiro",{
            "ticker": ticker
        })
        report = result.messages[0].content.text
        return report
    finally:
        await client.cleanup()
        
def run_async(func, *args):
    return asyncio.run(func(*args))

with gr.Blocks() as demo:
    gr.Markdown("Report Finance MCP Client (Gradio)")
    with gr.Tab("Price"):
        ticker1 = gr.Textbox(label="Ticker", value="BBAS3.SA")
        btn_price = gr.Button("Get Price")
        out_price = gr.Textbox(label="Price")
        btn_price.click(lambda x: run_async(get_price_gradio, x), inputs=ticker1, outputs=out_price)
    with gr.Tab("Info"):
        ticker2 = gr.Textbox(label="Ticker", value="BBAS3.SA")
        btn_info = gr.Button("Get Info")
        out_info = gr.Textbox(label="Info")
        btn_info.click(lambda x: run_async(get_ticket_info, x), inputs=ticker2, outputs=out_info)
    with gr.Tab("Report Finance"):
        ticker3 = gr.Textbox(label="Ticker", value="BBAS3.SA")
        btn_report = gr.Button("Generate Report")
        out_report = gr.Textbox(label="Report")
        btn_report.click(lambda x: run_async(report_finance, x), inputs=ticker3, outputs=out_report)
        
demo.launch()
    
