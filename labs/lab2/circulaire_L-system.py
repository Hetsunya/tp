import turtle
import math

def apply_l_system(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        next_result = ""
        for ch in result:
            next_result += rules.get(ch, ch)
        result = next_result
    return result

def draw_circle_fractal_l_system(x, y, size, iterations):
    axiom = "F"
    rules = {"F": "F+F-F-F+F"}

    l_system_string = apply_l_system(axiom, rules, iterations)

    for command in l_system_string:
        if command == "F":
            turtle.forward(size)
        elif command == "+":
            turtle.left(90)
        elif command == "-":
            turtle.right(90)

def l_system_main():
    turtle.speed(20000000)
    turtle.hideturtle()
    turtle.title("L-System Circle Fractal")

    x, y, initial_size, iterations = 0, 0, 5, 4

    draw_circle_fractal_l_system(x, y, initial_size, iterations)

    turtle.update()
    turtle.mainloop()

if __name__ == "__main__":
    l_system_main()
