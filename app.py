from stock_vcpscreener import StockVCPScreener
from datetime import date

selected_date = date(2023, 12, 16)

svs = StockVCPScreener(selected_date, ['AAPL'])
svs.check_stock_database('yfinance', create=True)

svs.select_stock()
