#split bill calc

def main():
  
    print("Welcome to split the bill calc ")
    total_bill = float(input("What was the total bill "))
    total_people = int(input("How many people to split the bill?"))
    tip = int(input("What percentage tip would you like to give?"))
    each_person_bill = ((total_bill + total_bill*(tip/100)) / total_people)
    print(f"Bill for each of you is {each_person_bill:.2f}")


if __name__ == '__main__':
    main()
