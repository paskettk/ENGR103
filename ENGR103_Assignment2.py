# imports math module
import math 

#######################################################################
# Program Filename: EGNR103_Assignment2_2.py
# Author: Kate Paskett
# Date: 6/26/24
# Description: Wind Power Calculation
# Input: average wind speed, operating efficiency, blade radius
# Output: max turbine power, actual turbine power
#######################################################################

#######################################################################
# Function: max_power_output()
# Description: calculates max power output of a wind turbine
# Parameters: 
#   -wind_speed (float): The average wind speed in meters per second (m/s)
#   -efficiency (float): The operating efficiency of the turbine as a percentage (%)
#   -radius (float): The radius of the turbine blades in meters (m)
# Return values: max power output (float)
# Pre-Conditions: 
#   -all inputs are integer values
#   -wind_speed should be greater than 0, efficiency should be between 0-100, and radius should be greater than 0
# Post-Conditions:
#   -returns max power output of turbine
#######################################################################

# create function to imput values

def max_power_output(wind_speed, efficiency, radius):

    # calculate max wind speed: 
    max_power =   0.5 * 1.2 * math.pi * (radius ** 2) * (wind_speed ** 3) / 1000
    return max_power

#######################################################################
# Function: main()
# Description: gathers values from user and displays max power and actual power
# Parameters: none
# Return values: none
# Pre-Conditions:
#   -max_power_output is defined
#   -inputs are integer values
# Post-Conditions:
#   -calculates and prints max turbine power and actual turbine power rounded to 2 decimal points
#######################################################################

def main():
    # Getting the wind speed from the user
    wind_speed = float(input("Please enter the wind speed in m/s: "))

    # Getting blade radius from user    
    radius = float(input("Please enter the blade radius in meters: "))

    # Getting the wind speed from the user
    efficiency = float(input("Please enter the efficiency as a %: "))

    # restate entered values
    print("Wind speed: ", wind_speed, "m/s", "Efficiency: ", efficiency,"%", "Radius: ", radius, "m")

    # calculate max power output
    x = max_power_output(wind_speed, efficiency, radius)
    print("Maximum turbine power: ", x, " kW")

    # calculate actual power ouput
    print("Actual turbine power: ", (efficiency/100) * x, " kW")

main()

