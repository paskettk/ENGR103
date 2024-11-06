#######################################################################
# Program Filename: ENGR103_Assignment3
# Author: Kate Paskett
# Date: 5/12/24
# Description: Computes pulse pressure and mean arterial pressure
# Input: SP, DP
# Output: PP, MAP
#######################################################################

#######################################################################
# Function: calculate_PP(SP, DP)
# Description: calculates pulse pressure
# Parameters: SP and DP (mmHg)
# Return values: PP 
# Pre-Conditions: SP and DP are integer values where SP>DP
# Post-Conditions: none
#######################################################################
    
def calculate_PP(SP, DP): # calculates pulse pressure
    return (SP-DP)

#######################################################################
# Function: check_PP(PP)
# Description: checks pulse pressure
# Parameters: PP (mmHg)
# Return values: prints PP status
# Pre-Conditions: PP is an integer value
# Post-Conditions: none
#######################################################################

def check_PP(PP): # check pulse pressure
    if PP > 80:
        print('PP is high')
    elif PP <= 80:
        print('PP is normal')
    else:
        print('Invalid input')

#######################################################################
# Function: calculate_MAP(DP, PP)
# Description: calculates MAP
# Parameters: DP, PP (mmHg)
# Return values: MAP (mmHg)
# Pre-Conditions: DP and PP are integer values
# Post-Conditions: none
#######################################################################

def calculate_MAP(DP, PP): # calculate mean arterial pressure
    return (DP + (1/3 * PP))

#######################################################################
# Function: check_MAP(MAP)
# Description: checks mean arterial pressure
# Parameters: MAP (mmHg)
# Return values: prints MAP status
# Pre-Conditions: MAP is an integer value
# Post-Conditions: none
#######################################################################

def check_MAP(MAP): # check mean arterial pressure
    if MAP < 60:
        print('MAP is low, seek medical assistance')
    elif MAP >= 60:
        print('MAP is acceptable')
    else:
        print('Invalid input')

#######################################################################
# Function: main()
# Description: prompts user input and runs above functions
# Parameters: none
# Return values: prints calculated values
# Pre-Conditions: none
# Post-Conditions: none
#######################################################################

def main(): # main function
    SP = int(input('Enter systolic pressure in mmHg:'))

    DP = int(input('Enter diastolic pressure in mmHg:'))

    PP = calculate_PP(SP, DP)
    print('Your pulse pressure is:', PP, 'mmHg')
    check_PP(PP)

    MAP = calculate_MAP(DP, PP)
    print('Your mean arterial pressure is:', MAP, 'mmHg')
    check_MAP(MAP)

main()