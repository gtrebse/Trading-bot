
from src.trade_bot import TradingBot
from trading_strategies.arbitrage_volume_strategy import arbitrage_volume_strategy
import src.db_helper as db_helper

def main():
    # Example usage:
    ticker_list = ['SOLUSDT', 'BTCUSDT', 'ETHUSDT', 'MANTAUSDT', 'JUPUSDT', 'MINAUSDT', 'AMPLUSDT']
    bots = []

    for ticker in ticker_list:
        # Initialize the database table for the ticker
        db_helper.init_db(ticker)
        
        # Create and start the bot
        bot = TradingBot('MEXC', 'KuCoin', 'BTC', ticker, arbitrage_volume_strategy)
        bots.append(bot)
        bot.start()

    # You can add code here to handle graceful shutdowns, logging, etc.

if __name__ == "__main__":
    main()