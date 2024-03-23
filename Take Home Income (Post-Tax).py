import matplotlib.pyplot as plt

income = 50000
max_pa = 12570

#Personal Allowance
if income < 100000:
    pa = 12570
elif income > 100000 and income <= 100000 + max_pa*2:
    pa = max_pa - (income-100000)/2
else:
    pa = 0
    
#Input tax brackets in format:
# [percentage taxed, lower bracket boundary, upper bracker boundary]
# where the boundaries are in units pounds per year and a upper boundary of True is used to denote no upper bound
tax_brackets = [[0, 0, pa],         #Income tax 0% below personal allowance
               [20, pa, 50270],     #Income tax 20% between £12,570 and £50,270 pa
               [13.25, 9880, 50268],#National insurance
               [3.25, 50268, True], #National insurance
               [9, 27295, True],    #SFE repayment 9% above £27,295 pa
               [40, 50270, 150000], #Income tax 40% between £50,270 and £150,000 pa
               [45, 150000, True]]  #Income tax 45% above £150,000 pa

def post_tax_income(income, tb = tax_brackets):
    takeaway = income
    tax = 0
    
    for i in range(len(tb)):
        
        #If income is less than tax bracket, skip
        if income < tb[i][1]:
            continue
        
        #Taxing income
        
        #If income is within this tax bracket
        elif income <= tb[i][2] or tb[i][2] == True:
            tax = (income - tb[i][1]) * tb[i][0] / 100
        #If income is above this tax bracket
        elif income > tb[i][2]:
            tax = (tb[i][2] - tb[i][1]) * tb[i][0] / 100 

        takeaway -= tax
    
    return takeaway

def plot(lowerx = 0, upperx = 200000, scale = "Y"):
    """Plots the post-tax (net) income again pre-tax (gross) incomes of range lowerx to upperx.
    To scale the y-axis, input argument of scale = "Y", "M", or "W" for yearly, monthly or weekly respectively. """
    x = list(range(lowerx, upperx, 50))
    s = ["Y", "y", "M", "m", "W", "w"]  #scale of plot
    
    if scale not in s:
        raise Exception("scale argument needs to be \"Y\", \"M\" or \"W\"")
    
    if scale == "Y" or scale == "y":
        s = 1
        date = "Yearly"
    elif scale == "M" or scale == "m":
        s = 12
        date = "Monthly"
    elif scale == "W" or scale == "w":
        s = 365/7
        date = "Weekly"     
    
    y = [post_tax_income(i)/s for i in x]
    
    plt.figure("Net income")
    plt.plot(x,y, "-")
    plt.plot(x, [i/s for i in x])
    plt.xlabel("Gross yearly income / £")
    plt.ylabel("{} income / £".format(date))
    plt.margins(x=0, y=0)
    plt.title("{} income (2022-2023)".format(date))
    plt.grid()
    plt.legend(["Net", "Gross"])
    #plt.savefig("Net income.png")
    plt.show()

plot(18000, 31000, scale = "m")

print()
print("You have a pre-tax (gross) income of £{:,} \n\
As such, you've a yearly net income of: £{:,.2f} with a yearly tax of £{:,.2f} \n\
As such, you've a monthly net income of: £{:,.2f} with monthly tax of £{:,.2f}".format(
    income, 
    post_tax_income(income), income-post_tax_income(income), 
    post_tax_income(income)/12, income/12-post_tax_income(income)/12))
