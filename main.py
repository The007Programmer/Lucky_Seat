import json as J
import random as R

def run():
    q1 = input("Use seating chart of existing period? (y/n):    ").lower()
    # q5 = input("Enter missing student numbers, press ENTER if none:  ")
    def thing():
        try:
            assert q1 in ['y', 'n']
            if q1 == 'y':
                def q1_y():
                    def_period_q = input("Period # (number input):    ")
                    try:
                        assert int(def_period_q) in [1, 2, 3, 4, 5, 6, 7]
                        # Load original datafile for json dicts
                        
                        with open("periods.json", 'r') as jsonfile:
                            pd_dict = J.load(jsonfile)
                        
                        returnlist_y = []
                        tick = 1
                        while tick <= pd_dict[int(def_period_q)-1]["tables"]*4:
                            returnlist_y.append(R.randint(tick, tick+3))
                            tick+=4
            
                    except AssertionError:
                        print("Enter vaid input!\n\n ...rerunning\n")
                        q1_y()

                    print(returnlist_y)
                    exit()

                q1_y()

            elif q1 == 'n':

                def q1_n():
                    try:

                        q2 = input("# of Tables?    ")
                        

                        assert type(q2) == int
                        global unsaved_tables
                        unsaved_tables = int(q2)
                        
                        returnlist_n = []
                        tick = 1
                        while tick <= unsaved_tables*4:
                            returnlist_n.append(R.randint(tick, tick+3))
                            tick+=4
                        
                    except ValueError:
                        print(f"Must be a number of tables!!\n\n ...rerunning\n")
                        q1_n()

                    except AssertionError:
                        pass

                    print(returnlist_n)

                q1_n()
                def default():
                    q3 = input("Save as default? (y/n):    ")

                    try:
                        assert q3 in ['y', 'n']
                        if q3 == 'y':

                            def q3_y():
                                q4 = input("Period number to assign to?    ")
                                try:
                                    assert int(q4) in [1, 2, 3, 4, 5, 6, 7]
                                    
                                    with open("periods.json", 'r') as jsonfile:
                                        pd_dict = J.load(jsonfile)

                                    pd_dict[int(q4)-1]['tables'] = unsaved_tables
                                    
                                    with open('periods.json', 'w') as jsonfile2:
                                        J.dump(pd_dict,jsonfile2)
                                    
                                    print(f"Saved new tables config to period {int(q4)}.")
                                    exit()

                                    


                                except AssertionError:
                                    print("Not a valid period number!!\n\n ...rerunning\n")
                                    q1_n()

                            q3_y()

                        elif q3 == 'n':
                            print("Not saved new tables as default for any period...")
                            exit()

                    except AssertionError:
                        print("Enter vaid input!\n\n ...rerunning\n")
                        default()
                default()

        except AssertionError:
            print("Enter vaid input!\n\n ...rerunning\n")
            run()
    thing()

run()