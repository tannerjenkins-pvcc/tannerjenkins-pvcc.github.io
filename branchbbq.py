# Name: Tanner Jenkins
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############################  define global variables  #############################
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95

CHILD_MEAL = 11.95

SALES_TAX_RATE = .062

# define global variables
num_adults = 0

num_children = 0


############################  define program functions #############################
def main():
    prompt_in = "\nWould you like to order again (Y or N)? "
    goodbye_msg = "Thank you for your order. Enjoy your meal!"
    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input(prompt_in)
        if (yesno.upper()) == "N":
            more_meals = False
            print(goodbye_msg)


def get_user_data():
    global num_adults, num_children
    num_children = int(input('Number of children: '))
    num_adults = int(input('Number of adults: '))


def perform_calculations():
    global subtotal, service_fee, sales_tax, total, child_price, adult_price
    adult_price = num_adults * ADULT_MEAL
    child_price = num_children * CHILD_MEAL
    subtotal = adult_price + child_price
    service_fee = SALES_TAX_RATE * subtotal
    total = subtotal + service_fee


def display_results():
    line = "---------------------------------------------------"
    title1 = "****  Branch Barbeque Buffet  ****"
    currency = '5,.2f'
    date = str(datetime.datetime.now())
    title2 = "Best Southern cooking this side of the Mississippi!"


    print(line)
    print(title1)
    print(title2)
    print(line)
    print('Number of Children ' + format(num_children, '7'))
    print('Number of Adults ' + format(num_adults, '9'))
    print('Price for Children $ ' + format(child_price, '2'))
    print('Price for Adults   $ ' + format(adult_price, '4'))
    print('Subtotal           $ ' + format(subtotal, currency))
    print('Sales Tax          $ ' + format(service_fee, currency))
    print('Total              $ ' + format(total, currency))
    print(line)
    print(date)


################# call on main program to execute ###################
main()
