import turtle
#declaration ddu variable zhou
zhou = turtle.Turtle()
zhou.pencolor()
#creation de module demi cercle

def draw(rad):
    zhou.color("blue")
    zhou.pensize(3)
    for i in range(2):

       zhou.circle(rad, 90)



zhou.penup()
zhou.forward(200)
zhou.pendown()
zhou.left(180)
zhou.seth(90)




for m in range(3):
        draw(90)

        zhou.left(180)
#manipulation et ajustement

zhou.right(90)
zhou.forward(541)
zhou.left(180)
zhou.forward(30)
zhou.right(90)
zhou.forward(65)
zhou.left(180)
zhou.forward(65)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(84)
zhou.left(180)
zhou.forward(84)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(90)
zhou.left(180)
zhou.forward(90)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(84)
zhou.left(180)
zhou.forward(84)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(65)
zhou.left(180)
zhou.forward(65)
zhou.right(90)
zhou.forward(62)
zhou.right(90)
zhou.forward(66)
zhou.left(180)
zhou.forward(66)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(84)
zhou.left(180)
zhou.forward(84)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(90)
zhou.left(180)
zhou.forward(90)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(84)
zhou.left(180)
zhou.forward(84)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(66)
zhou.left(180)
zhou.forward(66)
zhou.right(90)
zhou.forward(62)
zhou.right(90)
zhou.forward(67)
zhou.left(180)
zhou.forward(67)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(84)
zhou.left(180)
zhou.forward(84)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(90)
zhou.left(180)
zhou.forward(90)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(84)
zhou.left(180)
zhou.forward(84)
zhou.right(90)
zhou.forward(30)
zhou.right(90)
zhou.forward(64)
zhou.left(180)
zhou.forward(64)
zhou.right(90)


zhou.right(60)
zhou.forward(40)
zhou.left(180)
zhou.forward(40)
zhou.left(180)
zhou.right(60)
zhou.right(60)
zhou.left(71)
zhou.forward(88)
zhou.right(180)
zhou.left(40)
zhou.forward(88)
zhou.right(180)
zhou.right(40)
zhou.forward(88)
zhou.right(180)
zhou.left(40)
zhou.forward(89)
zhou.right(180)
zhou.right(55)
zhou.forward(41)
zhou.left(180)
zhou.forward(42)
zhou.right(55)
zhou.left(180)
zhou.forward(62)



zhou.left(180)
zhou.right(60)
zhou.forward(40)
zhou.left(180)
zhou.forward(40)
zhou.left(60)
zhou.left(90)
zhou.right(21)
zhou.forward(88)
zhou.right(180)
zhou.left(40)
zhou.forward(88)
zhou.right(180)
zhou.right(40)
zhou.forward(88)
zhou.right(180)
zhou.left(40)
zhou.forward(89)
zhou.right(180)
zhou.right(55)
zhou.forward(41)
zhou.left(180)
zhou.forward(42)
zhou.right(55)
zhou.left(180)
zhou.forward(62)
zhou.left(180)
zhou.right(60)
zhou.forward(42)
zhou.left(180)
zhou.forward(42)
zhou.left(60)
zhou.left(90)
zhou.right(20)
zhou.forward(88)
zhou.right(180)
zhou.left(40)
zhou.forward(88)
zhou.right(180)
zhou.right(40)
zhou.forward(88)
zhou.right(180)
zhou.left(40)
zhou.forward(89)
zhou.right(180)
zhou.right(55)
zhou.forward(37)
zhou.left(180)
zhou.forward(37)
zhou.right(55)
zhou.left(180)
zhou.forward(30)
zhou.left(180)
zhou.forward(180)

#module pour pieds du pont
def pied(taille):
    zhou.color("blue", "blue")#couleur du peint et couleur de fond
    zhou.begin_fill()# debut de remplissage couleur de fond

    zhou.forward(30)
    zhou.left(90)
    zhou.forward(20)
    zhou.right(90)
    zhou.forward(20)
    zhou.left(90)
    zhou.forward(20)
    zhou.left(90)
    zhou.forward(100)
    zhou.left(90)
    zhou.forward(20)
    zhou.left(90)
    zhou.forward(20)
    zhou.right(90)
    zhou.forward(20)
    zhou.left(90)
    zhou.forward(60)
    zhou.end_fill()  # fin de remplissage
pied(5)
zhou.forward(150)
pied(5)

turtle.done()

