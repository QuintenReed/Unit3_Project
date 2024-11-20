"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""

# Quinten Reed
# U3 Project
# Recursive Tree

import turtle
from random import randint

t = turtle.Turtle()

def draw_branch(angle, length, pensize):
  branches = 2 #randint(0, 2)

  if length > 0:
    t.pensize(pensize)
    t.color('#744E2A')

    if branches >= 1:
      t.left(angle)
      t.forward(length)
      draw_branch(randint(15, 25), length-10, pensize-1)
      t.backward(length)
      t.pensize(pensize)
      t.color('#744E2A')
      t.right(angle)

    if branches >= 2:
      t.right(angle)
      t.pensize(pensize)
      t.forward(length)
      draw_branch(randint(15, 25), length-10, pensize-1)
      t.backward(length)
      t.pensize(pensize)
      t.color('#744E2A')
      t.left(angle)
  else:
    t.pensize(10)
    t.color('green')

    if branches >= 1:
      t.left(angle)
      t.forward(length)
      t.backward(length)
      t.right(angle)

    if branches >= 2:
      t.right(angle)
      t.forward(length)
      t.backward(length)
      t.left(angle)

def main():
  t.speed(1000)
  t.pensize(10)
  t.color('#744E2A')
  t.left(90)
  t.forward(100)
  draw_branch(randint(15, 25), 90, 9)

  turtle.mainloop()

if __name__ == "__main__":
  main()