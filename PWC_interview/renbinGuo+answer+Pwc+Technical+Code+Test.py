# -*- coding: utf-8 -*-
###########################################################################################
#   breif   :  console application  that adds alerts for temperature values from console input 
#   history :  renbin Guo created 20200115_1825
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
##########################################################################################



##########################################################################################
#   breif   :   alerts for temperature values from temperature list
#   input   :   input_temp_list     :   [list]      the input temperature list  , all element  is float or int
#   return  :   alerted_temp_list   :   [list]      the alerted temperature list,
#                                                    exception : return []
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
        print("[alert_temperature] item = ",temp)
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
            print("T3 temp = ",temp)
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
    alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    print(" test1: alerted_temp_list  =  ")
    print(alerted_temp_list)

    input_temp = [5.0 ,-0.5, 0.5, -0.2, 100 ,101]
    alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    print(" test2: alerted_temp_list  =  ")
    print(alerted_temp_list)


    
    input_temp = [0.0,0.3 ,0.5 ,0.4, 0.7]
    alerted_temp_list = alert_temperature(input_temp,freezing_threshold,boiling_threshold,flu_value)
    print(" test3: alerted_temp_list  =  ")
    print(alerted_temp_list)
        

