
import csv
from decimal import *

with open('/Users/hectorprado/Desktop/CodeCademy/Data_Analytics/Projects/python-portfolio-project-starter-files/insurance.csv') as insurance:
#     converts the .csv into a dictionary 
    insurance_reader = csv.DictReader(insurance)
    
#     variables 
    sum_ages = 0
    file_length = 0
    sum_cost = 0
    south_west = 0
    south_east = 0 
    north_west = 0
    north_east = 0
    smokers = 0
    males = 0
    male_average_age = 0
    male_average_cost = 0
    male_average_bmi = 0
    male_smokers = 0
    females = 0
    female_average_age = 0
    female_average_cost = 0
    female_average_bmi = 0
    female_smokers = 0
    bmi_average = 0
    children = 0

#     Calculating the age average, cost average 
    for row in insurance_reader:
        file_length+=1
        sum_ages+=int(row["age"])
        sum_cost+= float(row['charges'])
        bmi_average += float(row['bmi'])
        children += int(row['children'])
        
        
        if row['sex'] == 'male':
            males+=1
            male_average_age += int(row['age'])
            male_average_cost += float(row['charges'])
            male_average_bmi += float(row['bmi'])
            if row['smoker'] == 'yes':
                male_smokers += 1
            
            
        else:
            females+=1
            female_average_age += int(row['age'])
            female_average_cost += float(row['charges'])
            female_average_bmi += float(row['bmi'])
            if row['smoker'] == 'yes':
                female_smokers += 1
                
    
            
        if row['smoker'] == 'yes':
            smokers+=1
            
        if row['region'] == 'southwest':
            south_west += 1
        elif row['region'] == 'southeast':
            south_east += 1
        elif row['region'] == 'northwest':
            north_west += 1
        else:
            north_east += 1
        
        
        
#     calculates the average 
    print('Number of people in the file: '+str(file_length))
    
    print('There are '+str(males)+' males in the file'+
          '\nThere are '+str(females)+" females in the file")
    
    print("\nThe averge age is: "+ str(round(sum_ages/file_length,0)))
    print("The average male age is: "+str(round(male_average_age/males,0))
          +'\nThe average female age is: '+str(round(female_average_age/females,0)))
    
    print('\nThe average BMI is :'+str(round(bmi_average/file_length,2)))
    print('The average male BMI is: '+str(round(male_average_bmi/males,2))
         +"\nThe average female BMI is: "+str(round(female_average_bmi/females,2)))
    
    print('\nPeople on file have '+str(round(children/file_length,0))+' child on average')
    
    print("\n"+str(smokers)+" people are smokers")
    print(str(male_smokers)+" males are smokers\n"
         +str(female_smokers)+" females are smokers")
    
    print("\nNumber of poeple at the follwoing location: \n" 
          +'South West: '+str(south_west)
          +'\nSouth East: '+str(south_east)
          +'\nNorth West: '+str(north_west)
          +'\nNorth East: '+str(north_east))
    
    average_insurance_cost = sum_cost/file_length
    print("\nThe average insurance cost is: "+str(round(average_insurance_cost,2))+" US dollars")
    print('The average male insurance cost is: '+str(round(male_average_cost/males,2))+" US dollars"
         +'\nThe average female insurance cost is: '+str(round(female_average_cost/females,2))+" US dollars")


with open('/Users/hectorprado/Desktop/CodeCademy/Data_Analytics/Projects/python-portfolio-project-starter-files/insurance.csv') as insurance:
    
    print(insurance.read())