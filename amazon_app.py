users = []
product_details = []
booking_history = []

class user_details:

    def __init__(self,id,name,mail,password):
        self.id = id
        self.name = name
        self.mail = mail
        self.password = password

    def hardcodedata(self):
        users.append(self)
        return users
    
    def validate_login(self,mail,passkey):
        for user in users:
            if user.mail==mail and user.password == passkey:
                return user
            else:
                return False
            
class product_lists:

    def __init__(self,id,name,type,price):
        self.id = id
        self.name = name
        self.type = type
        self.price = price

    def hardcodedata(self):
        product_details.append(self)

    def show(self):
        for product in product_details:
            print(f"Product Id:{product.id},"
                  f"Product Name:{product.name},"
                  f"Product Type:{product.type},"
                  f"Product Price:{product.price}\n")
            
class booking(product_lists):

    def __init__(self,selected_item):
        super().__init__(selected_item.id,selected_item.name,selected_item.type,selected_item.price)
        self.selected_item = selected_item

    def book(self,quantity):
        total_price = selected_item.price * quantity

        cart_item = {
            'Item Name':{selected_item.name},
            'Item Type':{selected_item.type},
            'Item Quantity':{quantity},
            'Item Total price':{total_price}
        }

        booking_history.append(cart_item)
        print("--------Item booked Successfully--------")

    def show(self):
        print("=========Your booking Details below-------")
        print(f"Item Name: {selected_item.name}"
              f"Item type: {selected_item.type}"
              f"Item price per day: {selected_item.price}\n")
        
class booked:
    def show(self):
        for book in booking_history:
            print("Your Booked history\n")
            print(f"Ordered Item Name: {book['Item Name']} "
                  f"Ordered Item Type: {book['Item Type']} "
                  f"Ordered Item Quantity: {book['Item Quantity']} "
                  f"Ordered Item Price: {book['Item Total price']}\n")
            
if __name__=="__main__":
    while True:
        print("--------Welcome to Amazon----------")

        email = input("Enter your mailid: ")
        passkey = input("Enter your password: ")

        obj = user_details(1,'sanjay','sanjay@mail','sanjay123')
        obj.hardcodedata()

        login_check = obj.validate_login(email,passkey)
        if login_check:
                flag = True
                while (flag == True):

                    print("--------services----------")
                    print("1. Products Lists")
                    print("2. Order Product")
                    print("3. Booking History")
                    print("4. Exit")

                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        prod = product_lists(1, 'Mobiles','Android',15000)
                        prod.hardcodedata()
                        prod = product_lists(2, 'Dresses','Women',1000)
                        prod.hardcodedata()
                        prod = product_lists(3, 'Books','Ebooks',500)
                        prod.hardcodedata()
                        prod.show()

                    if choice == 2:
                        Item_id = int(input("Enter the item Id you want: "))
                        selected_item = None
                        for item in product_details:
                            if item.id == Item_id:
                                selected_item = item
                                break
                        quantity = int(input("Enter the Quantity of the product: "))
                        if selected_item is not None:
                            prod = booking(selected_item)
                            prod.book(quantity)
                            prod.show()
                        else:
                            print("-----------Invalid item ID----------")

                    if choice == 3:
                        prod = booked()
                        prod.show()

                    if choice == 4:
                        print("---------Thank You for using our service----------")
                        flag = False
        else:
            print("---------Invalid user details---------")

            


            



