#Import the csv data file and create output file
import csv
fileToLoad="PythonPyBank.csv"
filtToOutput="PythonPyBankAnalysis.txt"
#Setup variables
totalMonths=0
prevRevenue=0
monthOfChange=[]
revenueChangeList=[]
greatestIncrease=[“”,0]
greatestdecrease=[“”,9999999999999]
totalRevenue=0
#Convert csv to a list of dictionaries
with open(fileToLoad) as revenueData:
    reader= csv.DictReader(revenueData)
#1 Calculate total number of months in the data set
    for row in reader:
        totalMonths=totalMonths+1
        totalRevenue=totalRevenue+int(row["Revenue"])
#2 Calculate net total Profit/Loss
        revenueChange=int(row["Revenue"])-prevRevenue
        prevNet=int(row["Revenue"])
        revenueChangeList=revenueChangeList+[revenueChange]
        monthOfChange=monthOfChange=[row["Date"]]
#4 Calculate greated increaes in profit (date and amount)
        if(revenueChange>greatestIncrease[1]):
            greatestIncrease[0]=row["Date"]
            greatestIncrease[1]=revenueChange
#5 Calculate greatest decrease in loss (date and amount)
        if(revenueChange<greatestDecrease[1]):
            greatestDecrease[0]=row["Date"]
            greatestDecrease[1]=revenueChange
#3 Calculate average change in P/L
revenueAvg=sum(revenueChangeList)/len(revenueChangeList)
#6 Print the analysis to the terminal and export a text file with the results
output=(
    f"\nFinancial Analysis\n"
    f"---------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${totalRevenue}\n"
    f"Average Change:${revenueAvg}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0] (${greatestIncrease[1]})\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0] (${greatestDecrease[1]})\n"
    
)
print(output)

with open(fileToOutput, "w") as txtFile:
    txtFile.write(output)

