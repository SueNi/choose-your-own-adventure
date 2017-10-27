import turtle
import time
import os


def main():
    wn = turtle.Screen()
    t = turtle.Turtle()

    t.up()
    t.goto(-500, 380)
    t.down()
    t.write("\nA story of Snow White\n "
            "Choose your own own adventure!", font=("Times New Roman", 70))
    time.sleep(1)
    wn.clear()
    t.up()
    t.goto(-500, 200)
    t.down()
    t.write("\nOnce upon a time, in the kingdom of math, there was a smart princess named Snow White"
            "\nShe has a evil step mother, the Queen, who is always jealous of her smartness."
            "\nThe Queen wanted to kill Snow White to become the smartest person in the kingdom."
            "\nA maid heard it and told Snow White, so she ran away."
            "\nHowever, she got lost in the forest."
            "\nWhile she was searching for a road, she saw two sign."

            "\nOne sign says Geometry and the other says algebra."
            "\nShe then realized that these are the entrances for the field of geometry and algebra."
            "\nShe loves both subject, so she couldn't decide which to go in. Please help her. ",
            font=("Times New Roman", 30))
    time.sleep(10)
    wn.clear()

    t.up()
    t.goto(-500, 220)
    t.down()
    t.write("\nChoose a field", align="left", font=("Times New Roman", 30, "normal"))
    t.up()
    t.goto(-500, 180)
    t.down()
    t.write("1. Geometry   2. Algebra  ", align="left", font=("Times New Roman", 30, "normal"))
    choice = input("Make your choice: ")

    def alg():
        t.write("\nSnow White ran into the field of Algebra."
                "\nIn there, she saw a cottage. This is where the 7 mathematicians live."
                "\nA lot of people want to meet them, but they don't have time."
                "\nThey set three math questions at the door, only people who answer it correctly can enter"
                "\nHowever, they didn't want it to be too hard, so there are at least different kinds of questions. "
                "\nIn algebra,there are 3 types: equations,functions,or polynomials", font=("Times New Roman", 30))
        time.sleep(2)
        t.up()
        t.goto(-500, -60)
        t.down()
        t.write("Which type of questions would you like to answer?", align="left",
                font=("Times New Roman", 30, "normal"))
        t.up()
        t.goto(-500, -100)
        t.down()
        t.write("1. Equations    2. Functions    3. Polynomials", font=("Times New Roman", 30))

    def geo():
        t.write("\nSnow White ran into the field of Geometry."
                "\nIn there, she saw a cottage. This is where the 7 mathematicians live."
                "\nA lot of people want to meet them, but they don't have time."
                "\nThey set three math questions at the door, only people who answer it correctly can enter"
                "\nHowever, they didn't want it to be too hard, so there are at least different kinds of questions. "
                "\nIn geometry,there are 3 types: circles, other shapes, and trigonometry",
                font=("Times New Roman", 30))
        time.sleep(2)
        t.up()
        t.goto(-500, -40)
        t.down()
        t.write("Which type of questions would you like to answer?", align="left",
                font=("Times New Roman", 30, "normal"))
        t.up()
        t.goto(-500, -80)
        t.down()
        t.write("1. Circles    2. Other shapes    3.Trigonometry", font=("Times New Roman", 30))

    t.up()
    t.goto(-500, -20)
    t.down()
    if choice == 2:
        alg()
    else:
        geo()

    question = input("Choose 1, 2 or 3: ")

    wn.clear()

    t.up()
    t.goto(-500, 250)
    t.down()

    def l1():
        t.write("The sum of 3 numbers is 12. The sum of the first and second numbers is 10, and \n"
                "the first number is 3 times the third number. Find the numbers.", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 200)
        t.down()
        t.write("1. (6,4,2)    2. (2,4,6)    3.(9,3,0)", font=("Times New Roman", 30))

    def l4():
        t.write("f(x) = -2x+4, what is f(y+z)", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 200)
        t.down()
        t.write("1. 4-2x-2y   2. 4-2x+2y    3.4+2x-2y", font=("Times New Roman", 30))

    def l7():
        t.write("Expand: (3x+5y)^2", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 200)
        t.down()
        t.write("1. 9x^2 + 30xy + 25y^2    2. 9x^2 + 25y^2     3.9x^2 + 15xy + 25y^2", font=("Times New Roman", 30))

    def l10():
        t.write("Write the equation for a circle with a diameter of 38 cm and is centered at (6, 7)",
                font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 200)
        t.down()
        t.write("1. (x-6)^2 + (y-7)^2 = 361    2. (x+6)^2 + (y+7)^2 = 361     3.(x-6)^2 + (y-7)^2 = 1444  ",
                font=("Times New Roman", 30))

    def l13():
        t.write("What's the volume of a sphere with a radius of 2.8 cm", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 200)
        t.down()
        t.write("1. 91.95 cm  2. 98.52 cm   3.95.45 cm ", font=("Times New Roman", 30))

    def l16():
        t.write("What is the hypotenuse of a right triangle with sides 63 cm and 84 cm", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 200)
        t.down()
        t.write("1. 105 cm     2. 73.5 cm     3. 115 cm ", font=("Times New Roman", 30))

    if question == 1 and choice == 2:
        l1()
    elif question == 2 and choice == 2:
        l4()
    elif question == 3 and choice == 2:
        l7()
    elif question == 1 and choice == 1:
        l10()
    elif question == 2 and choice == 1:
        l13()
    else:
        l16()

    def l2():
        t.goto(-500, 100)
        t.down()
        t.write(" Solve: 5|y+6| = 20 ", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 50)
        t.down()
        t.write("1. (-2)   2. (4,6)   3.(-2,-10)   ", font=("Times New Roman", 30))

    def l3():
        t.up()
        t.goto(-500, -50)
        t.down()
        t.write(" Solve: x^2 - 4x - 5 = 0 ", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, -100)
        t.down()
        t.write("1. (1, -5)   2. (5, -1)   3.(5, 1) ", font=("Times New Roman", 30))

    def l5():
        t.up()
        t.goto(-500, 100)
        t.down()
        t.write(" Find the slope for (-1,4), (-1,-2) ", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 50)
        t.down()
        t.write("1. m = -2   2.  m = 0   3.undefined   ", font=("Times New Roman", 30))

    def l6():
        t.up()
        t.goto(-500, -50)
        t.down()
        t.write(" What is the equation of a line that passes through (3,1) and is perpendicular to y = -x+2  ",
                font=("Times New Roman", 30))
        t.up()
        t.goto(-500, -100)
        t.down()
        t.write("1. y = 2x   2. y = x - 2  3. y = x + 2    ", font=("Times New Roman", 30))

    def l8():
        t.up()
        t.goto(-500, 100)
        t.down()
        t.write(" Factor: x^2 + 2x + xy + 2y ", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 50)
        t.down()
        t.write("1. (x+y)(2x)   2. (x+y)(y+2)   3.(x+2)(x+y)   ", font=("Times New Roman", 30))

    def l9():
        t.up()
        t.goto(-500, -50)
        t.down()
        t.write(" Divide: 2x^2 - 5x + 6 / x - 3", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, -100)
        t.down()
        t.write("1.2x+1 + 9   2. 2x+1 + 9/x-3   3.2x+1   ", font=("Times New Roman", 30))

    def l11():
        t.up()
        t.goto(-500, 100)
        t.down()
        t.write(" Right triangle ABC is inscribed in Circle O, AB is a diameter of circle O\n"
                "If angle ABC = 37, what is the measure of angle BAC?", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 50)
        t.down()
        t.write("1. 43   2. 143   3.53   ", font=("Times New Roman", 30))

    def l12():
        t.up()
        t.goto(-500, -50)
        t.down()
        t.write(" What is the area of a 162-degree-sector that has a radius of 7 cm", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, -100)
        t.down()
        t.write("1. 19.79  2. 69.27   3.33.79  ", font=("Times New Roman", 30))

    def l14():
        t.up()
        t.goto(-500, 100)
        t.down()
        t.write(" What is the surface area of a square pyramid with sides of 8 cm and slant height of 5 cm ",
                font=("Times New Roman", 30))
        t.up()
        t.goto(-500, 50)
        t.down()
        t.write("1. 64   2. 107   3. 144  ", font=("Times New Roman", 30))

    def l15():
        t.up()
        t.goto(-500, -50)
        t.down()
        t.write(" Area of pentagon with side length of 12 cm ", font=("Times New Roman", 30))
        t.up()
        t.goto(-500, -100)
        t.down()
        t.write("1. 60   2. 247,75   3.495.5  ", font=("Times New Roman", 30))

    def l17():
        t.up()
        t.goto(-500, 100)
        t.down()
        t.write(" Refer to the image below, how long is AC?  ", font=("Times New Roman", 30))
        x = turtle.Turtle()
        x.tracer(3)
        wn.addshape(os.path.expanduser("AM.gif"))
        x.shape(os.path.expanduser("AM.gif"))
        x.penup()
        x.goto(400, 100)
        x.pendown()
        t.up()
        t.goto(-500, 50)
        t.down()
        t.write("1. 12*(3**0.5)  2. 8   3.12   ", font=("Times New Roman", 30))

    def l18():
        t.up()
        t.goto(-500, -50)
        t.down()
        t.write(" Refer to the image below, what is BC? ", font=("Times New Roman", 30))
        x = turtle.Turtle()
        x.tracer(3)
        wn.addshape(os.path.expanduser("A.gif"))
        x.shape(os.path.expanduser("A.gif"))
        x.penup()
        x.goto(400, -50)
        x.pendown()
        t.up()
        t.goto(-500, -100)
        t.down()
        t.write("1. 5.44   2. 4.96   3. 6.32   ", font=("Times New Roman", 30))

    one = input("The answer is ")

    t.up()
    t.goto(-500, 150)
    t.down()
    if one == 1:
        t.write("Correct!", font=("Times New Roman", 30))
        time.sleep(1)
    else:
        t.write("Game over, Snow White died.", font=("Times New Roman", 50))
        wn.exitonclick()

    if one == 1 and question == 1 and choice == 2:
        l2()

    if one == 1 and question == 2 and choice == 2:
        l5()

    if one == 1 and question == 3 and choice == 2:
        l8()

    if one == 1 and question == 1 and choice == 1:
        l11()

    if one == 1 and question == 2 and choice == 1:
        l14()

    if one == 1 and question == 3 and choice == 1:
        l17()

    two = input("The answer is ")

    t.up()
    t.goto(-500, 0)
    t.down()
    if two == 3:
        t.write("Correct!", font=("Times New Roman", 30))
        time.sleep(1)
    else:
        t.write("Game over, Snow White died.", font=("Times New Roman", 50))
        wn.exitonclick()

    if two == 3 and question == 1 and choice == 2:
        l3()

    if two == 3 and question == 2 and choice == 2:
        l6()

    if two == 3 and question == 3 and choice == 2:
        l9()

    if two == 3 and question == 1 and choice == 1:
        l12()

    if two == 3 and question == 2 and choice == 1:
        l15()

    if two == 3 and question == 3 and choice == 1:
        l18()

    three = input("The answer is ")

    t.up()
    t.goto(-500, -150)
    t.down()
    if three == 2:
        t.write("Correct!", font=("Times New Roman", 30))
        time.sleep(1)

    else:
        t.write("Game over, Snow White died.", font=("Times New Roman", 50))
        wn.exitonclick()

    wn.clear()

    t.up()
    t.goto(-500, -100)
    t.down()
    t.write("\nSnow White successfully answered the questions with your help."
            "\nShe entered the house and became a good friend of the seven mathematicians"
            "\nThe Queen heard about it and challenged her with math questions."
            "\nBut the 7 mathematicians helped and defeated the queen, and she died.", font=("Times New Roman", 30))
    time.sleep(2)
    wn.clear()

    t.up()
    t.goto(-500, -100)
    t.down()
    t.write("\nOne day, a prince came by and asked Snow White a math question"
            "\nSnow White answered it perfectly, so the prince fell in love with her"
            "\nAt last, Snow White and the Prince did math everyday and  lived happily ever after."
            "\nThe end", font=("Times New Roman", 30))

    t.up()
    t.goto(-500, 250)
    t.down()

    time.sleep(2)

    wn.exitonclick()


main()
