import os
import csv

csv_path = os.path("C:\Users\Home\WUSTL201907DATA2\03-Python\Homework\Instructions\PyBank\Resources\budget_data.csv")

def PyBank(Budget):
    Month = 0
    Month_List = []
    Profit_Losses = []
    Change_List = []
    
    

    #Count Total Profit/Losses
    #Average Change Each Month
    Total_Profit_Losses
    Average_Change

    #Find Greatest Increase and Decrease
    Greatest_Increase 
    Greatest_Decrease 

    Monthly_Changes
        Greatest_Increase
        Greatest_Decrease
    

   


    #print(Profit_Losses)
    print(f'Financial Analysis')
    print(f'------------------------')
    print(f'Total Months: {Month}')
    print(f'Total Profit/Losses: ${Total_Profit_Losses}')
    print(f'Average Change: ${Average_Change}')
    print(f'Greatest Increase: {Date_I} with ${Greatest_Increase}')
    print(f'Greatest Decrease: {Date_D} with ${Greatest_Decrease}')

with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #print(csv_file)

    next(csv_reader,None)

    PyBank(csv_reader)
