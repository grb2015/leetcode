# -*- coding: utf-8 -*-
###########################################################################################
#   breif   :  console application  that adds alerts for temperature values from console input 
#   history :  renbin Guo created 20200116_0900
#   detail  :   Design and implement a console application in any program language that adds alerts for temperature values from console input. The application should,
                # On startup, get the user input of the freezing threshold, the boiling threshold and a fluctuation value.
                # Alerts are generated when a specific threshold has been reached or exceeded.
                # Alerts should not be repeatedly triggered if the temperature is fluctuating around the thresholds within the range of fluctuation value.
                # Alerts are defined with directions. Alert “freezing” is triggered if the previous temperature was above freezing threshold, and alert “unfreezing” is triggered if the previous temperature was below (freezing threshold + fluctuation value).
                # Similar for "boiling" and "unboiling". Alert “boiling” is triggered if the previous temperature was below boiling threshold, and alert “unboiling” is triggered if the previous temperature was above (boiling threshold - fluctuation value).
                #  
                # For example, considering the freezing threshold is set to 0, the boiling threshold is set to 100, and fluctuation value is set to 0.5,
                # Sample 1:
                # With the following temperature inputs,
                #     4.0 1.0 0.5 0.0 -0.5 0.0 0.5 0.0 -2.0 0.0 0.5 0.6 2.0
                # The output will be
                #     4.0 1.0 0.5 0.0 freezing -0.5 0.0 0.5 0.0 -2.0 0.0 0.5 0.6 unfreezing 2.0
                #  
                # Sample 2:
                # With the following temperature inputs,
                #     5.0 -0.5 0.5 -0.2 100 101
                # The output will be
                #     5.0 -0.5 freezing 0.5 -0.2 100 unfreezing boiling 101
                #  
                # Sample 3
                # With the following temperature inputs,
                #     0.0 0.3 0.5 0.4 0.7
                # The output will be
                #     0.0 freezing 0.3 0.5 0.4 0.7 unfreezing
#    note    :   
#                usage: python renbinGuo+answer+Pwc+Technical+Code+Test.py
                        # =====================================================================
                        # input freezing_threshold :0
                        # input boiling_threshold :100
                        # input flu_value :0.5
                        # input temperatures: -99 0.4 100   # iput from your keyboard 
                        # your input temperatures are:   [-99.0, 0.4, 100.0]
                        # The actual output is:
                        # [-99.0, 'freezing', 0.4, 100.0, 'unfreezing', 'boiling']
                        # test again ? [yes/no]yes
##########################################################################################



##########################################################################################
#   breif   :   alerts for temperature values from temperature list
#   input   :   input_temp_list     :   [list]      the input temperature list  , all element  is float or int
#               freezing_threshold  :   [float]     freezing threshold
#               boiling_threshold   :   [float]     boiling threshold
#               flu_value           :   [float]     fluctuation value
#   return  :   alerted_temp_list   :   [list]      the alerted temperature list,
#                                                  exception : return []
#   detail  :   temp ∈ (-∞,freezing_threshold]
#                       (freezing_threshold,freezing_threshold + flu_value]
#                       (freezing_threshold + flu_value,boiling_threshold -flu_value)
#                       [boiling_threshold -flu_value , boiling_threshold )
#                       [boiling_threshold,+∞ ) 
#               status ∈ { ice ,water ,boiding_water } 
#   note    :
##########################################################################################
def alert_temperature(input_temp_list,freezing_threshold,boiling_threshold,flu_value):
    WATER_STATUS = {
        'ICE':'ice',
        'WATER':'water',
        'BOILING_WATER':'boiding_water'
    }
    status = WATER_STATUS['WATER'] #  init the status 
    unfreezing_threshold = freezing_threshold +flu_value
    unboiling_threshold = boiling_threshold - flu_value
    alerted_temp_list = []
    for temp in input_temp_list:
        # print("[alert_temperature] item = ",temp)
        alerted_temp_list.append(temp)
        if not isinstance (temp,(int,float)):
            print("your input is wrong.")
            return []
        
        if temp <= freezing_threshold:  # T1
            if status == WATER_STATUS['ICE']:
                pass
            elif status == WATER_STATUS['WATER']:
                alerted_temp_list.append("freezing")
                status = WATER_STATUS['ICE']
            elif  status == WATER_STATUS['BOILING_WATER']:
                alerted_temp_list.append("unboiling")
                alerted_temp_list.append("freezing")
                status = WATER_STATUS['ICE']
        elif temp > freezing_threshold and temp <= freezing_threshold + flu_value  : # T2
            if status == WATER_STATUS['ICE']:
                pass
            elif status == WATER_STATUS['WATER']:
                pass
            elif status == WATER_STATUS['BOILING_WATER']:
                alerted_temp_list.append("unboiling")
                status = WATER_STATUS['WATER']
        elif temp >= freezing_threshold + flu_value and temp <boiling_threshold -flu_value: # T3
            if status == WATER_STATUS['ICE']:
                alerted_temp_list.append("unfreezing")
                status = WATER_STATUS['WATER']
            elif status == WATER_STATUS['WATER']:
                pass
            elif status == WATER_STATUS['BOILING_WATER']:
                alerted_temp_list.append("unboiling")
                status = WATER_STATUS['WATER']
        elif temp >= boiling_threshold - flu_value and  temp < boiling_threshold: #T4
            if status == WATER_STATUS['ICE']:
                alerted_temp_list.append("unfreezing")
                status = WATER_STATUS['WATER']
            elif status == WATER_STATUS['WATER']:
                pass
            elif status == WATER_STATUS['BOILING_WATER']:
                pass
        elif temp >= boiling_threshold : #T5
            if status == WATER_STATUS['ICE']:
                alerted_temp_list.append("unfreezing")
                alerted_temp_list.append("boiling")
                status = WATER_STATUS['BOILING_WATER']
            elif status == WATER_STATUS['WATER']:
                alerted_temp_list.append("boiling")
                status = WATER_STATUS['BOILING_WATER']
            elif status == WATER_STATUS['BOILING_WATER']:
                pass
            
    return alerted_temp_list

if  __name__ == "__main__":
    freezing_threshold = 0
    boiling_threshold = 100
    flu_value = 0.5
    input_temp = [4.0, 1.0 ,0.5 ,0.0 ,-0.5 ,0.0 ,0.5 ,0.0 ,-2.0 ,0.0 ,0.5, 0.6, 2.0]
    print("\n\nSample1:")
    print("With the following temperature inputs:")
    print(input_temp)
    print("The output will be:  =  ")
    print( [4.0, 1.0, 0.5, 0.0 ,'freezing', -0.5, 0.0 ,0.5, 0.0, -2.0 ,0.0 ,0.5 ,0.6 ,'unfreezing' ,2.0])
    print("\nThe  actual output is: ")
    alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    print(alerted_temp_list)

    input_temp = [5.0 ,-0.5, 0.5, -0.2, 100 ,101]
    print("\n\nSample2:")
    print("With the following temperature inputs:")
    print(input_temp)
    print("The output will be:    ")
    print([ 5.0 ,-0.5, 'freezing', 0.5, -0.2 ,100 ,'unfreezing','boiling', 101 ])
    print("The actual output is:  ")
    alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    print(alerted_temp_list)


    
    input_temp = [0.0,0.3 ,0.5 ,0.4, 0.7]
    alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    print("\n\nSample3:")
    print("With the following temperature inputs:")
    print(input_temp)
    print("The output will be:    ")
    print([0.0, 'freezing', 0.3, 0.5, 0.4, 0.7, 'unfreezing'])
    print("The actual output is:  ")
    print(alerted_temp_list)

    # input_temp = [0.0]
    # alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    # print("\n\nSample4:")
    # print("With the following temperature inputs:")
    # print(input_temp)
    # print("The output will be:    ")
    # print([0.0, 'freezing'])
    # print("The actual output is:  ")
    # print(alerted_temp_list)

    # input_temp = [100]
    # alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    # print("\n\nSample5:")
    # print("With the following temperature inputs:")
    # print(input_temp)
    # print("The output will be:    ")
    # print([100, 'boiling'])
    # print("The actual output is:  ")
    # print(alerted_temp_list)

    # input_temp = [100,-99]
    # alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    # print("\n\nSample6:")
    # print("With the following temperature inputs:")
    # print(input_temp)
    # print("The output will be:    ")
    # print([100, 'boiling',-99,'unboiling','freezing'])
    # print("The actual output is:  ")
    # print(alerted_temp_list)
    
    # input_temp = [-99,100]
    # alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    # print("\n\nSample7:")
    # print("With the following temperature inputs:")
    # print(input_temp)
    # print("The output will be:    ")
    # print([-99, 'freezing',100,'unfreezing','boiling'])
    # print("The actual output is:  ")
    # print(alerted_temp_list)

       
    # input_temp = [-99,0.4,100]
    # alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    # print("\n\nSample8:")
    # print("With the following temperature inputs:")
    # print(input_temp)
    # print("The output will be:    ")
    # print([-99, 'freezing',0.4,100,'unfreezing','boiling'])
    # print("The actual output is:  ")
    # print(alerted_temp_list)
    
    
    print("\n\n\n=====================================================================")
    test_again = 'yes'
    while test_again == 'yes':
        freezing_threshold = None
        boiling_threshold = None
        flu_value = None
        # print( "(freezing_threshold,(int,float)) =",(freezing_threshold,(int,float)) )
        #  get the input value  and check whether it is  valid  
        while not isinstance (freezing_threshold,(int,float)):
            try:
                freezing_threshold = float( input("input freezing_threshold :") )
            except ValueError:
                print('\nYou did not enter a valid integer or float,enter again:')
                pass 
        #  get the input value  and check whether it is  valid  
        while not isinstance (boiling_threshold,(int,float)):
            try:
                boiling_threshold = float( input("input boiling_threshold :") )
            except ValueError:
                print('\nYou did not enter a valid integer or float,enter again:')
                pass 
        # process exception
        if boiling_threshold <= freezing_threshold:
            print(" invalid input : boiling_threshold <= freezing_threshold ")
            break; 
        #  get the input value  and check whether it is  valid  
        while not isinstance (flu_value,(int,float)):
            try:
                flu_value = float( input("input flu_value :") )
            except ValueError:
                print('\nYou did not enter a valid integer or float,enter again:')
                pass 
        # process exception
        if flu_value < freezing_threshold  or  flu_value > boiling_threshold:
            print(" invalid input : flu_value <boiling_threshold  or  flu_value>freezing_threshold")
            break; 
        # print("freezing_threshold = ",freezing_threshold,"type(freezing_threshold) = ",type(freezing_threshold))
        # print("boiling_threshold = ",boiling_threshold,"type(boiling_threshold) = ",type(boiling_threshold))
        # print("flu_value = ",flu_value,"type(flu_value) = ",type(flu_value))
        is_input_temp_valid = False
        while not is_input_temp_valid:
            try:
                input_temp =  [ float(x) for x in input("input temperatures: ").split()]  
                is_input_temp_valid = True
            except ValueError:
                print('\nYou did not enter a valid integer or float,enter again:')
                pass
        # print("### input_temp = ",input_temp,"type(input_temp[0]) =",type(input_temp[0]))
        print("your input temperatures are:  ",input_temp)
        alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
        print("The actual output is: ")
        print(alerted_temp_list)
        test_again = input("test again ? [yes/no]")

