import turtle

def apply_rules(ch):
    if ch == 'F':
        return 'F+F-F-F+F'

def generate_l_system(axiom, iterations):
    result = axiom
    for _ in range(iterations):
        new_result = ""
        for ch in result:
            new_result += apply_rules(ch) if apply_rules(ch) else ch
        result = new_result
    return result

def draw_l_system(turtle, instructions, angle, distance):
    for command in instructions:
        if command == 'F':
            turtle.forward(distance)
        elif command == '+':
            turtle.left(angle)
        elif command == '-':
            turtle.right(angle)

def l_system_main():
    turtle.speed(2000)
    turtle.hideturtle()
    turtle.title("L-System Circle Fractal")

    axiom = 'F+F-F-F+F'
    iterations = 3
    angle = 90
    distance = 10

    instructions = generate_l_system(axiom, iterations)
    draw_l_system(turtle, instructions, angle, distance)

    turtle.done()

if __name__ == "__main__":
    l_system_main()
