
def compound_interest(principal, rate, time):
    future_value = principal * (1 + rate) ** time
    return future_value


def simple_interest(principal, rate, time):
    future_value = principal + (principal * rate * time)
    return future_value
