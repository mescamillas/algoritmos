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
        symbol('AAPL'): 0.1, #Apple Inc.
        symbol('PG'): 0.1, #Procter and Gamble co.
        symbol('CMCS_A'): 0.1, # Comcast Co.
        symbol('SDOW'): 0.1, # UltraPro Short Dow 30 ETF
        symbol('UDOW'):0.1, #  UltraPro Dow 30 ETF
        symbol('SOXL'):0.1, # Direxion Daily Semiconductor Bull 3x Shares ETF
    }
    
    # Set commision model for Robinhood
    set_commission(commission.PerShare(cost=0.2, min_trade_cost=0.0))
 
    # Rebalance our portfolio to maintain target weights
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open(minutes = 35))


def rebalance(context, data):
    for stock, weight in context.etfs.items():
        order_target_percent(stock, weight*context.target_leverage)
