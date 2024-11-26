def decorator(func):
    def inner():
        print("Process started")
        func()
        print("Process ended")
    return inner


@decorator  
def hello():
    print("Processing...")


hello()
