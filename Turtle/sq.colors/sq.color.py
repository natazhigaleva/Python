import turtle
def sq(a):
    for i in range(4):
        joe.color(colors[i%4])
        joe.forward(a)
        joe.left(90)
colors = ['red', 'yellow', 'purple', 'lime']
joe = turtle.Turtle()
joe.speed(200)
length = 30
for i in range(60):
    sq(length)
    joe.right(10)
    length = length + 5