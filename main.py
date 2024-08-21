import json as J
import random as R

class SeatPicker:
    
    def __init__(self):
        pass

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
            self.period_num_getter()
        # better use of the per_table
        self.assert__(self.period_number and self.per_table in [1,2,3,4,5,6,7], '\nPlease make sure your period number is between 1 to 7!`\n...Rerunning\n', self.seat_exists)

    def randomly_select(self):
        
        returnlist = []
        tick = 1
        # Period number:tables*4 (all students)
        while tick <= self.periods_dict[self.period_number-1]["tables"]*4:
            returnlist.append(R.randint(tick, tick+3))
            tick+=4
        
        print(f"\n{returnlist}\n")

        exit()
    

    def main(self):

        if self.does_seat_exist() == 'y':

            self.seat_exists()
            with open("periods.json", 'r') as jsonfile:
                self.periods_dict = J.load(jsonfile)
            self.randomly_select()
            
        else:
            pass
            



seat = SeatPicker()
seat.main()


# def run():
#     q1 = input("Use seating chart of existing period? (y/n):    ").lower()
#     # q5 = input("Enter missing student numbers, press ENTER if none:  ")

#             elif q1 == 'n':

#                 def q1_n():
#                     try:

#                         q2 = input("# of Tables?    ")
                        

#                         assert type(q2) == int
#                         global unsaved_tables
#                         unsaved_tables = int(q2)
                        
#                         returnlist_n = []
#                         tick = 1
#                         while tick <= unsaved_tables*4:
#                             returnlist_n.append(R.randint(tick, tick+3))
#                             tick+=4
                        
#                     except ValueError:
#                         print(f"Must be a number of tables!!\n\n ...rerunning\n")
#                         q1_n()

#                     except AssertionError:
#                         pass

#                     print(returnlist_n)

#                 q1_n()
#                 def default():
#                     q3 = input("Save as default? (y/n):    ")

#                     try:
#                         assert q3 in ['y', 'n']
#                         if q3 == 'y':

#                             def q3_y():
#                                 q4 = input("Period number to assign to?    ")
#                                 try:
#                                     assert int(q4) in [1, 2, 3, 4, 5, 6, 7]
                                    
#                                     with open("periods.json", 'r') as jsonfile:
#                                         pd_dict = J.load(jsonfile)

#                                     pd_dict[int(q4)-1]['tables'] = unsaved_tables
                                    
#                                     with open('periods.json', 'w') as jsonfile2:
#                                         J.dump(pd_dict,jsonfile2)
                                    
#                                     print(f"Saved new tables config to period {int(q4)}.")
#                                     exit()

                                    


#                                 except AssertionError:
#                                     print("Not a valid period number!!\n\n ...rerunning\n")
#                                     q1_n()

#                             q3_y()

#                         elif q3 == 'n':
#                             print("Not saved new tables as default for any period...")
#                             exit()

#                     except AssertionError:
#                         print("Enter vaid input!\n\n ...rerunning\n")
#                         default()
#                 default()

#         except AssertionError:
#             print("Enter vaid input!\n\n ...rerunning\n")
#             run()
#     thing()

# run()


