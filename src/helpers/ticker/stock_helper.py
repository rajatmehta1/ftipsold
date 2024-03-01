from ..langchains.chain_helper import ChainHelper

class StockHelper:

    def __init__(self):
        self.ch = ChainHelper()
        
    def get_stock_curr(self, stck):
        print(f'======> Can you do some fundamental analysis on {stck} ')
        return str(self.ch.reply(f'Can you do some fundamental analysis on {stck} and return response in plain text with Markdown format'))
