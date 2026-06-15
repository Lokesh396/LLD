"""
The Observer Design Pattern is a behavioral pattern that defines a one-to-many dependency between objects so that when one object (the subject) changes its state, all its dependents (observers) are automatically notified and updated.


The Observer Design Pattern provides a clean and flexible solution to the problem of broadcasting changes from one central object (the Subject) to many dependent objects (the Observers) all while keeping them loosely coupled.
"""

from abc import ABC, abstractmethod

class StockObserver(ABC):
    @abstractmethod
    def on_price_update(self, exchange):
        pass

class StockExchange:
    def __init__(self):
        self._prices = {}
        self._observers = []
        self._last_updated_symbol = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify_observers(self):
        for observer in list(self._observers):
            observer.on_price_update(self)

    def update_price(self, symbol, price):
        self._prices[symbol] = price
        self._last_updated_symbol = symbol
        print(f"\nExchange: {symbol} updated to ${price}")
        self._notify_observers()

    def get_price(self, symbol):
        return self._prices.get(symbol, 0.0)

    def get_last_updated_symbol(self):
        return self._last_updated_symbol

class PriceDisplay(StockObserver):
    def on_price_update(self, exchange):
        symbol = exchange.get_last_updated_symbol()
        print(f"Display -> {symbol}: ${exchange.get_price(symbol)}")

class AlertService(StockObserver):
    def __init__(self):
        self._thresholds = {}

    def set_alert(self, symbol, threshold):
        self._thresholds[symbol] = threshold

    def on_price_update(self, exchange):
        symbol = exchange.get_last_updated_symbol()
        if symbol in self._thresholds:
            threshold = self._thresholds[symbol]
            price = exchange.get_price(symbol)
            if price >= threshold:
                print(f"ALERT -> {symbol} hit ${price} (threshold: ${threshold})")

class TradingBot(StockObserver):
    def __init__(self):
        self._previous_prices = {}

    def on_price_update(self, exchange):
        symbol = exchange.get_last_updated_symbol()
        current_price = exchange.get_price(symbol)
        previous_price = self._previous_prices.get(symbol, current_price)

        if current_price > previous_price:
            print(f"Bot -> {symbol} rising (${previous_price} -> ${current_price}). HOLD.")
        elif current_price < previous_price:
            print(f"Bot -> {symbol} dropping (${previous_price} -> ${current_price}). BUY.")

        self._previous_prices[symbol] = current_price

# Client code
exchange = StockExchange()

display = PriceDisplay()
alerts = AlertService()
bot = TradingBot()

exchange.register_observer(display)
exchange.register_observer(alerts)
exchange.register_observer(bot)

alerts.set_alert("AAPL", 180.0)
alerts.set_alert("GOOG", 140.0)

exchange.update_price("AAPL", 175.50)
exchange.update_price("GOOG", 138.25)
exchange.update_price("AAPL", 182.00)
exchange.update_price("GOOG", 141.75)