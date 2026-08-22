def calculate_net_value(market_value, extraction_cost, shipping_cost):
    return market_value - extraction_cost - shipping_cost


def make_decision(net_value):
    if net_value > 10:
        return "RECOVER"
    else:
        return "RECYCLE"