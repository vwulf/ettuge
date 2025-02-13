def border(t: Turtle, a: Double) = runInBackground {
    t.setAnimationDelay(200)
    t.setPenColor(black)
    t.right()
    t.forward(1200)
    repeat(15){
        t.setFillColor(red)
        t.turn(a)
        t.forward(40)
        t.turn(a)
        t.forward(40)
        t.turn(a)

        t.setFillColor(blue)
        t.turn(a)
        t.forward(40)
        t.turn(a)
        t.forward(40)
        t.turn(a)
    }
    t.invisible()
}

def flower(t:Turtle, c:Color) = runInBackground {
    t.setAnimationDelay(20)
    t.setPenColor(black)
    t.setFillColor(c)
    repeat(4){
        t.right()
        repeat(90){
            t.turn(-2)
            t.forward(15)
        }
    }
    t.invisible()
}

clear()
// when drawing with multiple turtles running in the background
// don't ask the default turtle to do any work
// just hide it
// see TurtleMania sample for reasons
invisible()

val t1=newTurtle(-600,-150)
val t2=newTurtle(-600, 150)

/*
border(t1,120)
border(t2,-120)
*/


val centerT = newTurtle(0, 0)
runInBackground 
{
    import centerT._
    jumpTo(-4000,-1000)
    setAnimationDelay(20)
    setPenColor(black)
    setFillColor(cyan)
    turn(-55)
    repeat(5){
        turn(-200)
        repeat(90){
            turn(-2)
            forward(20)
        }
    }
    repeat(6){
        turn(-200)
        repeat(90){
            turn(-2)
            forward(20)
        }
    }
    turn(-80)
    repeat(5){
        turn(180)
        repeat(90){
            turn(-2)
            forward(20)
        }
    }
    invisible()
}


val t3=newTurtle(-3000,1000)
val t4=newTurtle(-4000,0)
val t5=newTurtle(-1000,1000)
val t6=newTurtle(-1500,0)

val t7=newTurtle(2000,1000)
val t8=newTurtle(500,0)
val t9=newTurtle(1000,1000)
val t10=newTurtle(0,0)


flower(t3, orange)
flower(t4, yellow)
flower(t5, red)
flower(t6, purple)

flower(t7, orange)
flower(t8, yellow)
flower(t9, red)
flower(t10, purple)
