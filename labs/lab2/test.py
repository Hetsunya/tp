import turtle

def apply_rules(axiom):
    new_string = ""
    for char in axiom:
        if char == "F":
            new_string += "F+F--F+F"
        else:
            new_string += char
    return new_string

def draw_l_system(t, axiom, angle, distance):
    for char in axiom:
        if char == "F":
            t.forward(distance)
        elif char == "+":
            t.left(angle)
        elif char == "-":
            t.right(angle)

def main():
    t = turtle.Turtle()
    t.speed(200)  # Fastest speed
    t.hideturtle()

    axiom = "F"
    angle = 60
    distance = 5
    iterations = 4  # Adjust for complexity

    for _ in range(iterations):
        axiom = apply_rules(axiom)

    draw_l_system(t, axiom, angle, distance)

    turtle.done()

if __name__ == "__main__":
    main()