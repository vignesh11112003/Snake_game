from turtle import Turtle

starting_position=[(0,0),(-20,0),(-40,0)]
distance=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]



    def create_snake(self):

        for s in starting_position:
            self.add_segment(s)
    def add_segment(self,s):
        segment1 = Turtle()
        segment1.shape("square")
        segment1.color("white")
        segment1.penup()
        segment1.goto(s)
        self.segments.append(segment1)
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(new_x, new_y)
        self.head.forward(distance)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)