def admin_required(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("You are not alloweded")
        else:
            return func(a,b)
    return wrapper

@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin




@admin_required
def delete_acc(user,accno):
    return str(accno)+"delete"

print(change_pin("admin",1000))
print(delete_acc("admin",1000))