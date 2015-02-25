import turtle
from threading import Thread

class TurtleReplay():
    _full = (87, 87, 87)
    _transparent = (0, 0, 0)

    def __init__(self, t, scr):
        self.movements = []
        self.watching = False
        self.reseting = False
        self.t = t
        self.follow_turtle = turtle.Turtle()
        self.follow_turtle.hideturtle()
        self.follow_turtle.penup()
        self.follow_turtle.shape(self.t.shape())
        self.follow_turtle.color("grey34")
        self.follow_turtle.speed(self.t.speed())
        self.scr = scr
        self.scr.onkey(self.reset, "r")
        self.scr.onkey(self.replay, "w")
        self.scr.listen()
        self.monitor()

    def reset(self):
        if not (self.watching or self.reseting):
            self.reseting = True
            self.t.clear()
            self.t.penup()
            self.t.home()
            self.t.pendown()
            self.movements = []
            self.reseting = False

    def monitor(self):
        if not (self.watching or self.reseting):
            self.movements.append({'position': self.t.pos(),
                                   'direction': self.t.heading()})
        self.scr.ontimer(self.monitor, 50)

    def replay(self):
        if not (self.watching or self.reseting):
            self.watching = True
            self.follow_turtle.setpos(self.movements[0]['position'])
            self.follow_turtle.setheading(self.movements[0]['direction'])
            self.follow_turtle.showturtle()
            for i in self.movements:
                self.follow_turtle.setpos(i['position'])
                self.follow_turtle.setheading(i['direction'])
            self.follow_turtle.hideturtle()
            self.watching = False

    def getWatching(self):
        return self.watching

    def getReseting(self):
        return self.reseting

if __name__ == "__main__":
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green4")
    scr = turtle.Screen()
    replay = TurtleReplay(t, scr)

    def fwd(not_used):
        if not (replay.getWatching() or replay.getReseting()):
            t.forward(10)
    def bwd(not_used):
        if not (replay.getWatching() or replay.getReseting()):
            t.backward(10)
    def left(not_used):
        if not (replay.getWatching() or replay.getReseting()):
            t.left(10)
    def right(not_used):
        if not (replay.getWatching() or replay.getReseting()):
            t.right(10)

    scr.getcanvas().bind("<Up>", fwd)
    scr.getcanvas().bind("<Down>", bwd)
    scr.getcanvas().bind("<Left>", left)
    scr.getcanvas().bind("<Right>", right)
    scr.listen()

    turtle.mainloop()