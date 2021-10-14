from ticket import *

User = Theatre(number_of_rows, number_of_seats)
User.setdict_seats()
User.set_total_seats()
User.set_total_income()
User.setpercentage()

import re

result = True
while result:
    print('--------------------------------')
    print('1.Show the seats\n2.Buy a Ticket\n3.Statistics\n4.Show booked Tickets User Info\n0.Exit')
    print('--------------------------------')
    while True:
        try:
            c = int(input('please enter the option\n'))
            print('--------------------------------')
            break
        except ValueError:
            continue

    if c == 0:
        result = False
    elif c == 1:
        # Show the seats
        print('Cinema:\n')
        User.displayseats()

        print()
    elif c == 2:
        # Buy a Ticket
        print('')
        print('Available seats\n')
        User.displayseats()
        print('')
        while True:
            while True:
                try:
                    row = int(input('Please Choose Row no \n'))
                    break
                except:
                    continue
            while True:
                try:
                    column = int(input('Please Choose Column no \n'))
                    break
                except:
                    continue
            if User.checkavailable(row,column) == True:
                break
            else:
                print('The seat you are selected is Not Available')
                print('Please select another seat\n')
                continue
        ticket_price = User.set_ticketprice(row)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\tticket price: ${}'.format(ticket_price))
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        while True:
            try:
                ch = int(input('Do you want to buy\n1.Yes\n2.No\n'))
                break
            except:
                continue
        while True:
            if ch == 1:
                print('Please enter your details\n')
                while True:
                    name = input('Please Enter Your Name \n')
                    if name.replace(' ','').isalpha():
                        break
                    else:
                        print('Please make sure that you have entered name in valid format\n')
                        continue
                while True:
                    gender =  input('Please Choose Male or Female no \n')
                    if gender.isalpha():
                        break
                    else:
                        print('Please make sure that you have entered Gender in valid format\n')
                        continue
                while True:
                    try:
                        age = int(input('Please Enter your Age \n'))
                        break
                    except:
                        print('Please make sure that you have entered Age in valid format\n')
                        continue
                while True:
                    while True:
                        try:
                            ph = str(int(input('Please Enter Your Phone no \n')))
                            break
                        except ValueError:
                            print('Please enter a valid 10 Digit phone number\n')
                            continue
                    regx = '[0-9]{10}'
                    if re.search(regx,ph) == None:
                        print('Please enter a valid 10 Digit phone number\n')
                        continue
                    else:
                        break
                User.bookticket(row,column,name,gender,age,ph)
                break
            elif ch == 2:
                print('Thank you for checking\n Wish to see you soon')
                break
            else:
                continue
        print('')
        pass

    elif c == 3:

        # Statistics
        print('')
        print('Number of purchased tickets : {}'.format(User.number_of_purchased_tickets))
        print('Percentage : {:.2f}%'.format(User.setpercentage()))
        print('Current income : ${}'.format(User.current_income))
        print('Total Income : ${}'.format(User.total_income))

        pass
    elif c == 4:
        # Show booked Tickets User Info
        print('User info')
        print(User)
        pass
    else:
        print('Please choose the correct no\n')