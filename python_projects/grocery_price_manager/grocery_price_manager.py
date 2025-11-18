# Grocery Price Manager - student style
def show_prices(prices):
    print("\nPrices:")
    for i, p in enumerate(prices, 1):
        print(f"{i}. R{p:.2f}")

def calculate_total(prices):
    return sum(prices)

def find_highest(prices):
    return max(prices)

def apply_discount(prices, discount_percent):
    factor = (100 - discount_percent) / 100.0
    return [round(p * factor, 2) for p in prices]

def main():
    prices = []
    print("Enter prices for at least 5 grocery items:")
    while len(prices) < 5:
        try:
            val = float(input(f"Price {len(prices)+1}: R"))
            if val < 0:
                print("Price cannot be negative.")
                continue
            prices.append(val)
        except ValueError:
            print("Enter a valid number.")
    while True:
        print("\nMenu:")
        print("1. Show all prices")
        print("2. Calculate total cost")
        print("3. Find highest price")
        print("4. Apply discount to all prices")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == '1':
            show_prices(prices)
        elif choice == '2':
            print(f"Total: R{calculate_total(prices):.2f}")
        elif choice == '3':
            print(f"Highest price: R{find_highest(prices):.2f}")
        elif choice == '4':
            try:
                d = float(input("Discount percent (0-100): "))
                if d < 0 or d > 100:
                    print("Invalid percent.")
                    continue
                prices = apply_discount(prices, d)
                print("Discount applied.")
            except ValueError:
                print("Enter a number.")
        elif choice == '5':
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
