import turtle

#this function makes the tic tac toe board
#also it puts numbers in each other the boxes so the players can tell what box is what number
def setup_tictactoe(turtle):
        turtle.pensize(3)  #so the box outline is thicker
        turtle.backward(120)  #this centres the board, so its not off to the right
        for i in range(3): #this loop makes 3 lines of 3 squares
                for m in range(3):   #this loop makes 3 squares in a row on one line
                        for n in range(0,4):  #this for loop make a square
                                turtle.forward(80)
                                turtle.right(90)
                        turtle.forward(80)
                if i!=2: #on the last time through it sets the turtle up for the next task
                        turtle.backward(80*3)
                        turtle.left(90)
                        turtle.forward(80)
                        turtle.right(90)
        #this section makes a number appear in each corner of the 9 boxes on the screen.
        turtle.pensize(1)
        turtle.penup()
        turtle.backward(78*3)
        turtle.right(90)
        turtle.forward(20)
        turtle.write("1", font=("Arial", 16, "normal"))
        turtle.left(90)
        turtle.forward(80)
        turtle.write("2", font=("Arial", 16, "normal"))
        turtle.forward(80)
        turtle.write("3", font=("Arial", 16, "normal"))
        turtle.right(90)
        turtle.forward(80)
        turtle.write("6", font=("Arial", 16, "normal"))
        turtle.right(90)
        turtle.forward(80)
        turtle.write("5", font=("Arial", 16, "normal"))
        turtle.forward(80)
        turtle.write("4", font=("Arial", 16, "normal"))
        turtle.left(90)
        turtle.forward(80)
        turtle.write("7", font=("Arial", 16, "normal"))
        turtle.left(90)
        turtle.forward(80)
        turtle.write("8", font=("Arial", 16, "normal"))
        turtle.forward(80)
        turtle.write("9", font=("Arial", 16, "normal"))
        #writes tic-tac-toe on the top of the game
        turtle.home()
        turtle.backward(95)
        turtle.left(90)
        turtle.forward(180)
        turtle.write("Tic-Tac-Toe", font=("Arial", 36, "normal"))
        
#this function draws an "x" then returns it back to home
def letter_x(turtle):
        turtle.left(45)
        turtle.pendown()
        turtle.forward(30)
        turtle.backward(60)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.backward(60)
        turtle.forward(30)
        turtle.penup()
        turtle.home()

#this function draws an "O", then returns it back to home
def circle_O(turtle):
        turtle.pendown()
        turtle.circle(30)
        turtle.penup()
        turtle.home()

#variables and lists
board = [1,2,3,4,5,6,7,8,9]
counter=0
counter2=0

#setting up screen
screen=turtle.Screen()  #putting the screen into a variable for the end of the program
turtle.bgcolor("yellow") #changing the background color

#setting up turtle and board
chloe=turtle.Turtle()
chloe.ht()  #makes turtle invisible
chloe.speed(0)  #so it goes faster
chloe.color("blue")  #changes the color
setup_tictactoe(chloe)  #calling the fuction to setup the board

#adjusting my turtle, to do other tasks
chloe.pensize(3)
chloe.color("red")  #changing colors
chloe.penup()
chloe.home()  #putting turtle back to the start

#telling the user how the game is played and giving them an introduction
print("Welcome to TicTacToe, Player 1 is O\'s, and Player 2 is X\'s")
print("A game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds")
print("in placing three respective marks in a horizontal, vertical, or diagonal row wins the game.")
print("To play you must enter a number which corresponds to the boxes that you want your X or O in.")


while counter!=1: #the counter will be 1, only if someone wins or if its a draw.
        counter2=counter2+1 #this counter will be used to control whose turn it is, based on if its even or odd. if its even its player two, odd is player 1
        counter3=0 #this counter will be used to see if the number the user gave is usable, resets every loop
        
        while counter3==0:  #it will keep looping until the number is good and usable
                if counter2%2 == 0:  #if its even (no remainder when divided by two.). It keeps track of who's turn it is.
                        if counter2==2: #if its their first turn, it gives the user more instruction than the other turns
                                user_number=int(input(("Player 2 turn, please enter the box number (then press enter) : "))) #turning it into a number
                        else:
                                user_number=int(input(("Player 2 turn, please enter the box number : ")))
                        if board[user_number-1]=="x" or board[user_number-1]=="o":  #checking if the number they gave already is an x or an o. 
                                print("That box has something in it, Player 2 Try Again.")
                        else:  
                                counter3=counter3+1  #adding one to counter so it knows that the number that is given is usable.                               
                else:  #if counter number is odd then its player 1's turn
                        if counter2==1:  #if its their first turn, it gives the user more instruction than the other turns
                                user_number=int(input(("Player 1 turn, please enter the box number (then press enter) : ")))  #turning it into a number
                        else:
                                user_number=int(input(("Player 1 turn, please enter the box number : ")))
                        if board[user_number-1]=="x" or board[user_number-1]=="o" : #checking if the number they gave already is an x or an o. 
                                print("That box has something in it, Player 1 Try Again.")
                        else:
                                counter3=counter3+1#adding one to counter so it knows that the number that is given is usable.
                                
        number= board[user_number-1]  #stores the number before it is turned into an X or O
        if counter2%2 == 0:  #if counter is even (no remainder when divided by two.)... Its player two's turn.
                board[user_number-1]="x" #changes the number into an x
        else:   #if its odd so player 1's turn
                board[user_number-1]="o"  #changes the number into an O
        if counter2%2 == 0: #if counter is even (no remainder when divided by two.)... If its player two's turn.
                if number==1:  #if number is 1 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.left(90)
                                chloe.forward(120)
                                chloe.right(90)
                                chloe.backward(80)
                                letter_x(chloe)
                                #goes through all the winning possible combinations if they enter 1, and if its a match you add to your counter to end the game 
                                if board[1]=="x":
                                        if board[2]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[3]=="x":
                                        if board[6]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[4]=="x":
                                        if board[8]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                elif number==2: #if number is 2 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.left(90)
                                chloe.forward(120)
                                letter_x(chloe)
                                #goes through all the winning possible combinations if they enter 2, and if its a match you add to your counter to end the game
                                if board[0]=="x":
                                        if board[2]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[4]=="x":
                                        if board[7]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                        
                elif number==3: #if number is 3 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.left(90)
                                chloe.forward(120)
                                chloe.right(90)
                                chloe.forward(80)
                                letter_x(chloe)
                                #goes through all the possible winning combinations if they enter 3, and if its a match you add to your counter to end the game
                                if board[1]=="x":
                                        if board[0]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[5]=="x":
                                        if board[8]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[4]=="x":
                                        if board[6]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                elif number==4: #if number is 4 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.backward(80)
                                chloe.left(90)
                                chloe.forward(40)
                                chloe.right(90)
                                letter_x(chloe)
                                #goes through all the possible winning combinations if they enter 4, and if its a match you add to your counter to end the game
                                if board[0]=="x":
                                        if board[6]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[4]=="x":
                                        if board[5]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                elif number==5: #if number is 5 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.left(90)
                                chloe.forward(40)
                                chloe.right(90)
                                letter_x(chloe)
                                #goes through all the possible winning combinations if they enter 5, and if its a match you add to your counter to end the game
                                if board[1]=="x":
                                        if board[7]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[3]=="x":
                                        if board[5]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[0]=="x":
                                        if board[8]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[2]=="x":
                                        if board[6]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                             
                elif number==6: #if number is 6 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.forward(80)
                                chloe.left(90)
                                chloe.forward(40)
                                chloe.right(90)
                                letter_x(chloe)
                                #goes through all the possible winning combinations if they enter 6, and if its a match you add to your counter to end the game
                                if board[2]=="x":
                                        if board[8]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[4]=="x":
                                        if board[3]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                                elif board[4]=="x":
                                        if board[6]=="x":
                                                print("Congrats Player Two, You Win!")
                                                counter=counter+1
                elif number==7: #if number is 7 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.backward(80)
                                chloe.right(90)
                                chloe.forward(40)
                                chloe.left(90)
                                letter_x(chloe)
                                #goes through all the possible winning combinations if they enter 7, and if its a match you add to your counter to end the game
                                if board[7]=="x":
                                        if board[8]=="x":
                                                print("You Win")
                                                counter=counter+1
                                elif board[0]=="x":
                                        if board[3]=="x":
                                                print("You Win")
                                                counter=counter+1
                                elif board[4]=="x":
                                        if board[2]=="x":
                                                print("You Win")
                                                counter=counter+1
                elif number==8: #if number is 8 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.right(90)
                                chloe.forward(40)
                                chloe.left(90)
                                letter_x(chloe)
                                #goes through all the possible winning combinations if they enter 8, and if its a match you add to your counter to end the game
                                if board[4]=="x":
                                        if board[1]=="x":
                                                print("You Win")
                                                counter=counter+1
                                elif board[6]=="x":
                                        if board[8]=="x":
                                                print("You Win")
                                                counter=counter+1
                                elif board[4]=="x":
                                        if board[2]=="x":
                                                print("You Win")
                                                counter=counter+1
        
                elif number==9: #if number is 9 it goes through this loop
                                # sets up the turtle to draw the letter X
                                chloe.forward(80)
                                chloe.right(90)
                                chloe.forward(40)
                                chloe.left(90)
                                letter_x(chloe)
                                #goes through all the possible winning combinations if they enter 9,and if its a match you add to your counter to end the game
                                if board[5]=="x":
                                        if board[2]=="x":
                                                print("You Win")
                                                counter=counter+1
                                elif board[4]=="x":
                                       if board[0]=="x":
                                                print("You Win")
                                                counter=counter+1
                                elif board[7]=="x":
                                        if board[6]=="x":
                                                print("You Win")
                                                counter=counter+1

                                                
        else:   # if its player 1's turn
                        if number==1: #if number is 1 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.penup()
                                chloe.left(90)
                                chloe.forward(150)
                                chloe.left(90)
                                chloe.forward(80)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if they enter 1,and if its a match you add to your counter to end the game
                                if board[1]=="o":
                                        if board[2]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[3]=="o":
                                        if board[6]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                        if board[8]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                        elif number==2:#if number is 2 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.left(90)
                                chloe.forward(150)
                                chloe.left(90)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if they enter 2, and if its a match you add to your counter to end the game
                                if board[0]=="o":
                                        if board[2]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                        if board[7]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                        
                        elif number==3:#if number is 3 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.left(90)
                                chloe.forward(150)
                                chloe.right(90)
                                chloe.forward(80)
                                chloe.left(180)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if they enter 3,and if its a match you add to your counter to end the game
                                if board[1]=="o":
                                        if board[0]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[5]=="o":
                                        if board[8]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                        if board[6]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                        elif number==4:#if number is 4 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.backward(80)
                                chloe.left(90)
                                chloe.forward(70)
                                chloe.left(90)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if they enter 4,and if its a match you add to your counter to end the game
                                if board[0]=="o":
                                        if board[6]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                        if board[5]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                        elif number==5:#if number is 5 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.left(90)
                                chloe.forward(70)
                                chloe.left(90)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if they enter 5,and if its a match you add to your counter to end the game
                                if board[1]=="o":
                                        if board[7]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[3]=="o":
                                        if board[5]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[0]=="o":
                                        if board[8]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[2]=="o":
                                        if board[6]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                             
                        elif number==6:#if number is 6 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.forward(80)
                                chloe.left(90)
                                chloe.forward(70)
                                chloe.left(90)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if they enter 6,and if its a match you add to your counter to end the game
                                if board[2]=="o":
                                        if board[8]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                        if board[3]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                        if board[6]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                        elif number==7:#if number is 7 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.left(90)
                                chloe.backward(70)
                                chloe.right(90)
                                chloe.backward(80)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if they enter 7,and if its a match you add to your counter to end the game
                                if board[7]=="o":
                                        if board[8]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[0]=="o":
                                        if board[3]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                        if board[2]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                        elif number==8:#if number is 8 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.left(90)
                                chloe.backward(70)
                                chloe.right(90)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if theyu enter 8,and if its a match you add to your counter to end the game
                                if board[4]=="o":
                                        if board[1]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[6]=="o":
                                        if board[8]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                        if board[2]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
        
                        elif number==9:#if number is 9 it goes through this loop
                                # sets up the turtle to draw the letter O
                                chloe.left(90)
                                chloe.backward(70)
                                chloe.right(90)
                                chloe.forward(80)
                                circle_O(chloe)
                                #goes through all the possible winning combinations if they enter 9,and if its a match you add to your counter to end the game
                                if board[5]=="o":
                                        if board[2]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[4]=="o":
                                       if board[0]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                elif board[7]=="o":
                                        if board[6]=="o":
                                                print("Congrats Player One, You Win!")
                                                counter=counter+1
                                                
        # this loop checks if its a draw by seeing if all the boxes are filled with C's or O's. If they are it adds to the counter to finish the game
        if counter!=1:
                if board[0]=="x" or board[0]=="o":
                        if board[1]=="x" or board[1]=="o":
                                if board[2]=="x" or board[2]=="o":
                                        if board[3]=="x" or board[3]=="o":
                                                if board[4]=="x" or board[4]=="o":
                                                        if board[5]=="x" or board[5]=="o":
                                                                if board[6]=="x" or board[6]=="o":
                                                                        if board[7]=="x" or board[7]=="o":
                                                                                if board[8]=="x" or board[8]=="o":
                                                                                        print("Its a Draw")
                                                                                        counter= counter+1

                

print("Thanks for playing! Click anywhere on turtle screen to exit, then press the enter key!")
screen.exitonclick()