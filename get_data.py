import config, time
from binance.client import Client
from binance.enums import *
import pandas as pd
client = Client(config.API_KEY, config.API_SECRET)

# Formats each row of incoming data 
def format_row(row):
        time = round(float(row[0])/1000)
        open = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])       
        volume = float(row[5])
        if open > close:
            volume = 0 - volume
        change = close-open
        amplitude = change/open 
        out = [time, open, high, low, close, volume, amplitude]
        return out

# Retrieves raw data from trading servers.  Returns 1000 rows max
def get_any(symbol, interval, start, end):
    target = client.get_historical_klines(symbol, interval, start, end)

    rows = []
    for row in target:
        rows.append(format_row(row))
    df = pd.DataFrame(rows, columns=['time','open','high','low', 'close', 'volume', 'amplitude'])

    return df


# User inputs
symbol = 'BTCUSDT' # Symbol for target trading pair
timeframe = KLINE_INTERVAL_1MINUTE # Target chart timeframe, 
out = pd.DataFrame()
start = 1636820525 
end = round(time.time())
iterate_by = 60000 # Number of seconds in timeframe

# Data retrieval
for i in range(start, end, iterate_by):
    temp = get_any(symbol, timeframe, str(i*1000), str((i+iterate_by)*1000))
    out = out.append(temp, ignore_index=True)
    print('batch: ', i)
out.to_csv('data/'+symbol+'_'+timeframe+'_'+str(start)+'_to_'+str(end)+'.csv')

