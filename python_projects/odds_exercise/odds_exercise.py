# Odd and Even Collector - student style
def is_even(n):
    return n % 2 == 0

def main():
    while True:
        try:
            n = int(input("Enter a number n (>=2): "))
            if n >= 2:
                break
            print("Please enter 2 or more.")
        except ValueError:
            print("Enter a valid integer.")
    odds = []
    evens = []
    i = 2
    while i <= n:
        try:
            val = int(input(f"Enter number {i}: "))
        except ValueError:
            print("Enter an integer.")
            continue
        if is_even(val):
            evens.append(val)
        else:
            odds.append(val)
        i += 1
    print("\nOdd numbers:", ' '.join(map(str, odds)))
    print("Even numbers:", ' '.join(map(str, evens)))

if __name__ == '__main__':
    main()
