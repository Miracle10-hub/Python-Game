# Smart Home Device Manager - student style
def read_float(prompt):
    while True:
        try:
            v = float(input(prompt))
            if v < 0:
                print("Value cannot be negative.")
                continue
            return v
        except ValueError:
            print("Enter a number.")

def main():
    while True:
        try:
            n = int(input("Enter number of devices (>=1): "))
            if n >= 1:
                break
            print("Must be at least 1.")
        except ValueError:
            print("Enter an integer.")
    devices = []
    for i in range(n):
        name = input(f"Name of device {i+1}: ").strip() or f"Device{i+1}"
        usage = []
        print(f"Enter 7 daily kWh for {name}:")
        day = 1
        while day <= 7:
            v = read_float(f"Day {day}: ")
            usage.append(v)
            day += 1
        devices.append({'name': name, 'usage': usage})
    def total_week(u): return sum(u)
    while True:
        print("\nMenu:")
        print("1. Add daily usage for a device (replace)")
        print("2. View daily usage for a device")
        print("3. View total and average usage for a device")
        print("4. Find device(s) with highest total usage")
        print("5. Find device(s) with lowest total usage")
        print("6. Exit")
        choice = input("Choose: ")
        if choice == '1':
            try:
                idx = int(input("Device number: ")) - 1
            except ValueError:
                print("Enter a number."); continue
            if 0 <= idx < len(devices):
                print(f"Enter 7 daily kWh for {devices[idx]['name']}:")
                devices[idx]['usage'] = [read_float(f"Day {d}: ") for d in range(1,8)]
            else:
                print("Invalid device number.")
        elif choice == '2':
            try:
                idx = int(input("Device number: ")) - 1
            except ValueError:
                print("Enter a number."); continue
            if 0 <= idx < len(devices):
                print(devices[idx]['usage'])
            else:
                print("Invalid device number.")
        elif choice == '3':
            try:
                idx = int(input("Device number: ")) - 1
            except ValueError:
                print("Enter a number."); continue
            if 0 <= idx < len(devices):
                tot = total_week(devices[idx]['usage'])
                avg = tot / 7.0
                print(f"Total: {tot:.2f} kWh, Average: {avg:.2f} kWh/day")
            else:
                print("Invalid device number.")
        elif choice == '4':
            totals = [total_week(d['usage']) for d in devices]
            mx = max(totals)
            print("Highest total usage devices:")
            for i,d in enumerate(devices):
                if totals[i] == mx:
                    print(d['name'], mx)
        elif choice == '5':
            totals = [total_week(d['usage']) for d in devices]
            mn = min(totals)
            print("Lowest total usage devices:")
            for i,d in enumerate(devices):
                if totals[i] == mn:
                    print(d['name'], mn)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")
    print("Goodbye.")

if __name__ == '__main__':
    main()
