users = []
vehicle_details = []
booking_details = []

class user_details:
    def __init__(self,id,name,mailid,password):
        self.id = id
        self.name = name
        self.mailid = mailid
        self.password = password

    def hardcodedata(self):
        users.append(self)
        return users

    def validate_login(self,mail,password):
        for user in users:
            if user.mailid == mail and user.password == password:
                return user
            else:
                return False

class vehicle_booking:
    def __init__(self,id,name,type,price):
        self.id = id
        self.name = name
        self.type = type
        self.price = price

    def hardcodedata(self):
        vehicle_details.append(self)

    def show(self):
        for vehicle in vehicle_details:
            print(f"vehicle ID: {vehicle.id}, "
                  f"vehicle Name: {vehicle.name}, "
                  f"vehicle Type: {vehicle.type}, " 
                  f"vehicle price: {vehicle.price}\n")
            
class booking_history:

    def show(self):
        print("----------Booking history-----------\n")
        for book in booking_details:
            print(f"Vehicle Id: {book['vehicleID']}, "
                  f"Vehicle Name: {book['vehicleName']}, "
                  f"No_of_days: {book['No_of_days']}, "
                  f"Total_price: {book['Total_price']}\n"
                  )
            
class booking(vehicle_booking):
    def __init__(self, selected_vehicle):
        super().__init__(selected_vehicle.id, selected_vehicle.name, selected_vehicle.type, selected_vehicle.price)
        self.selected_vehicle = selected_vehicle

    def book(self,no_of_days):
            
            total_price = int(selected_vehicle.price)*no_of_days

            cart_item = {
                'vehicleID': selected_vehicle.id,
                'vehicleName': selected_vehicle.name,
                'No_of_days': no_of_days,
                'Total_price': total_price
            }

            booking_details.append(cart_item)
            print(".........Vehicle booked successfully.........\n")

    def show(self):
        print("Your Booking details below\n")
        print(f"vehicle ID: {selected_vehicle.id}, "
                  f"vehicle Name: {selected_vehicle.name}, "
                  f"vehicle Type: {selected_vehicle.type}, "
                  f"No of days: {no_of_days}, " 
                  f"vehicle price per day: {selected_vehicle.price}\n")
        

if __name__=="__main__":

    print("------WELCOME TO TRAVELS------")

    obj = user_details(1,"sanjay","sanjay@mail","sanjay123")
    obj.hardcodedata()
    while True:
        email = input("Enter your mail: ")
        passkey = input("Enter your password: ")

        login_check = obj.validate_login(email,passkey)
        if login_check:
            flag = True
            while (flag==True):
                print("----------Services--------\n1. Vehicle Lists 2. Book vehicles 3. Booking history 4. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    vehi=vehicle_booking(1, "swift","3+1s",8000)
                    vehi.hardcodedata()
                    vehi=vehicle_booking(2, "Rapid","3+1s",10000)
                    vehi.hardcodedata()
                    vehi=vehicle_booking(3, "Innova","4+1s",12000)
                    vehi.hardcodedata()
                    vehi.show()

                if choice == 2:
                    vehi_id = int(input("Enter the vehicle id you want: "))

                    no_of_days = int(input("Enter the no.of.days you want the vehicle: "))

                    selected_vehicle = None
                    for vehicle in vehicle_details:
                        if vehicle.id == vehi_id:
                            selected_vehicle = vehicle
                            break
                    if selected_vehicle is not None:
                        vehi = booking(selected_vehicle)
                        vehi.book(no_of_days)
                        vehi.show()
                    else:
                        print("Invalid vehicle ID. Please try again.")

                if choice == 3:

                    vehi = booking_history()
                    vehi.show()

                if choice == 4:
                    print("..........Thank you for using our service.........")
                    print("-----------Logout Successfully-----------\n")
                    flag = False
        else:
            print("........Incorrect mail and password.........\n")

    


            






        