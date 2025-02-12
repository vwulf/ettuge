// Start writing your Kojo code here
clear()
showAxes()
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
  ladder(10)
}
}
clear()

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
repeat(3) {
  spir()
  forward(100)  
}
}

repeat(4) {
worm()
back(300)
right(90)
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
