def cost_to_carry(spot_price, risk_free_rate = 0.04, storage_cost = 0.01, time = 1):
    future_price = spot_price * np.exp((risk_free_rate + storage_cost) * time)
    return print(f"The future price of the coffee price as per the cost to carry model is: ${future_price:.3f} per pound.")

def black_scholes_call_price(spot_price, strike_price, risk_free_rate, time, volatility):
    d1 = (np.log(spot_price / strike_price) + (risk_free_rate + 0.5 * volatility ** 2) * time) / (volatility * np.sqrt(time))
    d2 = d1 - volatility * np.sqrt(time)
    call_price = spot_price * norm.cdf(d1) - strike_price * np.exp(-risk_free_rate * time) * norm.cdf(d2)
    return print(f"The price of the call option is: ${call_price:.3f}")

def monte_carlo_simulation(spot_price, risk_free_rate, time, volatility, num_simulations = 100000, num_steps = 252):
    dt = time / num_steps
    price_paths = np.zeros((num_steps, num_simulations))
    price_paths[0] = spot_price

    np.random.seed(53)
    for i in range(1, num_steps):
        z = np.random.standard_normal(num_simulations)
        price_paths[i] = price_paths[i-1] * np.exp((risk_free_rate - 0.5 * volatility ** 2) * dt + volatility * np.sqrt(dt) * z)

    average_simulated_price = np.mean(price_paths[-1])
    return print(f"The average simulated price of the coffee futures contract at maturity is: ${average_simulated_price:.3f}.")