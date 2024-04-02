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
    length = 0.5

    # Настройки экрана
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)
    screen.bgcolor("white")

    # Создание черепашки
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(0)  # Максимальная скорость
    fractal_turtle.penup()
    fractal_turtle.goto(-length * 1.5, -length * 0.5)
    fractal_turtle.pendown()

    # Отключение анимации
    turtle.tracer(0, 0)

    # Рисование кругового фрактала
    draw_fractal(fractal_turtle, iterations, length)

    # Обновление экрана
    turtle.update()

    # Закрытие экрана по клику
    screen.exitonclick()


if __name__ == "__main__":
    main()
