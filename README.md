A single call to the Binance server can only retrieve 1000 rows of data, presenting a problem when trying to retrieve short timeframe historical data from large time windows.  A year's worth of 1-minute data is 525,600 rows.  This script will iterate through the given range of time, pulling data in 1000 row chunks and storing them in a dataframe until.  When all rows are retrieved a .csv file is output to the 'data' folder.  The script requires a set of Binance API keys from the user.  

# Setup
Dependencies: pandas, python-binance
Copy your API keys into the corresponding fields in the 'config' file.

# Use
Enter desired values into corresponding fields in the user input section of the 'get_data' file and run.  
