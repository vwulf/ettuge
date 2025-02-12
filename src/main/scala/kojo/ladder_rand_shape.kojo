// Start writing your Kojo code here
clear()
showAxes()
setSpeed(medium) // speed up the turtle
setPenColor(cm.purple)
var clr = cm.rgba(255, 0, 0, 127) // start with a semi transparent red color

def shape(step: Int, rep: Int, sides: Int) = {
    repeat(rep) {
        setFillColor(clr)
        repeat(sides) {
            forward(step)
            right(360 / sides)
        }
        clr = clr.spin(360 / rep) // change color hue
        right(360 / rep)
    }
    forward(random(0, 300))
    right(random(90))
    ladder(10)
}

def square(n: Int) {
    repeat(4) {
        forward(n)
        right(90)
    }
}

def ladder(n: Int) {
    repeat(n) {
        setPenColor(randomColor)
        square(50)
        forward(50)
    }
}

def rings(n: Int) {
    repeat(n) {
        setSpeed(fast)
        forward(100)
        back(200)
        right(10)
        setSpeed(medium)
        back(50)
        hop(150)
        forward(20)
        setPenColor(randomColor)
        //setBackground(randomColor)
        circle(25)
        
    }
}
//clear()

def spir() = {
    setSpeed(fast)
    repeat(180) {
        setPenColor(randomColor)
        forward(100)
        hop(-100)
        right(2)
    }
}

def worm() = {
    repeat(1) {
        spir()
        forward(100)
    }
}

repeat(1) {
    worm()
    back(300)
    right(90)
    square(40)
    circle(25)
    rings(5)
    repeat(20) {
       shape(random(100), random(20), random(9))
    }

}

//rings(10)

/*
forward(100)
back(200)
right(90)
//setSpeed(medium)
back(50)
hop(150)

forward(20)
*/
//square(100)

//rings(20)