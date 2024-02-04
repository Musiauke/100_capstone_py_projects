class MortgageCalculator:
    def __init__(self):
        self.credited_cash = None
        self.input_cash = None
        self.interest_rate = None
        self.duration = None
        self.compounding = {'Monthly':12, 'Weekly':52, 'Daily':36, 'Continually': -1}
#compounding  
    def get_user_input(self):
        self.credited_cash = self.get_numeric_input('Hey how much you want to get: ', float)
        self.input_cash = self.get_numeric_input('What is your input? ', float)
        self.duration = self.get_numeric_input('For how long? In months: ', int)
        self.calculate_interest_rate()

    def get_numeric_input(self, message, value_type):
        while True:
            try:
                return value_type(input(message))
            except ValueError:
                print('Incorrect input! ')

    def calculate_interest_rate(self):
        if self.duration < 60:
            self.interest_rate = 8/100
        else:  
            self.interest_rate = 5/100 


    def calculate_payments(self, compounding_type='Monthly'):
        
        n = self.compounding[compounding_type]if compounding_type in self.compounding else 12 

        if n != -1:
            r = (1 + self.interest_rate / n) ** n - 1
        else:  # Continual compounding
            r = self.interest_rate * self.duration / 12

        loan_amount = self.credited_cash - self.input_cash
        if n != -1:
            # Calculate monthly payment based on standard formula
            monthly_payment = loan_amount * (r * (1 + r) ** self.duration) / ((1 + r) ** self.duration - 1)
        else:  # Continual compounding
            monthly_payment = loan_amount * r / self.duration

        print(f'Monthly payment: {monthly_payment:.2f}')

    #main loop
        
if __name__ == '__main__':

    calculator = MortgageCalculator()
    
    while True:
        calculator.get_user_input()
        calculator.calculate_payments()
            
        if input("Calculate again? (y/n): ").lower() != 'y':
            break
