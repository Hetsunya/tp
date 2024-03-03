import turtle

def apply_rule(ch):
    if ch == 'A':
        return 'F-F-F-F-F-F-Cf'
    elif ch == 'F':
        return 'Ff+Ff+Ff+Ff+Ff+Ff+C'
    elif ch == 'f':
        return 'f'
    elif ch == 'C':
        return 'C'
    else:
        return ch

def generate_l_system(axiom, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join(apply_rule(ch) for ch in result)
    return result

def draw_l_system(turtle, instructions, angle, length, distance_between_c_and_f):
    count = 1
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
            if count == 6:
                turtle.penup()
                turtle.forward(15)
                turtle.pendown()
                count = 0
            else:
                count += 1
                turtle.penup()
                turtle.forward(distance_between_c_and_f)
                turtle.pendown()

def main():
    turtle.speed(200)
    turtle.hideturtle()
    turtle.title("Modified L-System Fractal")

    axiom = 'A'
    iterations = 4
    angle = 30
    length = 20
    distance_between_c_and_f = 60

    l_system = generate_l_system(axiom, iterations)
    print(l_system)
    draw_l_system(turtle, l_system, angle, length, distance_between_c_and_f)

    turtle.done()

if __name__ == "__main__":
    main()
