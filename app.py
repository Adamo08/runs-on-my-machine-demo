user_input = input("Sh7al 3yiti lyoma (0-5)? ")

match int(user_input):
    case 0 | 1 | 2:
        print("ba9i fresh.")
    case 3 | 4 :
        print("Chwiya. pip install coffee --upgrade")
    case 5:
        print("Ingali3")
    case _:
        print("Mn nyta!")
