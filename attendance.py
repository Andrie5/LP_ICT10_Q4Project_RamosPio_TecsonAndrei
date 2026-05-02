import numpy as np, matplotlib.pyplot as plt
from pyscript import document, window

# creates x-axis positions for Monday to Friday
x = np.arange(0, 5)

# absence counters for each day of the week at the start
mo = 0  # Monday absences
tu = 0  # Tuesday absences
we = 0  # Wednesday absences
th = 0  # Thursday absences
fr = 0  # Friday absences

# variables for the y axis and labels
positions = [0, 1, 2, 3, 4]
labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def plot():
    plt.clf()  # clears the previous plot

    # global variables
    global mo, tu, we, th, fr

    # gets the selected day and number of absences from the HTML form
    day = document.getElementById("day").value
    n = int(document.getElementById("num").value)

    # update the day's absence count based on whatever the user selected
    if day == 'monday':
        mo = n
    elif day == 'tuesday':
        tu = n
    elif day == 'wednesday':
        we = n
    elif day == 'thursday':
        th = n
    elif day == 'friday':
        fr = n

    # creates numpy array
    y = np.array([mo, tu, we, th, fr])

    # plots the data as a line graph with red color
    plt.plot(x, y, color='red')
    # adds circular markers on each point
    plt.plot(y, marker='o', color='red')

    # sets chart title and axis labels
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel('Day')
    plt.xticks(positions, labels) 
    plt.ylabel('Number of Absences')

    # displays the plot in the HTML element with id "chart"
    from pyscript import display
    display(plt.gcf(), target="chart", append=False)
    plt.close() 

    # this makes this chart visible when you click the button, since at the start it is hidden
    document.getElementById("chart").style.display = "block"
    print("clicked")

window.plot = plot