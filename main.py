"""This is my integration project."""
__author__ = "Gildardo Miguel"
"""This program is used to make a transaction of ice cream through the system 
either for a large number of people or individual buyers. 
While giving an opportunity for the buyer 
to win a discount when a user buys in large."""


# Jairo helped me space out the question and clarify all the if statements
# (https://www.w3schools.com/python/default.asp)
# w3schools helped with any problem I encountered with code
# (https://www.youtube.com/watch?v=myJ36xIR7Yg&ab_channel=GeekTutorials)
# Jairo helped me simplify these terms

# calc for calculate
# disc for discount
# Calculate cost of cones with discounted price
# Jairo helped me write a doc string helped me by explaining
# I needed to explain: a parameter also what a return is.

def calc_cost_of_cones_with_disc(cones):
    """This function will find the cost of cones after the user
    has successfully passed the quiz and apply the discounted price.
    parameter:
        cones - The amount of cones ordered
    return:
        price_of_cones_with_discount - The new cost of the cones
        with the discount"""
    price = 1.25
    price_of_cones_with_discount = price * cones
    # return will bring back whatever is next to "return"
    # In this case when cones is inputted the function will "Return"
    # price of cones with discount
    return price_of_cones_with_discount


# calc for calculate
# reg for regular
# Calculate the cost of cones with regular price


def calc_cost_of_reg_price(cones):
    """This function will find the cost of cones after the user has failed
     the quiz and full price of cones is applied to the total.
     parameter:
        cones - The amount of cones ordered
     return:
        price_of_cones_with_no_discount - The new cost of the cones
        without discount"""
    price = 3.00
    price_of_cones_with_no_discount = price * cones
    return price_of_cones_with_no_discount


# calc for calculate
# w for with
# Calculate the total cost of cones and drinks

def calc_cost_of_cones_w_drinks(cones, drinks):
    """This function will find the cost of cones and
    drinks if drinks were purchased.
    parameter:
        cones - The amount of cones ordered
        drinks - The amount of drinks ordered
    return:
        price_of_cones_with_drinks - The new cost of cones after
        drinks were purchased """
    price_per_cone = 3.25
    price_per_drink = 2.50
    # int(_) will make anything inside the () a whole number
    price_of_cones_with_drinks = (price_per_cone * int(cones)) + \
                                 (price_per_drink * int(drinks))
    return price_of_cones_with_drinks


# calc for calculate
# j for just
# Calculate the cost of just cones

def calc_cost_of_j_cones(cones):
    """This function will find the cost of just cones being purchased.
    parameter:
        cones - The amount of cones ordered
    return:
        price - The cost of buying cones """
    price = 3.25
    # Shortcut operator multiplies the price and input of cones
    price *= int(cones)
    # return will Return the "price" when you calculate the cost of just cones
    return price


def calc_change(cost):
    """This function will give the proper change pack to the user by avoiding
     the user enter less than enough to pay for the total and
     allowing for exact change to be given.
     parameter:
        cost - The total amount due for the user "The bill"
     return:
        change - The amount of change that will be given back to the user"""
    print("Your total will be:$" + format(cost, "0.2f"))
    while True:
        try:
            cash = input(
                "Enter the amount of cash you want to pay with\n")
            change = float(cash) - cost
            if change >= 0:
                # break is used to let the user get out of the loop once they
                # satisfy the requirements
                break
        # except ValueError is a way to explain to the user that their input is
        # incorrect and will explain what they are doing wrong
        except ValueError:
            print("Invalid response")
    return change


def main():
    """This is the main function that is used to make a transaction
     of ice cream through the system either for a large number of people
    or individual buyers. While giving an opportunity for the buyer
    to win a discount through catering."""

    # Tohui is the name of the Ice Cream Store
    # Homemade ice cream is always better than bought
    # it asks for the user name to make it more friendly
    print("Hello Welcome to Tohui Ice Cream!\nWhere everything is made "
          "homemade! \nWhat is your name?")

    # customer's first input in the program is with their name
    # input allows user to input a function
    # customer_name will store the user's name
    customer_name = input("Enter your name:")

    # easter egg when you use the company's name
    # this line will ONLY run if the user types Tohui as their name
    if 'Tohui' in customer_name:
        print("Welcome back boss!!!")

    # Starting a transaction
    # Starting point of the program
    print("Hi", customer_name, "its nice to meet you \nWould you like to buy "
                               "some ice cream?")

    # Its a question to initiate a split to either continue with the program
    # or stop and end the program
    customer_choice = input("a = Yes b= No\nEnter a or b:")

    # the while statement will run until the user enters the proper input
    # Jairo helped me with this while statement != means does not equal
    # Customer_choice has to be put twice to use "And" to specify both
    # conditions
    while ((customer_choice != "a" and customer_choice != "A") and
           (customer_choice != "b" and customer_choice != "B")):
        # User enters a invalid response and will get a error message
        print("Invalid Response, Please try again.")
        customer_choice = input("a = Yes b = No \nEnter a or b:")

    # the if statements will check for uppercase and convert to lowercase
    # to continue running the program
    if customer_choice == "A":
        customer_choice = "a"
    if customer_choice == "B":
        customer_choice = "b"

    # First split of the program
    # a = Yes , yes they would like to buy some ice cream
    # == , means equal
    if customer_choice == "a":
        # Second split of the program user decides whether they are buying
        # for many people or just themselves
        print("Would you like to buy for Catering or Individually?")
        customer_choice = input("C = Catering D = Individually\n" "Enter C"
                                " or D:")
        # C=Catering
        # While loop to make the user select the appropriate response
        while ((customer_choice != "c" and customer_choice != "C") and
               (customer_choice != "d" and customer_choice != "D")):
            print("Invalid Response, Please try again.")
            customer_choice = input("C = Catering D = Individually\n"
                                    "Enter C or D:")
        if customer_choice == "c":
            customer_choice = "C"
        if customer_choice == "b":
            customer_choice = "B"

        # C means user chose Catering
        if customer_choice == "C":

            # Third split of the program
            print("How many cones would you like? \nWe have 50 or 100 cones "
                  "for your party.")

            cones = input("A = 50 cone or B = 100 cones \n"
                          "Enter your choice:")

            while ((cones != "a" and cones != "A") and
                   (cones != "b" and cones != "B")):
                print("Invalid Response")
                cones = input("A = 50 cone or B = 100 cones \n"
                              "Enter A or B:")
            if cones == "a":
                cones = "A"
            if cones == "b":
                cones = "B"

            # 50 cones option
            if cones == "A":

                # This question requires a user input
                print("How many people are in your party?")

                # Rachel and Jairo helped me with this while True function
                # The while True will run to see if the statement inside the
                # loop is true
                while True:
                    # try is another way of saying run this function
                    try:
                        # Inside the function will run into the proper input
                        # is given by the user people is a input determined
                        # by the user
                        people = int(input("Enter the number of people in "
                                           "your party \nEnter a number:"))

                        # A range is set on people to let everyone in the
                        # party to have at least one cone
                        # if statement and also be written
                        # if people < 0 and people < 51 but for python it will
                        # suggest you write it in their form to not get errors
                        if 0 < people < 51:

                            # The break is used to break out the loop
                            # because if the previous conditions are meet no
                            # further action is needed
                            break
                        else:

                            # The raise is like saying if they don't insert
                            # The proper answer The Value Error will tell
                            # The user what is wrong which is "ValueError"
                            raise ValueError

                    # The Except has to be at the end of every while True
                    # This plays like a net and makes sure the user
                    # Enters a valid answer in the marked priced range
                    except ValueError:

                        print("Error. Please enter a Positive Number between "
                              "1-50"
                              "\nMake sure this is enough cones to go around")
                # cones gets assigned the value of 50
                cones = 50

                # Number of extra cones that will be left if uneven
                # //Floor division is used
                left_over_cones = cones // int(people)

                # Number of cones each person will get equally
                # % Modulus used
                cones_everyone_gets = cones % int(people)
                print("There will be", cones_everyone_gets, "cones extra \n "
                                                            "and every one "
                                                            "will receive",
                      left_over_cones, "cones each\n")
                # used 2.x from repl.it example
                # Quiz starts to help give a discount to the user
                print("The price is $3.00 per cone would you want to play a "
                      "game for a chance to get \n each cone for "
                      "$1.25?")

                # Fourth split of the program
                # Start a possibility for discount
                customer_choice = input("a = Yes b= No\nEnter a or b:")
                while ((customer_choice != "a" and customer_choice != "A") and
                       (customer_choice != "b" and customer_choice != "B")):
                    print("Invalid Response, Please try again.")
                    print("Would you want to play a game for a chance to \n"
                          "each cone for $1.25?")
                    customer_choice = input("a = Yes b= No\n"
                                            "Enter a or b:")
                if customer_choice == "A":
                    customer_choice = "a"
                if customer_choice == "B":
                    customer_choice = "b"

                # a= Yes
                if customer_choice == "a":
                    print(
                        "If there's 20 apples to share with a group of 5 "
                        "friends how many apples do each friend get?\n "
                        "What two numbers in this sentence can be divided to "
                        "give each person 4 apples?")

                    # First number should be 20
                    first_num = int(input("First number\n"))

                    # Second number should be 5
                    second_num = int(input("Second number\n"))
                    # "/" is used for division
                    # first number is divided by second number
                    answer = (first_num / second_num)
                    print("Your answer is:", int(answer))

                    # if the answer is right it will continue to question 2
                    if answer == int(4):
                        print("Correct!")
                        print("Your half way there to your discount! Keep "
                              "going!")
                        print("\n")

                        # Question 2
                        print("What number do I need as a exponent to "
                              "multiply 10 by to get 100?\n")

                        # if the first question is the correct it will
                        # proceed to second question The exponent will be used
                        # to get the power of 10
                        # second_question = int(input("What x value for 10^x "
                        # "gives me 100? \n"))

                        while True:
                            # try is another way of saying run this function
                            try:
                                second_question = int(
                                    input("What x value for 10^x "
                                          "gives me 100? \n"))
                                break
                            except ValueError:
                                print(
                                    "Answer has to be in a number format")

                        # correct answer
                        if second_question == int(2):
                            print("Correct")
                            # ** exponential used
                            # sep is a separator of objects
                            print("Win!" * 10, sep=' ')

                            # user has passed the quiz and discount price is
                            # applied
                            print("Congrats on your discount!")

                            # def function is used to calculate the cost of
                            # cones with discount
                            # disc for discounted
                            disc_price_50_cones = calc_cost_of_cones_with_disc(
                                cones)
                            print("Your total is: $" + format(
                                disc_price_50_cones, "0.2f"),
                                  "Thank you for shopping!")
                            # function is applied
                            change = calc_change(disc_price_50_cones)
                            print("Your change will be: $" + format(change,
                                                                    "0.2f"),
                                  "\n Have a Nice Day", customer_name,
                                  "Come Again!")
                            # end of program for 50 cones option and passed
                            # the quiz

                        # if user got the second question wrong discount is
                        # defaulted regular price is applied
                        else:
                            print("Incorrect! Sorry you no longer qualify "
                                  "for the discount.")
                            regular_price_of_50_cones = calc_cost_of_reg_price(
                                cones)
                            print("Your total is: $" + format(
                                regular_price_of_50_cones, "0.2f"),
                                  "Thank you for shopping!")
                            change = calc_change(regular_price_of_50_cones)
                            print("Your change will be: $" + format(change,
                                                                    "0.2f"),
                                  "\n Have a Nice Day", customer_name,
                                  "Come Again!")
                        # end of 50 cones option end of program did NOT pass
                        # the quiz (missed second question)

                    # if user got first question wrong discount is defaulted
                    else:
                        print("Incorrect! Sorry you no longer qualify for "
                              "the discount.")
                        regular_price_of_50_cones = calc_cost_of_reg_price(
                            cones)
                        print("Your total is: $" + format(
                            regular_price_of_50_cones, "0.2f"),
                              "Thank you for shopping!")
                        change = calc_change(regular_price_of_50_cones)
                        print(
                            "Your change will be: $" + format(change, "0.2f"),
                            "\n Have a Nice Day", customer_name, "Come Again!")

                        # end of 50 cones option end of program did not pass
                        # the quiz (missed the first question)
                    # Chooses no discount opportunity and will be applied full
                    # price
                elif customer_choice == "b":
                    regular_price_of_50_cones = calc_cost_of_reg_price(
                        cones)
                    print(
                        "Your total is: $" + format(regular_price_of_50_cones,
                                                    "0.2f"),
                        "Thank you for shopping!")
                    change = calc_change(regular_price_of_50_cones)
                    print("Your change will be: $" + format(change, "0.2f"),
                          "\n Have a Nice Day", customer_name, "Come Again!")
                # end of 50 cones option end of program did Not try the quiz

            # start of 100 cones option
            elif cones == "B":
                print("How many people are in your party?")
                while True:
                    # try is another way of saying run this function
                    try:
                        # Inside the function will run into the proper input
                        # is given by the user people is a input determined
                        # by the user
                        people = int(input("Enter the number of people in "
                                           "your party \nEnter a number:"))
                        # A range is set on people to let everyone in the
                        # party to have at least one cone
                        # python is the only one that allows you to write
                        # 0 < people < 101 without using a "And" statement
                        # You can also write it like this:
                        # if people > 0 and people < 101
                        if 0 < people < 101:
                            # The break is used to break out the loop
                            # because if the previous conditions are meet no
                            # further action is needed
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Error. Please enter a Positive Number between "
                              "1 - 100 ")
                cones = 100

                # Number of extra cones that will be left if uneven
                left_over_cones = cones // int(people)

                # Number of cones each person will get equally the symbol %
                # will find the remainder of cones by the number of people
                number_cones_everyone_gets = cones % int(people)
                print("There will be", number_cones_everyone_gets,
                      "cones extra \n and every one will receive",
                      left_over_cones, "cones each")
                print("The price is $3.00 per cone would you want to play a "
                      "game for a chance to get \n each cone for" "$1.25 ?")

                # introducing quiz for discount
                # fourth split of the program
                customer_choice = input("a = Yes b= No\nEnter a or b:")

                while customer_choice != "a" and customer_choice != "b":
                    print("Invalid Response, Please try again.")
                    print("Would you want to play a game for a chance to \n"
                          "each cone for $1.25?")
                    customer_choice = input("a = Yes b= No\n"
                                            "Enter a or b:")
                if customer_choice == "A":
                    customer_choice = "a"
                if customer_choice == "B":
                    customer_choice = "b"

                # Yes is selected
                if customer_choice == "a":
                    print("If there's 20 apples to share with a group of 5 "
                          "friends how many apples do each friend "
                          "get?\n "
                          "What two numbers in this sentence can be divide "
                          "to give each person 4 apples?")
                    # First number should be 20
                    first_num = int(input("First number\n"))
                    # Second number should be 5
                    second_num = int(input("Second number\n"))
                    answer = (first_num / second_num)
                    print("Your answer is:", int(answer))
                    if answer == int(4):
                        print("Correct!")
                        print("Your half way there to your discount! Keep "
                              "going!")
                        print("\n")

                        # second question of quiz
                        print("What number do I need as a exponent to "
                              "multiply 10 by to get 100?\n")

                        # user has won will be charged discounted price
                        while True:
                            try:
                                second_question = int(
                                    input("What x value for 10^x "
                                          "gives me 100? \n"))
                                break
                            except ValueError:
                                print("Answer has to be in number format")

                        if second_question == int(2):
                            print("Correct")
                            print("Win" * 10)
                            print("Congrats on your discount!")
                            # disc for discounted
                            # Pri for price
                            # discounted price of 100 cones
                            disc_pri_100_cones = calc_cost_of_cones_with_disc(
                                cones)
                            print("discount price of cone is $" + format(
                                disc_pri_100_cones, '.2f'))
                            change = calc_change(disc_pri_100_cones)
                            print("Your change will be: $" + format(change,
                                                                    "0.2f"),
                                  "\n Have a Nice Day", customer_name,
                                  "Come Again!")
                        # end of the program 100 cones option passed quiz

                        # second question wrong
                        else:
                            print("Incorrect! Sorry you no longer qualify "
                                  "for the discount.")
                            # reg for regular
                            reg_price_of_100_cones = calc_cost_of_reg_price(
                                cones)
                            print("regular price of cone is $" + format(
                                reg_price_of_100_cones, '.2f'))
                            change = calc_change(reg_price_of_100_cones)
                            print("Your change will be: $" + format(change,
                                                                    "0.2f"),
                                  "\n Have a Nice Day", customer_name,
                                  "Come Again!")
                        # end of 100 cones option end of program did not
                        # pass the quiz (missed the second question)

                    # First question wrong charges full price
                    else:
                        print("Incorrect! Sorry you no longer qualify for "
                              "the discount.")
                        regular_price_of_100_cones = calc_cost_of_reg_price(
                            cones)
                        print("regular price of cone is $" + format(
                            regular_price_of_100_cones, '.2f'))

                        change = calc_change(regular_price_of_100_cones)
                        print(
                            "Your change will be: $" + format(change, "0.2f"),
                            "\n Have a Nice Day", customer_name, "Come Again!")

                        # end of 100 cones option end of program did not
                        # pass the quiz (missed the first question)

        # Individual option

        elif customer_choice == "D":
            # Professor Vanselow , Jairo , Ryan , and Rachel helped me with
            # building this list This part of the program enables a user to
            # build a list based on the flavors they choose List that will
            # be displayed
            flavor_lst = ["Vanilla", "Chocolate", "Strawberry"]
            # list that will be used to store user's pick
            # the user makes their list based on what the user picks
            user_lst = []
            print("We have these flavors available:", flavor_lst[0],
                  flavor_lst[1], flavor_lst[2])
            # Determine the amount of flavors the user will input
            while True:
                try:
                    user_flavors = int(
                        input("Enter number of flavors you would like "
                              ": "))
                    # the user needs to have at least one flavor
                    # but not exceed 3
                    if 0 < user_flavors < 4:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Enter a number between 1 and 3")

            # The for loop will take the input of the user
            for flavor in range(user_flavors):
                chosen_flavor = input("Enter a flavor:")
                while chosen_flavor not in flavor_lst:
                    chosen_flavor = input("Enter a flavor:")
                    print("Make sure you are using Capital letters")
                # append adds a item to the end of a list 
                user_lst.append(chosen_flavor)

            print(user_lst)
            if user_flavors == 1:
                print("Basic")
            elif user_flavors == 2:
                if ("Vanilla" in user_lst or "vanilla" in user_lst) and (
                        "Chocolate" not in user_lst):
                    print("Pretty Neutral")
                if "Chocolate" in user_lst:
                    if "Vanilla" or "vanilla" not in user_lst:
                        print("Zingy")

            elif user_flavors == 3:
                print("Neapolitan, Classy I like it! ")

            print("How many cones would you like? Each cone is $3.25")
            cones = input("Enter the amount of cones you would like. \n")
            # def function of calculate cost of just cones
            total_cost_just_cones = calc_cost_of_j_cones(cones)
            print("Your total so far is: $" + format(total_cost_just_cones,
                                                     "0.2f"),
                  "Would you like some drinks?")

            drinks = input("A = Yes B= No\nEnter A or B:")
            while drinks != "A" and drinks != "B":
                print("Invalid Response, Please try again.")
                drinks = input("A = Yes B= No\n"
                               "Enter A or B:")
            # Yes to drinks option
            if drinks == "a":
                drinks = "A"
            if drinks == "b":
                drinks = "B"

            if drinks == "A":
                print("How many drink would you like? each drink is $2.50")
                drinks = input("Enter the amount of drinks you would like. \n")
                total_cost_with_drinks_and_cones = calc_cost_of_cones_w_drinks(
                    cones, drinks)
                if total_cost_with_drinks_and_cones >= 100:
                    print("You're my favorite Customer!")
                else:
                    print(
                        "Sharing is caring, don't forget to buy grandma some!")
                print("Your new total is: $" + format(
                    total_cost_with_drinks_and_cones, "0.2f"),
                      "Thank you for shopping!")
                change = calc_change(total_cost_with_drinks_and_cones)
                print("Your change will be: $" + format(change, "0.2f"),
                      "\n Have a Nice Day", customer_name, "Come Again!")
            # end of individual program with drink options

            # No to drinks
            elif drinks == "B":
                change = calc_change(total_cost_just_cones)
                print("Your change will be: $" + format(change, "0.2f"),
                      "\n Have a Nice Day", customer_name, "Come Again!")

            # end of individual program with no drink option

    # If user said no to buying ice cream
    elif customer_choice == "b":
        print("Have a Nice Day!\n", end='End of program')
    # end of program


#   specify why this loop is done this way
# to avoid over indenting and passing the limited 79 characters
# to make the program run again and avoid going over Rachael advised me
# to put the main call inside a while True loop


while True:

    main()

    while input("Would you want to make another order?"
                "\n Enter Y or N:") != "Y" \
            and input != "y":
        print("Have a nice day")
        break
