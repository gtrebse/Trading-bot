
import src.db_helper as db_helper

def example_strategy(self, orderbook1, orderbook2):
    bid1 = float(orderbook1['bids'][0][0])
    ask1 = float(orderbook1['asks'][0][0])
    bid2 = float(orderbook2['bids'][0][0])
    ask2 = float(orderbook2['asks'][0][0])
    print(f"bid1: {bid1}, ask1: {ask1}, bid2: {bid2}, ask2: {ask2}")

    # Execute strategy only if the delta in prices is > 1.0025
    if bid1/ask2 > 1.0025:
        print(f"Ratio between bid1 and ask2: {bid1/ask2}")
        db_helper.log_trade(self.ticker, 'Buy on KuCoin', 'Sell on MEXC', ask2, bid1, bid1/ask2)
    elif bid2/ask1 > 1.0025:
        print(f"Ratio between bid2 and ask1: {bid2/ask1}")
        db_helper.log_trade(self.ticker, 'Buy on MEXC', 'Sell on KuCoin', ask1, bid2, bid2/ask1)
    else:
        print("Prices are equal; no action taken.")
