import json as J
import random as R

class LuckySeat:
    
    def __init__(self):
        self.file = 'periods.json'

    # Is _custom_builtin_ a good naming convention??
    def assert__(self, condition, error, func): #success = None#):
        '''
        DESC: A custom `assert` function which takes multiple parameters to avoid the repetitive try-assert-except structure from v0.1.
        ARGS: condition (condition to assert), error (error message to print), func (function to re-run)
        RTNS: NONE
        '''
        try:
            assert condition
            # print(success)
        except AssertionError:
            print(error)
            func()

    def does_seat_exist(self):
        existing_seat_chart = input("\nUse seating chart of existing period? (y/n):    ").lower()
        self.assert__(existing_seat_chart in ['y','n'], '\nPlease enter either `y` or `n`\n...Rerunning\n', self.does_seat_exist)
        return existing_seat_chart

    def seat_exists(self):
        '''
        DESC: If the user is using an existing seating chart, this will ask the period number and make sure that it is an integer between 1-7.
        ARGS: NONE
        RTNS: NONE
        '''
        try:
            period_number = int(input("\nPeriod # (number input):    "))
            
            self.period_number = period_number
            self.read_m()

            self.tables = self.periods_dict[self.period_number-1]["tables"]
            self.per_table = self.periods_dict[self.period_number-1]["per_table"]
        except ValueError:
            print('\nPlease make sure your value is a number!\n...Rerunning')
            self.seat_exists()
        self.assert__(self.period_number in [1,2,3,4,5,6,7], '\nPlease make sure your period number is between 1 to 7!`\n...Rerunning\n', self.seat_exists)

    def seat_no_exists(self):
        '''
        DESC: If the user is using an existing seating chart, this will ask the period number and make sure that it is an integer between 1-7.
        ARGS: NONE
        RTNS: NONE
        '''
        try:
            tables = int(input("\nNumber of tables? (number input):    "))
            self.tables = tables
            per_table = int(input("\nStudents per table? (number input):    "))
            self.per_table = per_table
        except ValueError:
            print('\nPlease make sure your value is a number!\n...Rerunning')
            self.seat_no_exists()
        # better use of the per_table
        self.assert__(self.tables and self.per_table in [1,2,3,4,5,6,7], '\nPlease make sure your period number is between 1 to 7!`\n...Rerunning\n', self.seat_no_exists)

    def randomly_select(self):
        
        returnlist = []
        tick = 1
        # Period number:tables*4 (all students)

        # this part is a bit confusing uh ill work on it
        while tick <= self.tables*self.per_table:
            returnlist.append(R.randint(tick, tick+(self.per_table-1)))
            tick+=self.per_table
        
        print(f"\n{returnlist}")


    def read_m(self):
        with open(self.file, 'r') as jsonfile:
            self.periods_dict = J.load(jsonfile)

    def write_m(self):
        with open(self.file, 'w') as jsonfile2:
            J.dump(self.periods_dict, jsonfile2)

    # def save_config(self):

    #     try:
    #         ask_save_config = input("\nSave configuration? (y/n):    ").lower()

    #         if ask_save_config == 'n':
    #             exit()
    #         else:
    #             self.write_m()
            
    #         ask_period_num = int(input("\nPeriod number to assign to?    "))
            
            
    #     except ValueError:
    #         self.assert__(ask_save_config in ['y','n'] and (ask_period_num in [1,2,3,4,5,6,7]), '\nPlease enter either `y` or `n`\n...Rerunning\n', self.save_config)

    def save_config(self):
        try:
            ask_save_config = input("\nSave configuration? (y/n):    ").lower()

            if ask_save_config not in ['y', 'n']:
                print("Invalid input! Please enter `y` or `n`.")
                self.save_config()  # Retry if invalid input

            if ask_save_config == 'n':
                exit()

            # Read period number and validate
            ask_period_num = input("\nPeriod number to assign to?    ")

            if not ask_period_num.isdigit():
                print("Please make sure your input is a number!")
                self.save_config()  # Retry if invalid input

            ask_period_num = int(ask_period_num)

            if ask_period_num not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid period number! It should be between 1 and 7.")
                self.save_config()  # Retry if invalid input

            # If all inputs are valid, proceed with saving
            self.periods_dict[ask_period_num - 1] = {"tables": self.tables, "per_table": self.per_table}
            self.write_m()
            print(f"Configuration saved for period {ask_period_num}.")

        except ValueError:
            print("Invalid input! Please make sure your input is a number.")
            self.save_config()  # Retry if invalid input


        
    def main(self):

        if self.does_seat_exist() == 'y':

            self.seat_exists()
            self.randomly_select()
            
        else:
            
            self.seat_no_exists()
            self.randomly_select()
            self.save_config()

if __name__ == '__main__':
    lucky = LuckySeat()
    lucky.main()