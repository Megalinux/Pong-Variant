### Pong-Variant
Relive a classic. Here is a short implementation of the Atari game Pong in Python with the help of PyGame.

### Features ###

* **Backtesting** of your strategies with Ta-lib and Qtpylib trading libraries
* Use of static and dynamic **stoploss**. Create your dinamyc stoploss formula.
* **Visualization** of the strategy progress and result with matplotblib
* Configuration of a set of **parameters**
* Calculation of a strategy **value**
* **Log** support of all operations
* Support of CryptoCurrency eXchange Trading Library [CCXT](https://github.com/ccxt/ccxt)

### Run ###

1. Configure strategy and parameters on strategy.py with text editor as already described
2. In terminal/cmd go to Your main Backtester's folder.
3. Run BacktestTool by command: python3 backtester_v1 {exchange} {pair}
    Example of run backtester:

    * `python3 backtester_v1 poloniex 'ATOM/BTC'`
    * `python3 backtester_v1 poloniex 'DOGE/BTC'`
    * `python3 backtester_v1 poloniex 'ETH/BTC'` 
    * `python3 backtester_v1 binance 'ETC/BTC'` 


### Requirements ###

* Python >=3.4
* Talib
* Matplotlib
* Requests
* Numpy
* Pandas
* Json
* Logging
* Ccxt

### Support ###

For any questions not covered by the documentation or for further information about the backtester, we encourage you to send an email to webmaster@megalinux.it

### Bugs / Issues ###

If you discover a bug in the bot, please search [our issue tracker first](https://github.com/Megalinux/Crypto_1_Backtester/issues?q=is%3Aissue) . If it hasn't been reported, please [create a new issue](https://github.com/Megalinux/Crypto_1_Backtester/issues/new) and ensure you follow the template guide so that our team can assist you as quickly as possible.
Feature Requests

Have you a great idea to improve the bot you want to share? Please, first search if this feature was not already discussed. If it hasn't been requested, please create a new request!

### License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2019 © Grando Ruggero.
