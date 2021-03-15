import math #imports the libary math 

print("Choose either 'investment' or 'bond' from the menu below to proceed:")#this print function gives instruction on what to do 


print("investment -    to calculate the amount of interest youll earn on you investment:")#this print function gives more instruction on the options


print("Bond -         to calculate the amount youll have to pay pn a home loan:")#this print function is added choice as well to the pevious instruction 


user_choice = input("please enter you choice here:")#stoes users input in this variable 


fix_capital= user_choice.lower()#takes user inout and puts it into lower case so no matter what way they type it will always be correct



if fix_capital =="investment":#if statment and its condition which checks if the users input is == the right condition 


    deposit = int(input("Please enter the amount of money you deposited here :R"))#takes users input and stores it in this variable


    rate = int(input("please enter the interet rate you would like note the rate is represented as a percentage but only type the number e.g (8) and not (8%):"))#takes users input and stores it in this variable


    years = int(input("pleaase enter the number of years you would like to keep this investment for:"))#takes users input and stores it in this variable


    investment = input("please choose between  'simple' or 'compound' interest:")#takes users input and stores it in this variable



    if investment == "compound":#nested if that checks if the above selection is true and runs the right formulas below and prints it out 
        
        percent = rate/100

        total = deposit * math.pow((1+percent),years)

        print("This is your total of all your investments with compound interest R{}".format(round(total,2)))

    elif investment == "simple":#if the above statement is wrong then this nested else statement will be run and its formulas 

        percent = rate/100

        total = deposit * (1+ percent * years)

        print("This is your total of all your investments with simple interest R{}".format(round(total)))



else:

 value = float(input("Please enter the value of your house here:R"))#this else stamne will be run only if our first if statement is false and all its inputs and formulas will be run and printed out with the print function


 rate = float(input("Please enter you interest rate here:"))


 months = int(input("please enter the amount of months you would like to take to pay:"))


 monthly_rate = rate/12


 total = (monthly_rate*value)/(1 - (1+monthly_rate)**(-months))


 print("this is your total bond repayment R{}".format(round(total,2)))
