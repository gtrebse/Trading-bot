import requests
import threading
import time
from typing import Callable
from mexc_sdk import Spot
from kucoin.client import Market
import data.keys as keys
import src.db_helper as db_helper


class PriceFetcher:
    def get_price(self, spot, ticker):
        raise NotImplementedError("This method should be implemented by subclasses")

class MEXCPriceFetcher(PriceFetcher):
    def get_price(self, spot, ticker):
        order_book = spot.depth(ticker, {"limit": 5})
        return order_book

class KuCoinPriceFetcher(PriceFetcher):
    def get_price(self, spot, ticker):
        order_book = spot.get_aggregated_orderv3(ticker) 
        return order_book

class TradingBot:
    def __init__(self, platform1, platform2, currency, ticker, strategy: Callable):
        self.price_fetchers = {
            'MEXC': MEXCPriceFetcher(),
            'KuCoin': KuCoinPriceFetcher(),
        }
        self.spot = Spot(keys.mexc_access_key, keys.mexc_secret_key)
        self.kucoin_client = Market(keys.kucoin_key, keys.kucoin_secret, keys.kucoin_pass)
        
        self.platform1_name = platform1
        self.platform2_name = platform2
        self.platform1 = self.price_fetchers[platform1]
        self.platform2 = self.price_fetchers[platform2]
        self.currency = currency
        self.ticker = ticker
        self.strategy = strategy
        self.running = False
        self.price_monitor_thread = None

    def start(self):
        """Starts the monitoring and trading process."""
        db_helper.init_db(self.ticker)
        self.running = True
        self.price_monitor_thread = threading.Thread(target=self.monitor_prices)
        self.price_monitor_thread.start()

    def stop(self):
        """Stops the monitoring and trading process."""
        self.running = False
        if self.price_monitor_thread:
            self.price_monitor_thread.join()

    def monitor_prices(self):
        """Monitors prices on both platforms and executes the trading strategy."""
        while self.running:
            mexc_ticker = self.ticker
            kucoin_ticker = self.ticker.replace("USDT", "-USDT")
            order_book1 = self.get_price(self.platform1, self.spot, mexc_ticker)
            order_book2 = self.get_price(self.platform2, self.kucoin_client, kucoin_ticker)
            self.strategy(self, order_book1, order_book2)
            time.sleep(0.1)  # Sleep for a second or your preferred interval

    def get_price(self, platform, spot, ticker):
        """Delegates price fetching to the appropriate platform's price fetcher."""
        return platform.get_price(spot, ticker)

    def execute_trade(self, platform, trade_type, amount, price):
        """Executes a trade on the specified platform."""
        # This function should be implemented to execute a trade on the platform.
        pass
