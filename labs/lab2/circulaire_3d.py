import turtle
from math import sin, cos, pi

def draw_3d_circle_fractal(x, y, size, depth, count):
    if depth == 0:
        return
    else:
        turtle.circle(size)
        turtle.forward(size)
        turtle.left(45)
        draw_3d_circle_fractal(x, y, size / 2, depth - 1, count)
        turtle.right(90)
        draw_3d_circle_fractal(x, y, size / 2, depth - 1, count)
        turtle.left(45)
        turtle.backward(size)

def three_d_main():
    turtle.speed(2000)
    turtle.hideturtle()
    turtle.title("3D Circle Fractal")

    x, y, initial_size, initial_depth, circles_count = 0, 0, 100, 3, 6

    draw_3d_circle_fractal(x, y, initial_size, initial_depth, circles_count)

    turtle.update()
    turtle.mainloop()

if __name__ == "__main__":
    three_d_main()
