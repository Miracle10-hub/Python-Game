# SuperMart Shopping Management System - student style
import math
transactions = []

def calc_discount(amount):
    if amount >= 5000: return 20
    if amount >= 3000: return 15
    if amount >= 1000: return 10
    if amount >= 500: return 5
    return 0

def final_amount(amount, delivery_choice):
    discount = calc_discount(amount)
    discounted = amount * (100 - discount) / 100.0
    delivery = 0 if discounted >= 3000 else (150 if delivery_choice else 0)
    final = discounted + delivery
    points = int(discounted // 100)
    return discount, discounted, delivery, final, points

def save_report():
    with open('shopping_report.txt','w') as f:
        for t in transactions:
            f.write(str(t) + '\n')
    print('Report saved to shopping_report.txt')

def main():
    while True:
        print('\nMenu:')
        print('1. View Discount Rules')
        print('2. Enter Shopping Bill & Calculate Final Amount')
        print('3. View All Transactions (History)')
        print('4. Compare Two Shopping Bills')
        print('5. Save Report to File')
        print('6. Exit')
        choice = input('Choose: ')
        if choice == '1':
            print('>= R5000 -> 20%\nR3000-4999 -> 15%\nR1000-2999 -> 10%\nR500-999 -> 5%\n< R500 -> 0%')
        elif choice == '2':
            try:
                amt = float(input('Enter shopping bill (before discounts): R'))
            except ValueError:
                print('Invalid number.')
                continue
            dchoice = input('Delivery (yes/no): ').lower().startswith('y')
            discount, discounted, delivery, final, points = final_amount(amt, dchoice)
            rec = {'before': amt, 'discount%': discount, 'after_discount': round(discounted,2), 'delivery': delivery, 'final': round(final,2), 'points': points}
            transactions.append(rec)
            print('Final:', rec)
        elif choice == '3':
            for i,t in enumerate(transactions,1):
                print(i, t)
        elif choice == '4':
            try:
                a = float(input('Bill A: R'))
                b = float(input('Bill B: R'))
            except ValueError:
                print('Invalid input.')
                continue
            da = calc_discount(a); db = calc_discount(b)
            _, ad, delA, finalA, pa = final_amount(a, False)
            _, bd, delB, finalB, pb = final_amount(b, False)
            print('A discount', da, 'B discount', db)
            print('A final', finalA, 'B final', finalB)
            print('A points', pa, 'B points', pb)
        elif choice == '5':
            save_report()
        elif choice == '6':
            break
        else:
            print('Invalid choice.')
    print('Goodbye.')

if __name__ == '__main__':
    main()
