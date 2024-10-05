user_input = input("enter the chai type \n")

match user_input:
    case "Black tea":
        print("the price of black tea is 4$")
    case "Oolong tea":
        print("the price of Oolong tea is 5$")
    case _:
        print("chal bikhari")

