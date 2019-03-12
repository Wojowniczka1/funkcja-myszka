def setup():
    size(150, 150)
    background(200)
    fill(0)

def draw():
    if mousePressed:
        fill(0)
        line(10, 40, 70, 100)
    else :
        fill(130)
        rect(10, 10, 30, 30)
