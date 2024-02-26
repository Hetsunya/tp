import turtle
import math

def apply_rule(ch):
    if ch == 'A':
        return 'F-F-F-F-F-F-C'
    elif ch == 'F':
        return 'Ff+Ff+Ff+Ff+Ff+Ff+Cf'
    elif ch == 'f':
        return 'f'
    elif ch == 'C':
        return 'C'
    else:
        return ch

def generate_l_system(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join(apply_rule(ch) for ch in result)
    return result

def draw_l_system(turtle, instructions, angle, length, distance_between_c_and_f):
    for instruction in instructions:
        if instruction == 'F':
            turtle.forward(length)
        elif instruction == 'f':
            turtle.penup()
            turtle.forward(length)
            turtle.pendown()
        elif instruction == '+':
            turtle.left(angle)
        elif instruction == '-':
            turtle.right(angle)
        elif instruction == 'C':
            # Перемещаем turtle к центральной точке с увеличенным расстоянием
            turtle.penup()
            turtle.forward(distance_between_c_and_f)
            turtle.pendown()

def main():
    turtle.speed(200)
    turtle.hideturtle()
    turtle.title("Modified L-System Fractal")

    axiom = 'A'
    rules = {'A': 'F-F-F-F-F-F-C', 'F': 'Ff+Ff+Ff+Ff+Ff+Ff+Cf', 'f': 'f', 'C': 'C'}
    iterations = 3
    angle = 60
    length = 7
    distance_between_c_and_f = 50  # Увеличенное расстояние между C и F

    l_system = generate_l_system(axiom, rules, iterations)
    draw_l_system(turtle, l_system, angle, length, distance_between_c_and_f)

    turtle.done()

if __name__ == "__main__":
    main()
