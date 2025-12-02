import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=compact&apikey={API_KEY}"

stocks = requests.get(url)

data = stocks.json()

latest_date = list(data["Time Series (Daily)"].keys())[0]
close_price = data["Time Series (Daily)"][latest_date]["4. close"]

print("Latest Close Price:", close_price)
