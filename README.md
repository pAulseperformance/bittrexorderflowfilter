# Bittrex Orderflow Filter
### The purpose of this script is to help identify key levels of accumulated buy/sell orders on the Bittrex orderbook.
Large bids will be printed to the terminal every 5 seconds separated by the current price and large asks on top.
The output is meant to be concise and minimal in order to quickly assess the state of the market.
```
________________MOON___________________

Price: 0.48179865                Amount: 51413.0
Price: 0.48237931                Amount: 13282.9813236
Price: 0.48334456                Amount: 13282.9813236
Price: 0.48399998                Amount: 61331.0
Price: 0.48968526                Amount: 23359.46136


LASTPRICE:0.47889998


Price: 0.47889998                Amount: 24899.3201939
Price: 0.47667973                Amount: 46514.0
Price: 0.47667972                Amount: 61331.0
Price: 0.4701105                Amount: 35805.9082155
Price: 0.47011                Amount: 49720.9541603
Price: 0.4695                Amount: 42492.3771021
Price: 0.46943459                Amount: 52995.1189405
Price: 0.46833741                Amount: 61331.0
Price: 0.465                Amount: 25004.9734875
Price: 0.46187057                Amount: 61331.0

_______________FLOOR__________________
```

## Setup
1. Clone this repository ```git clone https://github.com/GrilledChickenThighs/bittrexorderflowfilter.git ```
2. Install Dependencies ``pip install python-bittrex``
3. Run ```python2 main.py```

## To Do
 * Add support for user input
 * Abstract Modularize Functions
 * Round Decimal Outputs

## Future Features
* Graphical Display With Automated Level Plotting
* Automated Strategic Level Indicator/Alert (Will require back testing and statistical analysis to support profitability)
* Your Contributions
