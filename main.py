import json as J
import random as R
import tkinter as T
from tkinter import ttk as TT
import os as O
import time as TI

def filepath():
    '''
    DESC: Creates the JSON file to store data if it does not already exist in the runtime directory.
    ARGS: NONE
    RTNS: str: Path to the JSON file.
    '''
    # Get the directory where the script is located
    script_directory = O.path.dirname(O.path.abspath(__file__))
    json_filename = O.path.join(script_directory, 'periods.json')

    # Check if the file already exists
    if not O.path.exists(json_filename):
        # Data to write into JSON file on first run
        data = [
            {"tables": 0, "per_table": 0} for _ in range(7)
        ]
        # Write the data to the JSON file
        with open(json_filename, 'w') as json_file:
            J.dump(data, json_file, indent=4)

        print(f"JSON file '{json_filename}' created in the runtime folder.")
        
        # Ensure the file is fully written before proceeding
        TI.sleep(1)

    else:
        print(f"JSON file '{json_filename}' already exists in the runtime folder.")
    
    return json_filename

class LuckySeat:
    '''
    A class to manage seating arrangements and configurations.
    '''
    
    def __init__(self):
        self.file = filepath()  # Use filepath function to get the JSON file path

        # Wait until the JSON file is available
        while not O.path.exists(self.file):
            print(f"Waiting for the JSON file '{self.file}' to be available...")
            TI.sleep(0.5)  # Small delay before retrying

        with open(self.file, 'r') as jsonfile_init:
            self.periods_dict = J.load(jsonfile_init)


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

    def doesSeatExist(self):
        existing_seat_chart = input("\nUse seating chart of existing period? (y/n):    ").lower()
        self.assert__(existing_seat_chart in ['y','n'], '\nPlease enter either `y` or `n`\n...Rerunning\n', self.main)
        return existing_seat_chart

    def seatExists(self):
        '''
        DESC: If the user is using an existing seating chart, this will ask the period number and make sure that it is an integer between 1-7.
        ARGS: NONE
        RTNS: NONE
        '''
        try:
            period_number = int(input("\nPeriod # (number input):    "))
            
            self.period_number = period_number
            with open(self.file, 'r') as jsonfile:
                self.periods_dict = J.load(jsonfile)

            self.tables = self.periods_dict[self.period_number-1]["tables"]
            self.per_table = self.periods_dict[self.period_number-1]["per_table"]

        except ValueError:
            print('\nPlease make sure your value is a number!\n...Rerunning')
            self.seatExists()

        except IndexError:
            print(f"The specified period doesn't have the number of tables you entered!\n...Rerunning")
            self.seatExists()

        self.assert__(self.period_number in [1,2,3,4,5,6,7], '\nPlease make sure your period number is between 1 to 7!`\n...Rerunning\n', self.seatExists)

    def seatNoExists(self):
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
            self.seatNoExists()

        # better use of the per_table
        self.assert__(self.tables and self.per_table in [1,2,3,4,5,6,7], '\nPlease make sure your period number is between 1 to 7!`\n...Rerunning\n', self.seatNoExists)

    def randomlySelect(self):
        '''
        DESC: Uses the inputs to create the randomly picked students for each table and returns it.
        ARGS: NONE
        RTNS: ~~~
        '''
        returnlist = []
        tick = 1
        # Period number:tables*4 (all students)

        # this part is a bit confusing uh ill work on it
        while tick <= self.tables*self.per_table:
            returnlist.append(R.randint(tick, tick+(self.per_table-1)))
            tick+=self.per_table
        
        # global returnlist_i
        # returnlist_i = iter(returnlist)
        print(f"\n{returnlist}")

    def saveConfig(self):
        try:
            ask_save_config = input("\nSave table configuration? (y/n):    ").lower()
            self.assert__(ask_save_config in ['y', 'n'], '\nPlease enter either `y` or `n`\n...Rerunning\n', self.saveConfig)

            if ask_save_config == 'n':
                exit()
            else:
                ask_period_num = int(input("\nPeriod number to assign to?    "))
                self.assert__(1 <= ask_period_num <= 7, '\nPeriod number must be between 1 and 7.\n...Rerunning\n', self.saveConfig)

                # Update the periods_dict with the new configuration
                self.periods_dict[ask_period_num - 1] = {
                    "tables": self.tables,
                    "per_table": self.per_table
                }

                # Save the updated dictionary back to the file
                with open(self.file, 'w') as jsonfile2:
                    J.dump(self.periods_dict, jsonfile2, indent=4)  # indent for readability
                print(f"\nConfiguration saved for period {ask_period_num}.")

        except ValueError:
            print("\nPlease enter a valid number.\n...Rerunning\n")
            self.saveConfig()
        
    def main(self):

        if self.doesSeatExist() == 'y':

            self.seatExists()
            self.randomlySelect()
            
        else:
            
            self.seatNoExists()
            self.randomlySelect()
            self.saveConfig()


if __name__ == '__main__':
    filepath()
    lucky = LuckySeat()
    lucky.main()