def setup():
    size(150, 150)
    background(300, 200, 100)
    fill(0)

def clear():
    size(150,150)
    background(300, 200, 100)
    fill(0)
    
def draw():
    if mousePressed:
        fill(250, 150, 50)
        rect(50, 50, 50, 50)
    else:
        clear() 
