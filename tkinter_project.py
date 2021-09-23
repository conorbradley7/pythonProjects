from tkinter import *
import random
from time import *
from random import randint

class Shape(object):
    def __init__(self):
        self._x = random.randint(1, 420)
        self._y = random.randint(1, 420)
        self._time = time()

    def getX(self):
        return self._x

    def setX(self):
        raise NotImplementedError("Not implemented")

    def getY(self):
        return self._y

    def setY(self):
        raise NotImplementedError("Not implemented")

    def getTime(self):
        return self._time

    def setTime(self):
        raise NotImplementedError("Not implemented")

    x = property(getX)
    y = property(getY)
    time = property(getTime)

class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        self._size = randint(30,70)
        global colour
        colour = random.choice(score._colour_list)
        self._square = canvas.create_polygon(self._x, self._y, self._x + self._size, self._y, self._x + self._size, 
                                                    self._y + self._size, self._x,self._y + self._size, fill=colour)
        global square_create_time
        square_create_time = self._time
        start_button.destroy()
        canvas.tag_bind(self._square, "<ButtonPress-1>", click)
       
    def getSize(self):
        return self._size

    def setSize(self):
        raise NotImplementedError("Not implemented")

    size = property(getSize)



class Score(object):
    def __init__(self):
        self._score = 1
        self._level = 1
        self._time_allowed = 5
        self._scoreLabel = Label(text=str(self._score))
        self._levelLabel = Label(text=str(self._level))
        self._colour_list = ["green"]
    

    def getScore(self):
        return self._score

    def setScore(self):
        raise NotImplementedError("Not implemented")

    def plus1point(self):
        self._score += 1
        if self._score == 10:
            self._colour_list.append("red")
        if self._score == 20:
            self._colour_list.append("green")
            self._colour_list.append("green")
            self._colour_list.append("green")
            self._colour_list.append("red")
            self._colour_list.append("red")
            self._colour_list.append("red")
            self._colour_list.append("gold")

        if self._score % 10 == 0:
            self._level += 1
            if self._time_allowed > 1:
                self._time_allowed -= 1
            if self._time_allowed == 0:
                game_over()
        clock._time = self._time_allowed
        

    def penalty(self):
        self._score -= 5
        self._time_allowed -= 1
        clock._time = self._time_allowed
        if self._time_allowed <= 0:
            game_over()
        elif self._score <= 0:
            self._score = 0
            game_over()

    def labelRefresh(self):
        self._levelLabel.configure(text='Level: {}'.format(self._level), font=("Ariel", 18))
        self._scoreLabel.configure(text='Score: {}'.format(self._score), font=("Ariel", 18))
        self._levelLabel.pack()
        self._scoreLabel.pack()
        
    score = property(getScore)

class Timer:
    def __init__(self):
        self._time = 5
        self._time_label = Label(text="5s", font="Arial 30", width=10)
        self._time_label.pack()
        self.refresh_time()

    def refresh_time(self):
      
        if self._time == 0:
            evaluate()
        self._time_label.configure(text="%is" % self._time)
        self._time -= 1
        if not gameOver:
            self._countdown = self._time_label.after(1000, self.refresh_time)


    def getTime(self):
        return self._time
    def setTime(self):
        raise NotImplementedError("Not implemented")

    countdown_time = property(getTime)



def click(event):
    global click_time
    global square_create_time
    click_time = time()
    canvas.delete("all")
    canvas.after_cancel(clock._countdown)
    clock._countdown = canvas.after(0, clock.refresh_time)
    if colour == "red":
        score.penalty()
    if colour == "gold":
        score._score += 5
        score._time_allowed += 1
    elif (click_time - square_create_time) < score._time_allowed:
        score.plus1point()

    canvas.delete()
    Square()
    score.labelRefresh()

def evaluate():
    canvas.delete("all")
    if colour == "green" or colour == "gold":
        score.penalty()
    clock._time = score._time_allowed
    Square()
    score.labelRefresh()

def game_over():
    global gameOver
    gameOver = True
    canvas.delete("all")
    Button(canvas, text="Quit", font=("Ariel", 18), command=game.destroy).pack()
    
def start():
    global clock
    clock = Timer()
    Square()


game = Tk()
score = Score()
canvas = Canvas(game, width=500, height=500)
score.labelRefresh()
global gameOver
gameOver = False
canvas.pack(side=TOP)
frame = Frame(game)
start_button = Button(frame, text="Lets GOO!", font=("Ariel", 18), command=start)
start_button.grid(row=1, column=1)
frame.pack(side=BOTTOM)
canvas.pack()
game.mainloop()


