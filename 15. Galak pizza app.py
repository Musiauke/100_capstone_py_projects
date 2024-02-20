
def main():
    
    total_bill = 0

    print("Thank you for choosing Galak Pizza!")
    
    size = input("What's the size you would like to eat? (S,M or L)").upper()
    add_pepperoni = input("Would you like to have extra pepperoni? (Y or N)").upper()
    extra_cheese = input("Would you like to have extra cheese? (Y or N)").upper()

    if size == 'S':
        total_bill += 15
    elif size == 'M':
        total_bill += 20
    elif size == 'L':
        total_bill += 25
    else:
        print("Incorrect input")

    if add_pepperoni == 'Y' and size == 'S':
        total_bill += 2
    elif add_pepperoni == 'Y' and size  in ('M', 'L'):
        total_bill += 3
    else:
        pass

    if extra_cheese == 'Y':
        total_bill += 1

    print(f"Thank you for choosing Galak Pizza! Your final bill is:{total_bill}zł")

if __name__ == "__main__":
    main()
