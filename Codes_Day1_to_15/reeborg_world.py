# Codes for reborg's world
# Hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for h in range(0,6):
    hurdle()


## Hurdle 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    hurdle()

# OR
while  not at_goal():
    hurdle()

## Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        hurdle()
# OR 
while not at_goal():
    if wall_in_front:
        hurdle()
    else:
        move()

## Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()

## Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#if stuck in infinite loop issue use the statement below
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        