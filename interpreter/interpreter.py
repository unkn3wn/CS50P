expression = input("Expression: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        sub = x - z
        print(sub)
    case "*":
        product = x * z
        print(product)
    case "/":
        div = x / z
        print(div)