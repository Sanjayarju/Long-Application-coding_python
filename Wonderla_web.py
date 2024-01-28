users = []
category_lists = []
booking_details = []

class user_details:

    def __init__(self,id,name,mail,password):
        self._id = id
        self._name = name
        self._mail = mail
        self._password = password

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_mail(self):
        return self._mail

    def get_password(self):
        return self._password

    def hardcodedata(self):
        users.append(self)
        return users
    
    def validate_login(self,mail,password):
        for user in users:
            if user.get_mail() == mail and user.get_password() == password:
                return user
            return False
        
class category:

    def __init__(self,id,place,name,fare):
        self.id = id
        self.place = place
        self.name = name
        self.fare = fare

    def hardcodedata(self):
        category_lists.append(self)
        return category_lists
    
    def show(self):
        print("-------Your available category-------\n")
        for category in category_lists:
            print(f"categoryId: {category.id}\n"
                  f"Place of park: {category.place}\n"
                  f"TicketName: {category.name}\n"
                  f"Ticket Fare per person: {category.fare}\n")
            
class booking(category):

    def __init__(self,selected_item):
        super().__init__(selected_item.id,selected_item.place,selected_item.name,selected_item.fare)
        self.selected_item = selected_item

    def book(self,no_of_persons):
        date = input("Enter the date you want to book: ")
        total_price = selected_item.fare * no_of_persons

        pay = input("Enter the payment method(Cash or card or Netbanking or UPI): ").upper()
        if pay is not None:
            print("Your Total amount to be paid is",total_price)
            a = input("Please Confirm to pay(yes/no): ").lower()
            if a == 'yes':
                print("Payment Success")
                cart_item = {
                'Place': selected_item.place,
                'category': selected_item.name,
                'No of persons' : no_of_persons,
                'price': total_price,
                'Date': date,
                'pay' : pay
            }
                booking_details.insert(0,cart_item)
                print("..............Your tickets booked Successfully.................\n")
            else:
                print("Payment cancelled")

class booked(user_details):

    def show(self):
        if len(booking_details) != 0:

            print("--------Your Booking history--------\n")
            for book in booking_details:
                print(f"Name of the Customer: {self.get_name().upper()}")
                print(f"Place of the park: {book['Place']}")
                print(f"Ticket Type: {book['category']}")
                print(f"No of Tickets: {book['No of persons']}")
                print(f"Total amount paid: {book['price']}")
                print(f"Date of Booking slot: {book['Date']}")
                print(f"Payment method: {book['pay']}\n")
        else:
            print(".......No Booking Available........")

    def delete_history(self):

        global booking_details
        print("......Choose the options.....\n1. Delete last booking 2. Delete all history")
        choose = int(input("Enter valid option: "))

        if choose == 1:

            if len(booking_details) != 0:
                booking_details.pop(0)
                print("Last History is deleted successfully......")
            else:
                print("No History........")
        if choose == 2:

            booking_details = []
            print("All History deleted successfully......")
                        
if __name__ == "__main__":

    while True:
        print("**************Welcome to Wonderla****************")
        email = input("Enter your mailid: ")
        passkey = input("Enter your password: ")

        obj1 = user_details(1,'sanjay','sanjay@mail','sanjay123')
        obj1.hardcodedata()

        login_check = obj1.validate_login(email,passkey)
        if login_check:
            flag = True
            while (flag == True):
                print("\n----------Dashboard---------")
                print("1. Category")
                print("2. Book your ticket")
                print("3. Booking History")
                print("4. Delete History")
                print("5. Logout")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                        place = input("Enter your place of the park(kochi or bangalore or hyderabad): ")
                        if place == 'kochi':
                            obj = category(1,place,'Adult',1360)
                            obj.hardcodedata()
                            obj = category(2,place,'child',1090)
                            obj.hardcodedata()
                            obj = category(3,place,'Senior Citizen',1020)
                            obj.hardcodedata()
                            obj = category(4,place,'Student',1000)
                            obj.hardcodedata()
                        if place == 'bangalore':
                            obj = category(1,place,'Adult',1360)
                            obj.hardcodedata()
                            obj = category(2,place,'child',1090)
                            obj.hardcodedata()
                            obj = category(3,place,'Senior Citizen',1020)
                            obj.hardcodedata()
                            obj = category(4,place,'Student',1000)
                            obj.hardcodedata()
                        if place == 'hyderabad':
                            obj = category(1,place,'Adult',1360)
                            obj.hardcodedata()
                            obj = category(2,place,'child',1090)
                            obj.hardcodedata()
                            obj = category(3,place,'Senior Citizen',1020)
                            obj.hardcodedata()
                            obj = category(4,place,'Student',1000)
                            obj.hardcodedata()
                        obj.show()

                if choice == 2:
                    cat_id = int(input("Enter the category id you want to book: "))

                    no_of_persons = int(input("Enter the number of persons: "))

                    if cat_id == 0:
                        print("Enter the valid category id.....")
                    else:
                        for cat in category_lists:
                            if cat.id == cat_id:
                                selected_item = cat
                                break
                        if selected_item is not None:
                            objj = booking(selected_item)
                            objj.book(no_of_persons)
                        else:
                            print("You are not selected any......")

                if choice == 3:
                    app = booked(obj1.get_id(),obj1.get_name(),obj1.get_mail(),obj1.get_password())
                    app.show()

                if choice == 4:
                    app.delete_history()

                if choice == 5:
                    print("***************Thank you using our service***************")
                    print(".........Logout Successfully........\n")
                    flag = False
