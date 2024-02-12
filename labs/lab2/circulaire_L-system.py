import turtle

def apply_rule(ch, rules):
    return rules.get(ch, ch)

def generate_l_system(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join(apply_rule(ch, rules) for ch in result)
    return result

def draw_l_system(turtle, instructions, angle, length):
    for instruction in instructions:
        if instruction == 'F':
            turtle.forward(length)
        elif instruction == '+':
            turtle.left(angle)
        elif instruction == '-':
            turtle.right(angle)

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(5)
    fractal_turtle.penup()
    fractal_turtle.goto(-150, -150)
    fractal_turtle.pendown()

    axiom = "F"
    rules = {"F": "F+F-F-F+F"}
    iterations = int(input("Введите количество итераций (целое число): "))
    angle = 90
    length = 5

    instructions = generate_l_system(axiom, rules, iterations)
    draw_l_system(fractal_turtle, instructions, angle, length)

    window.exitonclick()

if __name__ == "__main__":
    main()
