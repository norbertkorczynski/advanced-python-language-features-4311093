# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values

x = None

# Literal patterns are explicit values: integers, strings, Booleans, etc
match x:
    case 0:
        print("zero")
    case 1:
        print("one")
    case "zero":
        print(0)
    case None:
        print("nothing")
    case _:
        print("no match")
