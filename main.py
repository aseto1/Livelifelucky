"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

import random
import time
import csv

name = ""
current_step = 0
money = 0
children = 0
total_steps = 0
steps_left = 0
path = 0
events_occured = 1
house = []
house_cost = []
salary = 0
house_price = 0
current_path = "regular"
bonuscards = 0
end = 0
x = -186
y = 191
direction = 1
square_size = 25
drawn_squares = 0

b = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("white")
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-175, 177)
t.pendown()
direction = -1
money = 0
drawn_squares = 0
square_size = 25
drawn_events = 0
drawn_steps_left = 0
on = False

b = turtle.Turtle()
b.penup()
b.setposition(-190, 200)
b.pendown()
m = turtle.Turtle()
m.hideturtle()
m.penup()
m.setposition(200,-200)
m.pendown()
m.write(f"Total Money: {money}")
m.penup()
m.setposition(200,-220)
m.pendown()
m.write(f"Total Children: {children}")
m.penup()
m.setposition(200,-240)
m.pendown()
m.write(f"House: {house}")

t.hideturtle()
m.hideturtle()

number = 3
direction = -1

colors = ['red','orange','yellow','green','light green','navy','cyan','purple','pink','maroon']

#108 SQUARES


leaderboard = [
  ['Player 1',0,0],
  ['Player 2',0,0],
  ['Player 3',0,0],
  ['Player 4',0,0],
  ['Player 5',0,0]
]

empty_list = []

try:
  with open('scores.csv',"r") as file:
    reader = csv.reader(file)
    for row in reader:
      empty_list.append(row)
  
except FileNotFoundError:
  with open("scores.csv",mode="w",newline='') as file:
    writer = csv.writer(file,csv.QUOTE_NONE)
    writer.writerows(leaderboard)

#DRAWING
def drawRect():
    global square_size, drawn_squares, drawn_steps_left,drawn_events, on

    t.speed(0)

    if drawn_squares < 111:
        if drawn_steps_left == 0: #LIFE EVENT
    
            t.fillcolor('misty rose')
            drawn_events +=1
            
            if drawn_events == 0:
                drawn_steps_left = 13
            elif drawn_events == 1:
                drawn_steps_left = 10
            elif drawn_events == 2:
                drawn_steps_left = 11
            elif drawn_events == 3:
                drawn_steps_left = 13
            elif drawn_events == 4:
                drawn_steps_left = 10
            elif drawn_events == 5:
                drawn_steps_left = 10
            elif drawn_events == 6:
                drawn_steps_left = 16
            elif drawn_events == 7:
                drawn_steps_left = 10
            else:
                drawn_steps_left = 15
        
        elif drawn_squares % 5 == 0:  #PAYCHECK
            t.fillcolor('light yellow')
        elif drawn_squares % 8 == 0:  #SPINTOWIN
            t.fillcolor('light cyan')
        elif drawn_squares % 12 == 0: #HOUSING
            t.fillcolor('lavender')
        else:
            t.fillcolor('white')

    t.begin_fill()
    t.forward(square_size)
    t.right(90)
    t.forward(square_size)
    t.right(90)
    t.forward(square_size)
    t.right(90)
    t.forward(square_size)

    if on is True:
        t.right(90)
    
    t.end_fill()

    drawn_squares += 1
    drawn_steps_left -= 1


def drawRectLeft():
    global square_size, drawn_squares, drawn_steps_left, drawn_events

    t.speed(0)

    if drawn_squares < 111:
        if drawn_steps_left == 0: #LIFE EVENT
    
            t.fillcolor('misty rose')
            drawn_events +=1
            
            if drawn_events == 0:
                drawn_steps_left = 13
            elif drawn_events == 1:
                drawn_steps_left = 10
            elif drawn_events == 2:
                drawn_steps_left = 11
            elif drawn_events == 3:
                drawn_steps_left = 13
            elif drawn_events == 4:
                drawn_steps_left = 10
            elif drawn_events == 5:
                drawn_steps_left = 10
            elif drawn_events == 6:
                drawn_steps_left = 16
            elif drawn_events == 7:
                drawn_steps_left = 10
            else:
                drawn_steps_left = 15
        
        elif drawn_squares % 5 == 0:  #PAYCHECK
            t.fillcolor('light yellow')
        elif drawn_squares % 8 == 0:  #SPINTOWIN
            t.fillcolor('light cyan')
        elif drawn_squares % 12 == 0: #HOUSING
            t.fillcolor('lavender')
        else:
            t.fillcolor('white')

    t.begin_fill()
    t.forward(square_size)
    t.left(90)
    t.forward(square_size)
    t.left(90)
    t.forward(square_size)
    t.left(90)
    t.forward(square_size)
    t.end_fill()

    drawn_squares += 1
    drawn_steps_left -= 1


def moveDown():
    t.right(90)

    #down vertical
    for num in range(14):
        drawRect()
        t.right(90)
        t.forward(square_size)
    t.right(180)
    t.forward(square_size)
    t.right(90)


def moveRight():
    #right horizontal
    for num in range(2):
        drawRect()
        t.right(90)
        t.forward(square_size)


def moveRightLess():
    drawRect()
    t.right(90)
    t.forward(square_size)


def moveUp():
    #up vertical
    t.left(90)
    for num in range(13):
        drawRectLeft()
        t.left(90)
        t.forward(square_size)
    t.right(90)


def drawMap():
    global square_size, drawn_squares, on

    for num in range(3):

        moveDown()
        moveRight()
        moveUp()
        moveRightLess()
        t.forward(square_size)

    moveDown()
    moveRight()

    #up vertical
    t.left(90)
    for num in range(5):
        drawRectLeft()
        t.left(90)
        t.forward(square_size)
    t.right(90)

    #draw key
    t.penup()
    t.setposition(-380,180)
    t.pendown()
    on = True

    t.fillcolor('light yellow')
    drawRect()
    t.penup()
    t.setposition(-355,160)
    t.pendown()
    t.write(" = Paycheck Day",font=('Arial',10))

    t.penup()
    t.setposition(-380,150)
    t.pendown()

    t.fillcolor('light cyan')
    drawRect()
    t.penup()
    t.setposition(-355,130)
    t.pendown()
    t.write(" = Spin to Win",font=('Arial',10))

    t.penup()
    t.setposition(-380,120)
    t.pendown()

    t.fillcolor('lavender')
    drawRect()
    t.penup()
    t.setposition(-355,100)
    t.pendown()
    t.write(" = Moving Day",font=('Arial',10))

drawMap()


def car():
    car_color = input(
        "\nWhat color do you want your car to be? r for red, y for yellow, g for green, b for blue ")
    #try:
    if car_color.lower() == "r":
      car_color = "red"
    elif car_color.lower() == "y":
      car_color = "yellow"
    elif car_color.lower() == "g":
      car_color = "green"
    else:
      car_color = "blue"
    #except GraphicsError:
      #t.color("blue")

    b.color(car_color)
  

#SCORING
def retirement():
  global name, current_step, end, money, children, total_steps, steps_left, path, events_occured, house, house_cost, salary, house_price, current_path, direction, x, y, bonuscards, end, title, number
  print("\nYou've reached the end of the game! Now let's count up your score!")
  time.sleep(3)
  print("\nFirst, we need to sell your houses.")
  while len(house) > 0:
    num = 0
    print(f"\nSelling {house[num]}...")
    sale = random.randint(1,2)
    if sale == "1":
      house_cost[num] += 200
    if sale == "2":
      house_cost[num] += 500
    print(f"\nSold for {house_cost[num]}!")
    del house_cost[num]
    del house[num]
  
  print("\nLet's count up your bonus cards!")
  add = bonuscards*100
  money += add
  print(f"\nYou have {bonuscards} bonus cards, so get {add} more dollars!")
  
  print("\nYou get money for each of your children!")
  add2 = children*50
  money += add2
  print(f"\nYou have {children} children, so get {add2} more dollars!")
  time.sleep(2)
  print("\nAdding up all your money...")
  time.sleep(2)
  print(f"\nYou got ${money}!")
  time.sleep(2)
  print("\nThat means you are ranked as a ...")
  time.sleep(3)
  if money <= 100000:
      print("\nLevel 1 player!")
      rank = 1
  elif money <= 200000:
      print("\nLevel 2 player!")
      rank = 2
  elif money <= 250000:
      print("\nLevel 3 player!")
      rank = 3
  elif money <= 300000:
      print("\nLevel 4 player!")
      rank = 4
  elif money <= 350000:
      print("\nLevel 5 player!")
      rank = 5
  end = 1
  current_path = "regular"
  events_occured += 1
  steps_left = 0
  perfect_score = [name,money, rank]

  try:
    if rank > float(empty_list[4][1]) or rank == float(empty_list[4][1]) and money > float(empty_list[4][2]):
      if rank > float(empty_list[3][1]) or rank == float(empty_list[3][1]) and money > float(empty_list[3][2]):
        if rank > float(empty_list[2][1]) or rank == float(empty_list[2][1]) and money > float(empty_list[2][2]):
          if rank > float(empty_list[1][1]) or rank == float(empty_list[1][1]) and money > float(empty_list[1][2]):
            if rank > float(empty_list[0][1]) or rank == float(empty_list[0][1]) and money > float(empty_list[0][2]):
              empty_list.insert(0,perfect_score)
              print("\nYou got first on the leaderboard!")
            else:
              empty_list.insert(1,perfect_score)
              print("\nYou got second on the leaderboard!")
          else:
            empty_list.insert(2,perfect_score)
            print("\nYou got third on the leaderboard!")
        else:
          empty_list.insert(3,perfect_score)
          print("\nYou got fourth on the leaderboard!")
      else:
        empty_list.insert(4,perfect_score)
        print("\nYou got fifth on the leaderboard!")
    else:
      print("\nSorry, you didn't make it on the empty_list. Nice try!")
      
  except IndexError:
    with open('scores.csv',"r") as file:
      reader = csv.reader(file)
      for row in reader:
        empty_list.append(row)
    if rank > float(empty_list[4][1]) or rank == float(empty_list[4][1]) and money > float(empty_list[4][2]):
      if rank > float(empty_list[3][1]) or rank == float(empty_list[3][1]) and money > float(empty_list[3][2]):
        if rank > float(empty_list[2][1]) or rank == float(empty_list[2][1]) and money > float(empty_list[2][2]):
          if rank > float(empty_list[1][1]) or rank == float(empty_list[1][1]) and money < float(empty_list[1][2]):
            if rank > float(empty_list[0][1]) or rank == float(empty_list[0][1]) and money < float(empty_list[0][2]):
              empty_list.insert(0,perfect_score)
              print("\nYou got first on the leaderboard!")
            else:
              empty_list.insert(1,perfect_score)
              print("\nYou got second on the leaderboard!")
          else:
            empty_list.insert(2,perfect_score)
            print("\nYou got third on the leaderboard!")
        else:
          empty_list.insert(3,perfect_score)
          print("\nYou got fourth on the leaderboard!")
      else:
        empty_list.insert(4,perfect_score)
        print("\nYou got fifth on the leaderboard!")
    else:
      print("\nSorry, you didn't make it on the empty_list. Nice try!")

  try:
    if len(empty_list) >= 5:
      del empty_list[5]
  except IndexError:
    pass

  with open("scores.csv",mode="w",newline='') as file:
    writer = csv.writer(file,csv.QUOTE_NONE)
    writer.writerows(empty_list)
    file.close()



def lifeevents():
  global name, current_step, end, money, children, total_steps, steps_left, path, events_occured, house, house_cost, salary, house_price, current_path,  direction, x, y, bonuscards, title, number
  if end == 0:
    print("\nYou reached a major turning point in your life!")
    time.sleep(1)
    #print(events_occured)
  if events_occured == 1:
      question = input("\nDo you choose to go to [1] go straight to a career or [2] go to college? ") 
      if question == "1":
        print("\nYou are not going to college.")
        steps_left = 13
        job_list = ["cashier", "waiter", "basketball player", "YouTuber", "fashion designer", "janitor", "influencer"]
    
        salary_list = [30000, 45000, 50000, 40000, 50000, 35000, 55000, 30000]
        events_occured += 2
        num1 = random.randint(0,7)
        num2 = random.randint(0,7)

        question = input(f"\nWould you want to be a [1] {job_list[num1]} with a salary of {salary_list[num1]} or [2] {job_list[num2]} with a salary of {salary_list[num2]}? ")

        if question == "1":
          title = job_list[num1]
          salary = salary_list[num1]
        else:
          title = job_list[num2]
          salary = salary_list[num2]
        print(f"\nYou are now a {title} with a salary of: ${salary}.")
        for i in range(10):
          b.penup()  
        if number < 2: #MOVING RIGHT
            x += 25
            number += 1
        elif number == 2: #SWITCHING DIRECTION
            direction = direction * -1
            number = 4
        elif number < 17: #MOVING VERTICALLY
            y += 25 * direction
            number += 1
        else:
            number = 0
        #elif y >= 200 and number < 3:
          #x+= 25
          #number += 1
        b.setposition(x, y)
        b.pendown()
        b.shape("circle")
        b.shapesize(1)
        time.sleep(1)
        b.clear()
  
      else:
        print("\nGoing to college!")
        steps_left = 23
        events_occured += 1
        spin()
  elif events_occured == 2:
    print("\nYay, you have just graduated college. Let's spin to see what job you will get!")
  
    job = random.randint(0, 9)
    job2 = random.randint(0, 9)
  
    job_list = ["teacher", "doctor", "software engineer", "author", "aerospace engineer", "lawyer", "architect", "accountant", "governor", "journalist"]
      
    salary_list = [60000, 130000, 100000, 60000, 110000, 120000, 90000, 70000, 70000, 80000]
  
    while job2 == job:
          job2 = random.randint(0, 9)
  
    title = job_list[job]
    salary = salary_list[job]
  
    title2 = job_list[job2]
    salary2 = salary_list[job2]
  
    question = input(f"\nWould you like to be a(n) [1] {title} or [2] {title2}? {title} has a salary of {salary} and {title2} has a salary of {salary2}.")
    if question == "2":
        title = title2
        salary = salary2
    print(f"\nYou are now a {title} with a salary of: ${salary}.")
    events_occured += 1
    steps_left = 10
    spin()
  elif events_occured == 3:
      print("\nYou are getting married! Spin to see what wedding gifts you get!")
      gifts = random.randint(1, 2)
      time.sleep(2)
      if gifts == 1:
          print("\nYou got $50!")
          money += 50
      if gifts == 2:
          print("\nYou got $100!")
          money += 100
      events_occured += 1
      steps_left = 11
      spin()
  elif events_occured == 4:
    question = input("\nDo you want to go [1] back to college to get a different job or [2] continue living life? ")
    if question == "1":
      steps_left = 13
      print("\nOkay, going back to college!")
      events_occured += 1
      spin()
    if question == "2":
      steps_left = 23
      print("\nOkay, continuing life as it is!")
      for i in range(10):
          b.penup()  
          if number < 2: #MOVING RIGHT
              x += 25
              number += 1
          elif number == 2: #SWITCHING DIRECTION
              direction = direction * -1
              number = 4
          elif number < 17: #MOVING VERTICALLY
              y += 25 * direction
              number += 1
          else:
              number = 0
          #elif y >= 200 and number < 3:
          #x+= 25
          #number += 1
          b.setposition(x, y)
          b.pendown()
          b.shape("circle")
          b.shapesize(1)
          time.sleep(1)
          b.clear()
    
      events_occured += 2
      spin()
  elif events_occured == 5:
    print("\nYay, you have just graduated college. Let's spin to see what job you will get!")
  
    job = random.randint(0, 9)
    job2 = random.randint(0, 9)
  
    job_list = ["teacher", "doctor", "software engineer", "author", "aerospace engineer", "lawyer", "architect", "accountant", "governor", "journalist"]
      
    salary_list = [60000, 130000, 100000, 60000, 110000, 120000, 90000, 70000, 70000, 80000]
  
    while job2 == job:
          job2 = random.randint(0,9)
  
    title = job_list[job]
    salary = salary_list[job]
  
    title2 = job_list[job2]
    salary2 = salary_list[job2]
  
    question = input(f"\nWould you like to be a [1] {title} or [2] {title2}? {title} has a salary of {salary} and {title2} has a salary of {salary2}? ")
    if question == "2":
        title = title2
        salary = salary2
    print(f"\nYou are now a {title} with a salary of: ${salary}.")
    events_occured += 1
    steps_left = 10
    spin()
  elif events_occured == 6:
    question = input("\nDo you choose to [1] have kids or [2] continue life? ")
    if question == '1':
      print("\nAlright, you're going to start a family!")
      steps_left = 10
      events_occured += 1
      spin()
    else:
      print("\nAlright, let's keep on living life!")
      steps_left = 26
      for i in range(10):
          b.penup()  
          if number < 2: #MOVING RIGHT
              x += 25
              number += 1
          elif number == 2: #SWITCHING DIRECTION
              direction = direction * -1
              number = 4
          elif number < 17: #MOVING VERTICALLY
              y += 25 * direction
              number += 1
          else:
              number = 0
          #elif y >= 200 and number < 3:
          #x+= 25
          #number += 1
          b.setposition(x, y)
          b.pendown()
          b.shape("circle")
          b.shapesize(1)
          time.sleep(1)
          b.clear()
      events_occured += 2
      spin()
  elif events_occured == 7:
    print("\nLet's see how many kids you had!")
    children = random.randint(1,5)
    time.sleep(1)
    print(f"\nYou had {children} kids!")
    steps_left = 16
    events_occured +=1
  elif events_occured == 8:
    question = input("\nDo you choose to take the [1] risky path or [2] the safe path? ")
    if question == '1':
      print("\nRisky path it is!")
      current_path = "risky"
      steps_left = 10
      events_occured +=1
      spin()
    if question == "2":
      print("\nSafe path it is!")
      steps_left = 25
      events_occured +=1
      spin()
  elif events_occured == 9:
    print("\nYou've reached retirement age!")
    time.sleep(4)
    retirement()
  
      

def intro():
  global name, current_step, end, money, children, total_steps, steps_left, path, events_occured, house, house_cost, salary, house_price, current_path,  direction, x, y, bonuscards, title, number
  print("Welcome to the Game of Life, the game with the answers to all of life's questions!")

  
  print("""---------------------HIGH SCORE TABLE-----------------""")
  try:
    with open('scores.csv',"r") as file:
      reader = csv.reader(file)
      for row in reader:
        print(f"           Name: {row[0]}, Rank: {row[1]}, Money: {row[2]}")
      file.close()

  except FileNotFoundError:
    print("""\n                     No scores yet\n""")
    
  name = input("\nWhat is your name? ")

  print(f"\nNice to meet you {name}!")

  question1 = input("\nWould you like me to give you an overview of the game? y for yes, n for no :: ")

  if question1.lower() == "y":
      overview()
  car()
  b.penup()
  b.setposition(-190, 200)
  b.pendown()
    
  print("\nAlright let's get to the game!")
  lifeevents()


def overview():
    print("\nIn the Game of Life, you go through life and have multiple major life choices that may affect your success and happiness such as career choices, family choices, and housing choices. ")
    time.sleep(4)
    print("\nThe type of job you get will determine your salary and the more kids you have the more money you get. In the end, the amount of money you have will determine your ranking."
    )
    time.sleep(4)
    print("\nAlright, time to play! Good luck!")


def spin():
  global name, current_step, end, money, children, total_steps, steps_left, path, events_occured, house, house_cost, salary, house_price, current_path,  direction, x, y,bonuscards, size, number
  time.sleep(1)
  input("Click enter to continue.")
  print("\nSpinning the wheel!")
  time.sleep(3)
  print("\n2 4 3 2 1 0 2 9 3 5 8 6 7 3 6 7....")
  
  if end == 0:
    steps = random.randint(1, 10)
    #return steps
    steps_left -= steps
    total_steps += steps
    
    w = turtle.Turtle()
    w.hideturtle()
    w.speed(10)
    w.color("red")
    num = 1
    w.left(18)
    
    w.speed(0)
    num = 0
    w.color("red")
    w.left(18)
    
    for i in range(10):
      w.setposition(0,0)
      w.begin_fill()
      w.pendown()
      w.forward(110)
      w.right(108)
      w.forward(70)
      w.right(108)
      w.forward(110)
      w.end_fill()
      
      w.penup()
      w.right(180)
      if num < 9:
        num += 1
        color = colors[num]
        w.color(color)
      
    
    #while True:
      #for spoke in spokes:
        #spoke.left(26)
    r = turtle.Turtle()
    r.hideturtle()
   
    steps = random.randint(1,10)
    print(steps)
    num = steps*7
    for i in range(num):
      r.forward(50)
      r.clear()
      r.setposition(0,0)
      r.right(5)
  
    time.sleep(2)
    r.color('white')
    r.write(steps, font=('Arial',20))

    time.sleep(4)
    r.clear()
    w.clear()
    
    print(f"{steps}!")
    print(f"\nYou move {steps} steps forward.")
      
    for i in range(steps):
        b.penup()  
        if number < 2: #MOVING RIGHT
            x += 25
            number += 1
        elif number == 2: #SWITCHING DIRECTION
            direction = direction * -1
            number = 4
        elif number < 17: #MOVING VERTICALLY
            y += 25 * direction
            number += 1
        else:
            number = 0
        #elif y >= 200 and number < 3:
          #x+= 25
          #number += 1
        b.setposition(x, y)
        b.pendown()
        b.shape("circle")
        b.shapesize(1)
        time.sleep(1)
        b.clear()
      
    time.sleep(2)

  if current_path == "risky":

      rand_amount = random.randint(1,10000)
      outcome = random.randint(1,2)

      if outcome == 1:
          money += rand_amount
          print(f"\nYou have won ${rand_amount}!")
      if outcome == 2:
          money -= rand_amount
          print(f"\nYou have lost ${rand_amount}!")
  elif steps_left == 0 and current_path == "risky":
    steps_left = 15
    current_path = "regular"
  elif steps_left <= 0:
      lifeevents()
  elif end == 0:
      play()
  

def play():
  global name, current_step, end, money, children, total_steps, steps_left, path, events_occured, house, house_cost, salary, house_price, current_path,  direction, x, y, bonuscards, title, number
  if total_steps % 5 == 0 and salary > 0:     #PAYCHECK
  
      money += salary
      print(f"\nYou landed on a paycheck! Your current balance is: ${money}.")
      spin()
      
  elif total_steps % 8 == 0:  #SPIN TO WIN
      
      numm = input("\nYou get to SpinToWin! Enter a value 1-10: ")
      computer = random.randint(1,10)
      if numm == computer:
          print("\nThat is correct! You have won $200")
      else:
          print(f"\nUnfortunately, that is incorrect. The correct answer was {computer}. You don't win anything.")
      spin()
          
  elif total_steps % 12 == 0:  #HOUSING

    num = random.randint(0,6)

    house_list = ["small cottage", "windmill", "penthouse", "mansion", "beach house","tent", "rv"]
    price_list = [10000,5000,100000,500000,75000,500,1000]

    purchase = input(f"\nYou can buy a {house_list[num]} for ${price_list[num]}. Would you like to purchase it (y or n): ")

    if purchase == "y":
      if price_list[num] > money:
          print(
              "You cannot afford this house. You will continue homeless for now."
          )
      else:
          print(f"\nCongratulations on your new {house}!")
          house.append(house_list[num])
          house_price = price_list[num]
          house_cost.append(house_price)
          money -= house_price
              
    else:
      print("\nOh well, moving on then!")
    spin()

  else:  #BONUS CARD
      bonuscards += 1

      money = 0 #change later
      c = turtle.Turtle()
      c.hideturtle()
      c.color("black")
      c.fillcolor('white smoke')
      c.penup()
      c.setposition(-175,200)
      c.pendown()
        
      c.begin_fill()
      c.forward(300)
      c.right(90)
      c.forward(500)
      c.right(90)
      c.forward(300)
      c.right(90)
      c.forward(500)
      c.right(90)
      c.end_fill()
    
      card_list = ["You got the award for best gelled-hair", "You solved the world's problem of lice", "You made someone laugh", "You saved the species of axolotls", "You got a good grade", "You mastered the skill of kungfu", "You sold your collection of old antique toys!", "You found $40 on the ground!", "You got a fortune in bingo!", "You slept for 13 hours straight!","Oh no! Your house was broken into. You have been robbed of $1000 worth of items.","You accidentally spilled some coffee on your new clothes. You have lost $50.",f"It's tax time! You have to pay ${(salary*.15)}.","You end up falling for a Nigerian Price Scam and lose $20000.","You were caught speeding at 200 mph! You were forced to pay a fine of $700.","You chose to go on a GIANT spending spree and ended up using $5000 on clothes and $75000 on a new car.","Oh no! You have been laid off. You will now get a new job."]
      amount_list = [100,400,200,300,150,2000,40,375,225,80,-1000,-50,-(salary*.15),-20000,-700,-80000,0]
    
      rand = random.randint(0,16)
      print(card_list[rand])
      time.sleep(1)

      c.penup()
      c.setposition(-30,80)
      c.pendown()
      c.color('blue')
      c.begin_fill()
      c.circle(9)
      c.end_fill()
    
      c.penup()
      c.goto(10,80)
      c.pendown()
      c.penup()
      c.forward(25)
      c.begin_fill()
      c.circle(9)
      c.end_fill()
    
      if rand <=9:
        print(f"You win {amount_list[rand]} dollars!")
        money += amount_list[rand]
        c.penup()
        c.goto(40,50)
        c.pendown()
        c.right(92)
        c.down()
        c.circle(-40, 180)
        c.up()
      if rand >= 10 and rand != 16:
        print(f"You lose {amount_list[rand]} dollars!")
        c.penup()
        c.goto(40,20)
        c.pendown()
        c.right(92)
        c.down()
        c.circle(-40, -180)
        c.up()
        money -= amount_list[rand]
      time.sleep(1)

      m.penup()
      m.setposition(200,-200)
      m.pendown()
      m.write(f"Total Money: {money}")
      m.penup()
      m.setposition(200,-220)
      m.pendown()
      m.write(f"Total Children: {children}")
      m.penup()
      m.setposition(200,-240)
      m.pendown()
      m.write(f"House: {house}")
    
      c.color("black")
      c.penup()
      c.setposition(-150,160)
      c.pendown()
      c.write(card_list[rand],font=('Arial',15))
      c.penup()
      c.setposition(-90, -100) 
      c.pendown()
      c.write(f"Win: ${amount_list[rand]}",font=('Arial',15))
    
      time.sleep(4)
      c.clear()
              
      if rand == 16: #LOST JOB

          if salary >= 16000:
              job_list = ["teacher", "doctor", "software engineer", "author", "aerospace engineer", "lawyer", "architect", "accountant", "governor", "journalist"]
              salary_list = [60000, 130000, 100000, 60000, 110000, 120000, 90000, 70000, 70000, 80000]

              number = random.randint(0,9)
              job = job_list[number]
              salary = salary_list[number]
              
          else:
              job_list = ["cashier", "waiter", "basketball player", "YouTuber", "fashion designer", "janitor", "influencer"]
              salary_list = [30000, 45000, 50000, 40000, 50000, 35000, 55000]

              number = random.randint(1,6)
              job = job_list[number]
              salary = salary_list[number]
                  

          print(f"\nYou are now a {job} with a salary of ${salary}.")

  m.penup()
  m.setposition(200,-200)
  m.pendown()
  m.write(f"Total Money: {money}")
  m.penup()
  m.setposition(200,-220)
  m.pendown()
  m.write(f"Total Children: {children}")
  m.penup()
  m.setposition(200,-240)
  m.pendown()
  m.write(f"House: {house}")

  spin()


#START PLAYING HERE-------------------

intro()


#END PLAYING HERE----------
