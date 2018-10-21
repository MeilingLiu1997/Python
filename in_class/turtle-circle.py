import turtle


def drawPolygon(t, sideLength, numSides):
    for i in range(6):
        t.forward(sideLength)
        t.left(numSides)


def main():
    wn = turtle.Screen()
    wn.bgcolor("Lightgreen")

    alex = turtle.Turtle()
    drawPolygon(alex, 150, 60)

    drawCircle(alex, 150)
    wn.exitonclick()


def drawCircle(t, radius):
    t.circle(radius)


main()
