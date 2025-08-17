"""
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and
they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example. m = 6 cost = [1, 3, 4, 5, 6]

The two flavors that cost 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.
"""


def create_dicctionary(prices):
    position = 1
    dict_prices = {}
    for price in prices:
        if price in dict_prices:
            dict_prices[price] = [dict_prices[price], position]
        else:
            dict_prices[price] = position
        position += 1
    return dict_prices


def icecreamParlor2(money, prices):
    dict_prices = create_dicctionary(prices)
    for price in prices:
        target = money - price
        if target in dict_prices.keys():
            if isinstance(dict_prices[target], list):
                return dict_prices[target]
            else:
                return dict_prices[price], dict_prices[target]
    pass


def icecreamParlor(money, prices):
    seen_prices = {}
    for i, price in enumerate(prices):
        target = money - price
        if target in seen_prices:
            return [seen_prices[target], i + 1]
        seen_prices[price] = i + 1