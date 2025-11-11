"""
This is my Elite 101 chatbot for the prework project.
I chose the name DeliBot which is a food delivery assistant chatbot.
The bot helps with your delivery problems (refunds, delays, etc).
"""

# The Intro Functions:
def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print("Hello", name + ", welcome to DeliBot Support.")
    print("I can help you with common delivery issues today.")

# Main Function (which handles a lot of the stuff):
def main():
    user_name = get_user_name()
    greet_user(user_name)

    while True:
        print("What issue are you experiencing?")
        print("1. My food hasn’t arrived")
        print("2. My order is incorrect")
        print("3. I want to request a refund")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            order_number = input("Please enter your order number: ")
            print("Thank you. We are checking your order status.")
            print("Your driver appears to be delayed and should arrive soon.")
        elif choice == "2":
            item = input("Please enter the item that was wrong or missing: ")
            print(f"We’re sorry about that. We’ll notify the restaurant and credit you for {item}.")
        elif choice == "3":
            reason = input("Please describe why you are requesting a refund: ")
            print("Thank you. A refund request has been submitted for review.")
            print("You will receive an update within 24 hours.")
        elif choice == "4":
            print("Thank you for contacting DeliBot Support. Goodbye!")
            #this breaks when you choose option 4
            break
        else:
            print("Invalid selection. Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()

