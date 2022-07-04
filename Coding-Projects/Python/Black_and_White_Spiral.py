import turtle;

trl = turtle.Pen();

colors = ["black","white"];
for x in range(1000):
    trl.speed(500);
    trl.width(5);
    trl.color(colors[x%2]);
    turtle.bgcolor("yellow")
    trl.left(100);
    trl.forward(x);