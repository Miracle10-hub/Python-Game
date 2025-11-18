# Temperature Analysis - student style
def calculate_average(temps):
    return sum(temps) / len(temps)
def find_highest(temps):
    return max(temps)
def find_lowest(temps):
    return min(temps)
def sort_descending(temps):
    return sorted(temps, reverse=True)
def main():
    while True:
        try:
            n = int(input('Enter number of days (1-30): '))
            if 1 <= n <= 30:
                break
            print('Number between 1 and 30.')
        except ValueError:
            print('Enter an integer.')
    temps = []
    i = 1
    while i <= n:
        try:
            t = float(input(f'Day {i} temp (-50 to 50): '))
            if -50 <= t <= 50:
                temps.append(t)
                i += 1
            else:
                print('Value out of range.')
        except ValueError:
            print('Enter a number.')
    print('Average:', calculate_average(temps))
    print('Highest:', find_highest(temps))
    print('Lowest:', find_lowest(temps))
    print('Sorted descending:', sort_descending(temps))
if __name__ == '__main__':
    main()
