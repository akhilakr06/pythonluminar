#bank account problem
#define fixed ammound user accept

print("....Bank Details....")
# name=input("Enter the name of account holder")
# print(name)
fixed_deposit = 10000
withdraw=int(input("Enter amount to withdraw:"))
# if withdraw > fixed_deposit:
#     print("insufficient balance!!!")
# else:
#     bal=fixed_deposit-withdraw
#     print("Your balance is", bal)
#     print("successfully withdrawn")

if withdraw <= fixed_deposit:
    bal = fixed_deposit - withdraw
    print("Your balance is", bal)
    print("successfully withdrawn")
else:
    print("insufficient balance!!!")