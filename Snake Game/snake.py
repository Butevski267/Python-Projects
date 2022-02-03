from turtle import Screen, Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        self.all_turtles=[]
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for i in range(3):
            coordinate = -i*20
            new_turtle = Turtle(shape='square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.setx(coordinate)
            new_turtle.sety(0)
            new_turtle.speed('slowest')
            self.all_turtles.append(new_turtle)

    def move_snake(self):
        for index in range(len(self.all_turtles)-1,0,-1):
            new_x = self.all_turtles[index-1].xcor()
            new_y = self.all_turtles[index-1].ycor()
            self.all_turtles[index].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def increase_snake(self):
        if self.all_turtles[-1].heading() == LEFT:
            coordinate_x = self.all_turtles[-1].xcor() + 20
            coordinate_y = self.all_turtles[-1].ycor()
        elif self.all_turtles[-1].heading() == RIGHT:
            coordinate_x = self.all_turtles[-1].xcor() - 20
            coordinate_y = self.all_turtles[-1].ycor()
        elif self.all_turtles[-1].heading() == UP:
            coordinate_x = self.all_turtles[-1].xcor()
            coordinate_y = self.all_turtles[-1].ycor() - 20
        elif self.all_turtles[-1].heading() == DOWN:
            coordinate_x = self.all_turtles[-1].xcor()
            coordinate_y = self.all_turtles[-1].ycor() + 20

        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(coordinate_x,coordinate_y)
        new_turtle.speed('slowest')
        self.all_turtles.append(new_turtle)

    def red_color(self):
        for segment in self.all_turtles:
            segment.color('red')