# Name: Tanner Jenkins
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]


num_emps = len(emp)

fed_ded_list = []
state_ded_list = []
soc_ded_list = []
med_ded_list = []
retirement_ded_list = []
gross_pay_list = []
net_pay_list = []

gross_pay_grand = 0
net_pay_grand = 0

################## Define Global Variables ###############
JOB_CODES = ("C", "S", "J", "M",)
PAY_RATE = (16.50, 15.75, 15.75, 19.50,)
DED = (.12, .03, .062, .0145, .04,)

################# Define Functions #######################

def main():
    perform_calculations()
    display_results()


def perform_calculations():
    global gross_pay_grand, net_pay_grand
    
    for i in range(num_emps):
        if job[i] == JOB_CODES[0]:
            gross_pay = PAY_RATE[0] * hours[i]

        elif job[i] == JOB_CODES[1]:
            gross_pay = PAY_RATE[1] * hours[i] 

        elif job[i] == JOB_CODES[2]:
            gross_pay = PAY_RATE[2] * hours[i] 

        else:  
            gross_pay = PAY_RATE[3] * hours[i] 

        fed_ded = gross_pay * DED[0]
        state_ded = gross_pay * DED[1]
        soc_ded = gross_pay * DED[2]
        med_ded = gross_pay * DED[3]
        retirement_ded = gross_pay * DED[4]

        total_ded = fed_ded + state_ded + soc_ded + med_ded + retirement_ded
        net_pay = gross_pay - total_ded

        gross_pay_grand += gross_pay 
        net_pay_grand += net_pay

        fed_ded_list.append(fed_ded)
        state_ded_list.append(state_ded)
        soc_ded_list.append(soc_ded)
        med_ded_list.append(med_ded)
        retirement_ded_list.append(retirement_ded)
        gross_pay_list.append(gross_pay)
        net_pay_list.append(net_pay)

def display_results():
    line =('-------------------------------------------------------------------------------------------------------------------------------------------------')
    money ='8,.2f'
    tab = '\t'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]

    print (line)
    print ("************************************************************** FRESHFOODS PAYROLL ***************************************************************")
    print ("\n\tRUN DATE/TIME: " + dt_short)
    print ("\nName" + tab + tab + tab + "Job" + tab + "Hours" + tab + tab + "Fed Deduction" + tab + tab +
           "State Deduction" + tab + tab + "Social Security" + tab + tab + "Medicare" + tab + "Retirement" + tab + "Net Pay")
    
    for i in range(num_emps):
        dataline1 = emp[i]+ tab + job[i] + tab + format(hours[i],money) + tab + format(fed_ded_list[i],money) + tab + tab
        dataline2 = format(state_ded_list[i],money) + tab + tab + format(soc_ded_list[i],money) + tab + tab + format(med_ded_list[i],money) + tab + format(retirement_ded_list[i],money) + tab + format(net_pay_list[i],money)
        print (dataline1 + dataline2)
    print (line)
    print ("Total Gross Pay: " + format(gross_pay_grand,money))
    print ("Total Net Pay: " + format(net_pay_grand,money))

main()
