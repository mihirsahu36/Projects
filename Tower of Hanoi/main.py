import turtle  # Import the Turtle graphics library for visualization

size = 20  # Size of the smallest disk
tower_width = 100  # Width of the tower base
tower_height = 200  # Height of the tower
tower_radius = 5  # Radius of the tower poles
tower_distance = 250  # Distance between tower poles
tower_altitude = -100  # Altitude of the tower base

SPEED = 1  # Speed of the turtle

# Dictionary to map tower names to x-coordinates
tower_loc = {
    "A": -1,
    "B": 0,
    "C": 1
}

# Dictionary to store disks on each tower
tower_poles = {
    "A": [],
    "B": [],
    "C": []
}

# List of colors for the disks
FillColors = [
    "#d25b6a",
    "#d2835b",
    "#e5e234",
    "#83d05d",
    "#2862d2",
    "#35b1c0",
    "#5835c0"
]


def set_plate(i):
    """Create the shape for a disk."""
    l = size * (i + 2)

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)

    t.left(90)
    t.begin_poly()
    t.forward(l)
    t.circle(size, 180)
    t.forward(l * 2)
    t.circle(size, 180)
    t.forward(l)
    t.end_poly()
    p = t.get_poly()

    turtle.register_shape("plate_%s" % i, p)


def set_tower():
    """Create the shape for a tower."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)

    t.left(90)
    t.begin_poly()
    t.forward(tower_width)
    t.circle(tower_radius, 180)
    t.forward(tower_width - tower_radius)
    t.right(90)
    t.forward(tower_height)
    t.circle(tower_radius, 180)
    t.forward(tower_height)
    t.right(90)
    t.forward(tower_width - tower_radius)
    t.circle(tower_radius, 180)
    t.forward(tower_width)
    t.end_poly()
    p = t.get_poly()
    turtle.register_shape("tower", p)


def draw_towers():
    """Draw the three towers."""
    set_tower()
    tower = turtle.Turtle("tower")
    tower.speed(0)
    tower.penup()
    tower.goto(-tower_distance, tower_altitude)
    tower.stamp()
    tower.goto(0, tower_altitude)
    tower.stamp()
    tower.goto(tower_distance, tower_altitude)


def draw_plates(pn):
    """Draw the given number of plates on the first tower."""
    plates = []
    for i in range(pn):
        set_plate(i)
        _p = turtle.Turtle('plate_%s' % i)
        _p.penup()
        _p.speed(SPEED)
        _colorIdx = i % len(FillColors)
        _color = FillColors[_colorIdx]
        _p.color(_color, _color)
        plates.append(_p)

    return plates


def draw_move(plate, fromPole, toPole, move_number):
    """Animate moving a disk from one tower to another."""
    to_x = tower_loc[toPole] * tower_distance
    toPole_count = len(tower_poles[toPole])
    to_y = tower_altitude + 2 * tower_radius + toPole_count * size * 2 - 30  # Adjusted to display below the rod

    if fromPole:
        tower_poles[fromPole].remove(plate)
        from_x = tower_loc[fromPole] * tower_distance
        plate.goto(from_x, tower_height)
        plate.goto(to_x, tower_height)

    plate.goto(to_x, to_y)
    tower_poles[toPole].append(plate)

    turtle.undo()
    turtle.penup()
    turtle.goto(0, -tower_height - 50)  # Adjusted to display below the rods
    turtle.write(f"Move {move_number}: Moved plate from {fromPole} to {toPole}", align="center",
                 font=("Arial", 30, "normal"))


def moveTower(height, fromPole, withPole, toPole, plates, move_number):
    """Recursive function to move a tower of disks from one pole to another."""
    if height == 1:
        draw_move(plates[0], fromPole, toPole, move_number)
        return 1, move_number + 1
    else:
        moves, move_number = moveTower(height - 1, fromPole, toPole, withPole, plates, move_number)
        moves += 1
        draw_move(plates[height - 1], fromPole, toPole, move_number)
        moves, move_number = moveTower(height - 1, withPole, fromPole, toPole, plates, move_number + 1)
        return moves + 1, move_number


if __name__ == '__main__':
    turtle.setup(width=800, height=600)  # Set up the turtle window
    draw_towers()  # Draw the towers
    n = int(turtle.textinput("Tower of Hanoi", "Enter the number of disks: "))  # Get the number of disks from user input
    plates = draw_plates(n)  # Draw the disks on the first tower

    for i in range(n):  # Move all disks to the first tower
        draw_move(plates[n - 1 - i], '', 'A', 1)

    total_moves, _ = moveTower(n, 'A', 'B', 'C', plates, 1)  # Move the tower from 'A' to 'C'
    total_moves = 2 ** n - 1  # Calculate the total number of moves using the formula 2^n - 1
    turtle.undo()  # Remove the initial message
    turtle.goto(0, -tower_height - 50)  # Adjust the position to display the total moves
    turtle.write(f"Total moves: {total_moves}", align="center", font=("Arial", 30, "normal"))  # Display the total moves

    turtle.mainloop()  # Start the main event loop to keep the window open
