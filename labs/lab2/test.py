import math
import turtle

def apply_rule(ch):
    if ch == 'A':
        return 'F+F+F+F+F+F-C'
    if ch == 'F':
        return 'F+F+F+F+F+F-C'
    elif ch == 'C':
        return 'F'
    else:
        return ch

def generate_l_system(axiom, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join(apply_rule(ch) for ch in result)
    return result

def draw_fractal(instructions, size):
    for instruction in instructions:
        if instruction == 'A':
            turtle.circle(size)
        elif instruction == 'F':
            turtle.circle(size/6)
        elif instruction == 'C':
            turtle.circle(size)
        elif instruction == '+':
            turtle.left(60)
        elif instruction == '-':
            turtle.goto(95,15)


def main():
    turtle.speed(20)
    turtle.hideturtle()
    turtle.title("Circle Fractal")

    axiom = 'A'
    iterations = 3

    l_system_string = generate_l_system(axiom, iterations)

    draw_fractal(l_system_string, 120)

    turtle.done()

if __name__ == "__main__":
    main()
