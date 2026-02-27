import turtle as t
t.color('white')
t.shape('classic')
t.Screen().setup(960, 538)
t.Screen().bgpic('c:/Users/1/Downloads/i.png')
moving_forward = False
moving_back = False
moving_left = False
moving_right = False


def step():
    global moving_forward
    moving_forward = True


def stop_forward():
    global moving_forward
    moving_forward = False


def back():
    global moving_back
    moving_back = True


def stop_back():
    global moving_back
    moving_back = False


def left():
    global moving_left
    moving_left = True


def stop_left():
    global moving_left
    moving_left = False


def right():
    global moving_right
    moving_right = True


def stop_right():
    global moving_right
    moving_right = False


def move():
    if moving_forward:
        t.forward(5)
    if moving_back:
        t.back(5)
    if moving_left:
        t.left(10)
    if moving_right:
        t.right(10)
    t.ontimer(move, 1)


t.Screen().listen()

t.Screen().onkeypress(step, 'Up')
t.Screen().onkeyrelease(stop_forward, 'Up')
t.Screen().onkeypress(back, 'Down')
t.Screen().onkeyrelease(stop_back, 'Down')
t.Screen().onkeypress(left, 'Left')
t.Screen().onkeyrelease(stop_left, 'Left')
t.Screen().onkeypress(right, 'Right')
t.Screen().onkeyrelease(stop_right, 'Right')

move()
t.done()
