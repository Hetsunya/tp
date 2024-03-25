import turtle

def apply_rules(s):
    return s.replace('F', 'FF+F+F+F+FF')

def draw_fractal(turtle, iterations, length):
    axiom = 'F+F+F+F'
    s = axiom
    for _ in range(iterations):
        s = apply_rules(s)
    for char in s:
        if char == 'F':
            turtle.forward(length)
        elif char == '+':
            turtle.right(90)

def main():
    # Настройки рисования
    iterations = 6
    length = 10

    # Настройки экрана
    screen = turtle.Screen()
    screen.setup(width=700, height=700)
    screen.bgcolor("white")

    # Создание черепашки
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(3)
    fractal_turtle.penup()
    fractal_turtle.goto(-length * 1.5, -length * 0.5)
    fractal_turtle.pendown()

    # Рисование кругового фрактала
    draw_fractal(fractal_turtle, iterations, length)

    # Закрытие экрана по клику
    screen.exitonclick()

if __name__ == "__main__":
    main()
