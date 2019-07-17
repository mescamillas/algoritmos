'''
A simple algorithm showing how diversification and rebalancing
can make dramatic improvements to volatility and returns.
Note that this trades in 3X leveraged ETFs to get increased returns.
The diversification however, keeps the volatility in check.
'''

def initialize(context):
    """
    Called once at the start of the algorithm.
    """   
    
    # Here are any algorithm 'constants' we'll be using
    context.target_leverage = 1.0
    
    # Here are the ETFs we want to trade along with the weights 
    # Ensure they add to 1.00
    context.etfs = {
        symbol('TYD'): 0.1, # Daily 7-10 Year Treasury Bull 3X Shares
        symbol('TMF'): 0.1, # Daily 20+ Year Treasury Bull 3X Shares
        symbol('EDZ'): 0.1, # Daily MSCI Emerging Markets Bear 3X Shares
        symbol('SPXL'): 0.1, # Daily S&P 500 Bull 3X Shares
        symbol('ADBE'): 0.1, # ADOBE inc.
        symbol('AU'): 0.1, # AngloGold Ashanti
        symbol('BP'): 0.1, #BP
        symbol('EA'): 0.1, # Electronic Arts
        symbol('XRX'): 0.1, # Xerox
        symbol('IBM'): 0.1 # IBM
    }
    
    # Set commision model for Robinhood
    set_commission(commission.PerShare(cost=0.2, min_trade_cost=0.0))
 
    # Rebalance our portfolio to maintain target weights
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open(minutes = 35))


def rebalance(context, data):
    for stock, weight in context.etfs.items():
        order_target_percent(stock, weight*context.target_leverage)
