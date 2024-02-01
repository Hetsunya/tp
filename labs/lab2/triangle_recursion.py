import turtle

def draw_sierpinski_triangle(turtle, order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        size /= 2
        draw_sierpinski_triangle(turtle, order - 1, size)
        turtle.forward(size)
        draw_sierpinski_triangle(turtle, order - 1, size)
        turtle.backward(size)
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)
        draw_sierpinski_triangle(turtle, order - 1, size)
        turtle.left(60)
        turtle.backward(size)
        turtle.right(60)

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(2)
    fractal_turtle.penup()
    fractal_turtle.goto(-150, -150)
    fractal_turtle.pendown()

    order = int(input("Введите порядок фрактала (целое число): "))
    size = 300

    draw_sierpinski_triangle(fractal_turtle, order, size)

    window.exitonclick()

if __name__ == "__main__":
    main()
