# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3500,
    "MSFT": 300
}

def get_user_portfolio():
    portfolio = {}
    print("Enter your stock holdings (type 'done' to finish):")
    while True:
        stock = input("Stock symbol: ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print(f"Stock '{stock}' is not in the available price list.")
            continue
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Please enter a valid integer for quantity.")
    return portfolio

def calculate_portfolio_value(portfolio):
    total_value = 0
    print("\n--- Portfolio Summary ---")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        print(f"{stock}: {quantity} shares × ${price} = ${value}")
        total_value += value
    print(f"\nTotal Portfolio Value: ${total_value}")

# Run the program
if __name__ == "__main__":
    portfolio = get_user_portfolio()
    calculate_portfolio_value(portfolio)

