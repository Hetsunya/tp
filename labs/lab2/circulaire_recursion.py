import turtle

def draw_circle_fractal(turtle, radius, depth):
    if depth == 0:
        return
    else:
        for _ in range(7):
            turtle.circle(radius)
            turtle.up()
            turtle.forward(radius * 2)
            turtle.down()
            draw_circle_fractal(turtle, radius / 3, depth - 1)
            turtle.up()
            turtle.backward(radius * 2)
            turtle.left(360 / 7)
            turtle.down()

def main():
    turtle.speed(2000)
    turtle.hideturtle()
    turtle.title("Circle Fractal")

    initial_radius = 100
    initial_depth = 3

    draw_circle_fractal(turtle, initial_radius, initial_depth)

    turtle.done()

if __name__ == "__main__":
    main()
