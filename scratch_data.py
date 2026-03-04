import yfinance as yf
import pandas as pd

# 1. Khai báo mã cổ phiếu/tài sản (Gold Futures là GC=F)
ticker_symbol = "GC=F"

# 2. Tải dữ liệu
# period: khoảng thời gian (1d, 5d, 1mo, 1y, 5y, max, etc.)
# interval: tần suất dữ liệu (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
gold_data = yf.download(ticker_symbol, start="2015-01-01", end="2026-03-01", interval="1d")

# 3. Kiểm tra dữ liệu
print("Dữ liệu 5 dòng đầu tiên:")
print(gold_data.head())

# 4. Lưu dữ liệu ra file CSV để tiện phân tích sau này (không cần cào lại nhiều lần)
gold_data.to_csv("gold_prices.csv")

print("\nĐã lưu dữ liệu vào file gold_prices.csv thành công!")