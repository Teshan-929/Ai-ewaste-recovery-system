def calculate_net_value(
    estimated_resale_value,
    extraction_cost,
    testing_cost,
    shipping_cost
):
    return (
        estimated_resale_value
        - extraction_cost
        - testing_cost
        - shipping_cost
    )


def make_decision(net_recovery_value, scrap_value):

    if net_recovery_value > scrap_value:
        return "RECOVER"
    else:
        return "RECYCLE"