from fastapi import FastAPI, Response
import yfinance as yf
from helpers.ticker.stock_helper import StockHelper
# from ..helpers.ticker.stock_helper import StockHelper
app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello from fast api"}

@app.get("/question/")
async def input(q: str = None):
    return {"message": "Hello from fast api"}

def get_stock_details(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    return stock.info

# @app.get("/stock/{ticker_symbol}")
# async def read_stock(ticker_symbol: str):
#     return get_stock_details(ticker_symbol)


@app.get("/stock/{q}")
def read_text(q: str):
    sh = StockHelper()
    return Response(sh.get_stock_curr(q),media_type="text/plain")

