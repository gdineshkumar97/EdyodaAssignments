while True:
    while True:
        try:
            number_of_rows = int(input('Enter the number of rows:\n'))
            break
        except ValueError:
            # There is a chance of error can happen user can enter a string or float
            continue
    while True:
        try:
            number_of_seats = int(input('Enter the number of seats in each row:\n'))
            break
        except ValueError:
            # There is a chance of error can happen user can enter a string or float
            continue
    if number_of_rows == 0 or number_of_seats == 0:
        print('Hey its not a valid row or column\n')
        continue
    else:
        break

class Theatre:
    seat_rows = []  # Total Rows store here
    dict_seats = {}  # Total Seats will be stored here

    def __init__(self, number_of_rows, number_of_seats):
        self.number_of_rows = number_of_rows
        self.number_of_seats = number_of_seats

        self.rows_list = [i for i in range(1, self.number_of_rows + 1)]
        self.seats_list = [j for j in range(1, self.number_of_seats + 1)]
        self.total_seats = 0
        self.total_income = 0
        self.ticket_price = 0
        self.current_income = 0
        self.number_of_purchased_tickets = 0
        self.percentage = 0

    def displayseats(self):
        #This method is to display the available seats
        self.list1 = [' ']
        for i in range(1, self.number_of_seats + 1):
            self.list1.append(str(i))
        print(*self.list1)

        for key, val in Theatre.dict_seats.items():
            if val[0] == 'S':
                # || We have used index 0 for display purpose as a numbers
                self.x = key.split('Row')
                val[0] = self.x[1]
        for i in Theatre.dict_seats.values():
            print(*i)

    def setdict_seats(self):
        #This method is for to set seats
        for row in self.rows_list:
            self.seat_rows.append('Row' + str(row))
            for seat in self.seat_rows:
                self.dict_seats[seat] = ['S' for i in range(len(self.seats_list) + 1)]

    def set_total_seats(self):
        #this is for set total seats
        self.total_seats = self.number_of_rows * self.number_of_seats

    def get_total_seats(self):
        #This is for get the total seats
        return self.total_seats

    def set_ticketprice(self, r):
        #This method is for calculate the ticket price
        self.row = r
        if self.total_seats < 60:
            self.ticketprice = 10
        else:
            self.middle_index = len(self.rows_list) // 2
            self.front_half = self.rows_list[:self.middle_index]
            self.back_half = self.rows_list[self.middle_index:]

            self.FH_Total = len(self.front_half) * 10 * len(self.seats_list)
            self.BH_Total = len(self.back_half) * 8 * len(self.seats_list)

            if self.row in self.front_half:
                self.ticketprice = 10
            elif self.row in self.back_half:
                self.ticketprice = 8

        return self.ticketprice

    def set_total_income(self):
        #This method is for calculate the total income and return the total income
        self.tp = 10
        if self.total_seats < 60:
            self.total_income = self.total_seats * self.tp
        else:
            self.middle_index = len(self.rows_list) // 2
            self.front_half = self.rows_list[:self.middle_index]
            self.back_half = self.rows_list[self.middle_index:]

            self.FH_Total = len(self.front_half) * 10 * len(self.seats_list)
            self.BH_Total = len(self.back_half) * 8 * len(self.seats_list)
            self.total_income = self.FH_Total + self.BH_Total

        return self.total_income

    def checkavailable(self,r,c):
        #This method is for checking the availability of the seat
        self.row = r
        self.column=c
        try:
            for self.key in self.dict_seats:
                if self.key == 'Row' + str(self.row):
                    if self.dict_seats[self.key][self.column] == 'S':
                        return True
                    else:
                        return False
        except:
            return False

    def bookticket(self, row, column, name, gender, age, ph):
        #This method is for book a seat if the want to book
        self.name = name
        self.gender = gender
        self.age = age
        self.ph = ph
        self.row = row
        self.column = column

        for self.key in self.dict_seats:
            if self.key == 'Row' + str(self.row):
                if self.dict_seats[self.key][self.column] == 'S':
                    self.dict_seats[self.key][self.column] = 'B'
                    print('Ticket Booked Successfully\n')

                    self.current_income = self.current_income + self.ticketprice
                    self.number_of_purchased_tickets = self.number_of_purchased_tickets + 1
                else:
                    print('Please select un booked seat')
                    pass

    def setpercentage(self):
        #This method is for calculate the percentage
        self.percentage = (self.number_of_purchased_tickets / self.total_seats) * 100
        return self.percentage

    def __str__(self):
        #This method is for print the user info
        return '*************************\n*     DINESH CINEMAS    *\n*************************\nName         : {}\nGender       : {} \nAge          : {} \nTicket Price : ${}\nPhone        : {}\n*************************\n'.format(
            self.name, self.gender, self.age, self.set_ticketprice(self.row), self.ph)