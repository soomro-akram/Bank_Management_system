
# Bank Management System! 
from pathlib import Path
file_path = Path("Record.txt")

print("\tBank_Management_System\n")

def create_account():
    try:
        acc_no = int(input("ENTER YOUR ACCOUNT NUMBER: "))
        name = input("ENTER YOUR NAME: ")
        balance = int(input("ENTER YOUR ACCOUNT BALANCE: "))

        with open(file_path,"a") as fs:
            fs.write(f" {acc_no}\t {name.upper()}\t {balance}\n")

            print("ACCOUNT CREATED SUCCESSFULY!")
    except Exception as err:
        print(f"An error occured as {err}")
def deposit():
    try:
        acc_no = int(input("ENTER ACCOUNT NUMBER: "))
        amount = int(input("ENTER DEPOSIT AMOUNT: "))

        with open(file_path, "r") as fs:
            records = fs.readlines()

        updated_records = []
        found = False

        for record in records:
            data = record.strip().split("\t")

            if int(data[0]) == acc_no:
                balance = int(data[2])
                balance += amount

                updated_records.append(
                    f"{data[0]}\t{data[1]}\t{balance}\n"
                )

                found = True
                print("DEPOSIT SUCCESSFUL!")
                print(f"NEW BALANCE: {balance}")

            else:
                updated_records.append(record)

        if not found:
            print("ACCOUNT NOT FOUND!")
            return

        with open(file_path, "w") as fs:
            fs.writelines(updated_records)

    except Exception as err:
        print(f"An error occurred: {err}")
    
def withdraw():
    try:
        acc_no = int(input("ENTER ACCOUNT NUMBER: "))
        amount = int(input("ENTER WITHDRAW AMOUNT: "))

        with open(file_path, "r") as fs:
            records = fs.readlines()

        updated_records = []
        found = False

        for record in records:
            data = record.strip().split("\t")

            if int(data[0]) == acc_no:
                balance = int(data[2])

                if amount > balance:
                    print("INSUFFICIENT BALANCE!")
                    return

                balance -= amount

                updated_records.append(
                    f"{data[0]}\t{data[1]}\t{balance}\n"
                )

                found = True
                print("WITHDRAWAL SUCCESSFUL!")
                print(f"REMAINING BALANCE: {balance}")

            else:
                updated_records.append(record)

        if not found:
            print("ACCOUNT NOT FOUND!")
            return

        with open(file_path, "w") as fs:
            fs.writelines(updated_records)

    except Exception as err:
        print(f"An error occurred: {err}")
    
def check_balance():
    try:
        acc_no = int(input("ENTER ACCOUNT NUMBER: "))

        with open(file_path, "r") as fs:
            records = fs.readlines()

        found = False

        for record in records:
            data = record.strip().split("\t")

            if int(data[0]) == acc_no:
                print("\n----- ACCOUNT DETAILS -----")
                print(f"Account Number : {data[0]}")
                print(f"Account Holder : {data[1]}")
                print(f"Balance        : {data[2]}")
                found = True
                break

        if not found:
            print("ACCOUNT NOT FOUND!")

    except Exception as err:
        print(f"An error occurred: {err}")
def view_all_accounts():
    try:
        with open(file_path, "r") as fs:
            records = fs.readlines()

        if len(records) == 0:
            print("NO ACCOUNTS FOUND!")
            return

        print("\n========== ALL ACCOUNTS ==========")
        print(f"{'ACCOUNT NO.':<15}{'NAME':<20}{'BALANCE'}")
        print("-" * 45)

        for record in records:
            data = record.strip().split("\t")

            print(f"{data[0]:<15}{data[1]:<20}{data[2]}")

    except FileNotFoundError:
        print("RECORD FILE NOT FOUND!")

    except Exception as err:
        print(f"An error occurred: {err}")


print("Press 1 for Creating Bank Account: ")
print("Press 2 for Deposit Money: ")
print("Press 3 for Withdraw Money: ")
print("Press 4 for Check Balance: ")
print("Press 5 for View All Accounts: ")

user = int(input("\nENTER YOUR CHOICE: "))

if user == 1:
    create_account()
elif user ==2:
    deposit()
elif user == 3:
    withdraw()
elif user == 4:
    check_balance()
elif user == 5:
    view_all_accounts()

else:
    print("Invalid Choice!")