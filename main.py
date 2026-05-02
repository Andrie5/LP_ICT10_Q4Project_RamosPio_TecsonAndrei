import numpy as np
from pyscript import document
from pyodide.ffi import create_proxy

# used numpy array to store classmates
# each row represents [Name, Section, Favorite Subject]
classmates = np.array([
    ["Nathan", "Ruby", "Science"],
    ["Thea", "Ruby", "Math"],
    ["Maiah", "Ruby", "Music and SS"],
    ["Anxela", "Ruby", "Music and SS"],
    ["Gab", "Ruby", "Art"],
    ["Joo", "Ruby", "SS"],
    ["Caiomey", "Ruby", "Snacktime"],
    ["Athena", "Ruby", "TLE"],
    ["Niko", "Ruby", "PE"],
    ["Chelsea", "Ruby", "SS"],
    ["Jercey", "Ruby", "English"],
    ["Sittie", "Ruby", "Math"],
    ["Jarett", "Ruby", "Math"],
    ["Jakob E.", "Ruby", "TLE"],
    ["Cara", "Ruby", "SS"],
    ["Uriel", "Ruby", "TLE"],
    ["Aaron", "Ruby", "PE"],
    ["Gelo", "Ruby", "English"],
    ["Ezra", "Ruby", "SS"],
    ["Jakob L.", "Ruby", "SS and PE"],
    ["Trisha", "Ruby", "English & Science"],
    ["Kaila", "Ruby", "Music"],
    ["Xander", "Ruby", "Math"],
    ["Sam", "Ruby", "SS"],
    ["Pio", "Ruby", "PE"],
    ["Katelynn", "Ruby", "SS"],
    ["Hans", "Ruby", "PE and SS"],
])

def add(event):
    # this is a function to add a new classmate to the list
    global classmates

    # this gets input values from the HTML form
    name = document.querySelector("#name").value
    section = document.querySelector("#section").value
    subject = document.querySelector("#subject").value

    if name and section and subject:
        # create a new numpy array for the new student
        new_student = np.array([[name, section, subject]])
        # adds the new student to the existing classmates array 
        classmates = np.vstack([classmates, new_student]) if classmates.size > 0 else new_student

        # clears the input fields after after adding a new student
        document.querySelector("#name").value = ""
        document.querySelector("#section").value = ""
        document.querySelector("#subject").value = ""

        # success message
        result_div = document.querySelector("#result")
        result_div.innerHTML = f'<p style="color: green; margin-top: 10px;">Added {name} successfully!</p>'
    else:
        # error message if any field is empty
        result_div = document.querySelector("#result")
        result_div.innerHTML = '<p style="color: red; margin-top: 10px;">Please fill in all fields!</p>'

def list(event):
    # displays the list of all classmates
    result_div = document.querySelector("#result")

    if classmates.size > 0:
        # HTML list of classmates
        html = '<div style="text-align: left; margin-top: 20px;"><h4>Classmates List:</h4><ul style="list-style: none; padding: 0;">'
        for i in range(classmates.shape[0]):
            # formats each classmate's information
            html += f'<li style="padding: 8px; border-bottom: 1px solid #ccc;">{i+1}. Allo! My name is {classmates[i, 0]}, I am in {classmates[i, 1]} and my favorite subject is {classmates[i, 2]}</li>'
        html += '</ul></div>'
        result_div.innerHTML = html
    else:
        # displays message if no classmates are added yet
        result_div.innerHTML = '<p style="color: gray; margin-top: 10px;">No classmates added yet!</p>'

def setup():
    # event listeners for the buttons
    add_btn = document.querySelector("#addBtn")
    list_btn = document.querySelector("#listBtn")

    # this adds click event listeners to the buttons
    add_btn.addEventListener("click", create_proxy(add))
    list_btn.addEventListener("click", create_proxy(list))

setup()




