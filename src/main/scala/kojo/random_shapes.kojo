clear()
setSpeed(medium) // speed up the turtle
setPenColor(cm.purple)
var clr = cm.rgba(255, 0, 0, 127) // start with a semi transparent red color

def shape(step: Int, rep: Int, sides: Int) = {
repeat(rep) {
    setFillColor(clr)
    repeat(sides) {
        forward(step)
        right(360/sides)
    }
    clr = clr.spin(360 / rep) // change color hue
    right(360 / rep)
}
forward(random(-300, 300))
right(random(90))    
}

repeat(20) {
    shape(random(100), random(20), random(9))
}
