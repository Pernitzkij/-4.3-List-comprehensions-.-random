original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

prices_reddit = [(x if x > 0 else 0) for x in original_prices]

print(prices_reddit)
