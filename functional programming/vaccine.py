def vaccine_check(func):
    def wrapper(a,b,c):
        if b<18:
            raise  Exception("not eligible")
        else:
            return func(a,b,c)
    return wrapper

@vaccine_check
def vaccine(name,age,place):
    return "eligible"
print(vaccine("anu",18,"ernakulam"))