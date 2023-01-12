import pandas as pd
from urllib.request import Request, urlopen
import csv
from datetime import datetime
import os
import time

# Add while loop to get the most recent stats automatically

i = 1
while i == 1:
    url = 'https://goldprice.org/cryptocurrency-price'
    import_request = Request(url, headers={'user-Agent': 'Chrome/108.0.0.0 Safari/537.36'})
    data = urlopen(import_request).read()
    finance = pd.read_html(data)
    print(finance[0])
    # Display Table in the correct format
    # print(finance[0])

    # Shows columns
    # print(finance[0].columns)

    # Filter columns

    finance[0].drop(finance[0].columns[[4, 5, 7, ]], axis=1, inplace=True)  # 1 = Columns 0 = Rows
    # Checking the Data types


    # print(finance[0].dtypes)

    # Renaming columns
    finance[0].rename(columns={'Change (24h)': 'Change (24h) %'}, inplace=True)


    #  Take out all the % commas, and currency symbols::
    # This takes out the $ symbol
    finance[0]['Market Cap.'] = list(map(lambda x: x[1:], finance[0]['Market Cap.']. values))
    # This takes out the $ symbol
    finance[0]['Price'] = list(map(lambda x: x[1:], finance[0]['Price']. values))
    # This takes out the % symbol
    finance[0]['Change (24h) %'] = list(map(lambda x: x[:-1], finance[0]['Change (24h) %']. values))

    # This takes out the Commas
    finance[0]['Market Cap.'] = finance[0]['Market Cap.'].str.replace(',', '')
    finance[0]['Price'] = finance[0]['Price'].str.replace(',', '')

    # Update data types
    finance[0]['Market Cap.'] = finance[0]['Market Cap.'].astype('int64')
    finance[0]['Price'] = finance[0]['Price'].astype(float).round(2)
    finance[0]['Change (24h) %'] = finance[0]['Change (24h) %'].astype(float).round(2)

    # Update positions
    finance[0] = finance[0][['Rank', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']]

    # Sleep function will update the data for the selected period stated
    time.sleep(5) # New row will be added and updated every 5 seconds
    # From Callback
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    # Process Each Coin - Bitcoin
    # rank
    bc_rank = finance[0][finance[0]['CryptoCurrency'] == 'Bitcoin']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    bc_currency = finance[0][finance[0]['CryptoCurrency'] == 'Bitcoin']['CryptoCurrency'].iloc[0]
    # price
    bc_price = finance[0][finance[0]['CryptoCurrency'] == 'Bitcoin']['Price'].iloc[0]
    # change
    bc_change = finance[0][finance[0]['CryptoCurrency'] == 'Bitcoin']['Change (24h) %'].iloc[0]
    # market
    bc_market = finance[0][finance[0]['CryptoCurrency'] == 'Bitcoin']['Market Cap.'].iloc[0]

    # Ethereum
    # rank
    et_rank = finance[0][finance[0]['CryptoCurrency'] == 'Ethereum']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    et_currency = finance[0][finance[0]['CryptoCurrency'] == 'Ethereum']['CryptoCurrency'].iloc[0]
    # price
    et_price = finance[0][finance[0]['CryptoCurrency'] == 'Ethereum']['Price'].iloc[0]
    # change
    et_change = finance[0][finance[0]['CryptoCurrency'] == 'Ethereum']['Change (24h) %'].iloc[0]
    # market
    et_market = finance[0][finance[0]['CryptoCurrency'] == 'Ethereum']['Market Cap.'].iloc[0]

    # Tether
    # rank
    tet_rank = finance[0][finance[0]['CryptoCurrency'] == 'Tether']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    tet_currency = finance[0][finance[0]['CryptoCurrency'] == 'Tether']['CryptoCurrency'].iloc[0]
    # price
    tet_price = finance[0][finance[0]['CryptoCurrency'] == 'Tether']['Price'].iloc[0]
    # change
    tet_change = finance[0][finance[0]['CryptoCurrency'] == 'Tether']['Change (24h) %'].iloc[0]
    # market
    tet_market = finance[0][finance[0]['CryptoCurrency'] == 'Tether']['Market Cap.'].iloc[0]

    # USD Coin
    # rank
    usd_rank = finance[0][finance[0]['CryptoCurrency'] == 'USD Coin']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    usd_currency = finance[0][finance[0]['CryptoCurrency'] == 'USD Coin']['CryptoCurrency'].iloc[0]
    # price
    usd_price = finance[0][finance[0]['CryptoCurrency'] == 'USD Coin']['Price'].iloc[0]
    # change
    usd_change = finance[0][finance[0]['CryptoCurrency'] == 'USD Coin']['Change (24h) %'].iloc[0]
    # market
    usd_market = finance[0][finance[0]['CryptoCurrency'] == 'USD Coin']['Market Cap.'].iloc[0]

    # BNB Coin
    # rank
    bnb_rank = finance[0][finance[0]['CryptoCurrency'] == 'BNB']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    bnb_currency = finance[0][finance[0]['CryptoCurrency'] == 'BNB']['CryptoCurrency'].iloc[0]
    # price
    bnb_price = finance[0][finance[0]['CryptoCurrency'] == 'BNB']['Price'].iloc[0]
    # change
    bnb_change = finance[0][finance[0]['CryptoCurrency'] == 'BNB']['Change (24h) %'].iloc[0]
    # market
    bnb_market = finance[0][finance[0]['CryptoCurrency'] == 'BNB']['Market Cap.'].iloc[0]

    # BIN Coin
    # rank
    bin_rank = finance[0][finance[0]['CryptoCurrency'] == 'Binance USD']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    bin_currency = finance[0][finance[0]['CryptoCurrency'] == 'Binance USD']['CryptoCurrency'].iloc[0]
    # price
    bin_price = finance[0][finance[0]['CryptoCurrency'] == 'Binance USD']['Price'].iloc[0]
    # change
    bin_change = finance[0][finance[0]['CryptoCurrency'] == 'Binance USD']['Change (24h) %'].iloc[0]
    # market
    bin_market = finance[0][finance[0]['CryptoCurrency'] == 'Binance USD']['Market Cap.'].iloc[0]

    # XRP Coin
    # rank
    xrp_rank = finance[0][finance[0]['CryptoCurrency'] == 'XRP']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    xrp_currency = finance[0][finance[0]['CryptoCurrency'] == 'XRP']['CryptoCurrency'].iloc[0]
    # price
    xrp_price = finance[0][finance[0]['CryptoCurrency'] == 'XRP']['Price'].iloc[0]
    # change
    xrp_change = finance[0][finance[0]['CryptoCurrency'] == 'XRP']['Change (24h) %'].iloc[0]
    # market
    xrp_market = finance[0][finance[0]['CryptoCurrency'] == 'XRP']['Market Cap.'].iloc[0]

    # DOGECoin
    # rank
    dog_rank = finance[0][finance[0]['CryptoCurrency'] == 'Dogecoin']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    dog_currency = finance[0][finance[0]['CryptoCurrency'] == 'Dogecoin']['CryptoCurrency'].iloc[0]
    # price
    dog_price = finance[0][finance[0]['CryptoCurrency'] == 'Dogecoin']['Price'].iloc[0]
    # change
    dog_change = finance[0][finance[0]['CryptoCurrency'] == 'Dogecoin']['Change (24h) %'].iloc[0]
    # market
    dog_market = finance[0][finance[0]['CryptoCurrency'] == 'Dogecoin']['Market Cap.'].iloc[0]

    # Cardano
    # rank
    car_rank = finance[0][finance[0]['CryptoCurrency'] == 'Cardano']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    car_currency = finance[0][finance[0]['CryptoCurrency'] == 'Cardano']['CryptoCurrency'].iloc[0]
    # price
    car_price = finance[0][finance[0]['CryptoCurrency'] == 'Cardano']['Price'].iloc[0]
    # change
    car_change = finance[0][finance[0]['CryptoCurrency'] == 'Cardano']['Change (24h) %'].iloc[0]
    # market
    car_market = finance[0][finance[0]['CryptoCurrency'] == 'Cardano']['Market Cap.'].iloc[0]

    # Polygon
    # rank
    poly_rank = finance[0][finance[0]['CryptoCurrency'] == 'Polygon']['Rank'].iloc[0]  # loc[0] takes out the index 0
    # currency
    poly_currency = finance[0][finance[0]['CryptoCurrency'] == 'Polygon']['CryptoCurrency'].iloc[0]
    # price
    poly_price = finance[0][finance[0]['CryptoCurrency'] == 'Polygon']['Price'].iloc[0]
    # change
    poly_change = finance[0][finance[0]['CryptoCurrency'] == 'Polygon']['Change (24h) %'].iloc[0]
    # market
    poly_market = finance[0][finance[0]['CryptoCurrency'] == 'Polygon']['Market Cap.'].iloc[0]

    # The sleep function will update the stats every 5 seconds and then a csv file will be created::
    with open('bc_data.csv', 'a')as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, bc_rank, bc_currency, bc_price, bc_change, bc_market])
        # print(dt_string, bc_rank, bc_currency, bc_price, bc_change, bc_market)

    with open('et_data.csv', 'a')as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, et_rank, et_currency, et_price, et_change, et_market])
        # print(dt_string, et_rank, et_currency, et_price, et_change, et_market)

    with open('tet_data.csv', 'a')as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, tet_rank, tet_currency, tet_price, tet_change, tet_market])
        # print(dt_string, tet_rank, tet_currency, tet_price, tet_change, tet_market)

    with open('usd_data.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, usd_rank, usd_currency, usd_price, usd_change, usd_market])
        # print(dt_string, usd_rank, usd_currency, usd_price, usd_change, usd_market)

    with open('bnb_data.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, bnb_rank, bnb_currency, bnb_price, bnb_change, bnb_market])
        # print(dt_string, bnb_rank, bnb_currency, bnb_price, bnb_change, bnb_market)

    with open('bin_data.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, bin_rank, bin_currency, bin_price, bin_change, bin_market])
        # print(dt_string, bin_rank, bin_currency, bin_price, bin_change, bin_market)

    with open('xrp_data.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, xrp_rank, xrp_currency, xrp_price, xrp_change, xrp_market])
        # print(dt_string, xrp_rank, xrp_currency, xrp_price, xrp_change, xrp_market)

    with open('dog_data.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, dog_rank, dog_currency, dog_price, dog_change, dog_market])
        # print(dt_string, dog_rank, dog_currency, dog_price, dog_change, dog_market)

    with open('car_data.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, car_rank, car_currency, car_price, car_change, car_market])
        # print(dt_string, car_rank, car_currency, car_price, car_change, car_market)

    with open('poly_data.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([dt_string, poly_rank, poly_currency, poly_price, poly_change, poly_market])
        # print(dt_string, poly_rank, poly_currency, poly_price, poly_change, poly_market)