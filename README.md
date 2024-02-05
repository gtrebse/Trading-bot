# Trade bot framework

This is a Python project that includes a trading bot, data analysis, and various trading strategies.

## Project Structure

The project has the following structure:

- `main.py`: The main entry point of the application.
- `analysis.ipynb`: A Jupyter notebook for data analysis.
- `data/keys.py`: Add relevant keys for connecting and trading on relevant exchanges
- `src/db_helper.py`: Contains helper functions for database operations.
- `src/trade_bot.py`: Contains the implementation of the trading bot.
- `trading_strategies/example_strategy.py`: Contains an example trading strategy. Add additional trading strategies to this folder.

## Adding New Trading Strategies

To add a new trading strategy, create a new Python file in the `trading_strategies/` directory. The file should define a function that implements the trading strategy. The function should take as input the current market state and return trading signals.

The trading strategy function is kept separate in order not to expose it to git.

For example, a simple trading strategy might look like this:

```python
def simple_strategy(sefl, orderbook1, orderbook2):
    if orderbook1['price'] < orderbook2['moving_average']:
        # Perform Buy
    else:
        # Perform Sell
```

After creating the new strategy file, import it in the trade_bot.py file and add it to the list of strategies.

## Running the Project
To run the project, execute the main.py file:
```bash
python main.py
```