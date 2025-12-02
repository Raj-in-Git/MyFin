import requests

stocks = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=compact&apikey=U9D0GNY4CA9T8UPU")

print (stocks[0])
