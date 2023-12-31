# RollTheDiceGame
In the roll the dice game, we throw a dice having six faces. Each face of the dice has a unique value from 1 to 6. Hence, we get a random number between 1 to 6. We can repeatedly roll the dice to obtain different numbers from 1 to 6 as long as we want.

This is the classic "roll the dice" game.

How to implement Roll the Dice Game in Python?

To implement the rolling dice game in Python, We will be using the random module. The random module provides us with different functions to generate numbers within a range or select numbers with a range from a list. Since we want to randomize the numbers we get from the dice, we will use the randint() function and the choice() function defined in the random module to implement the game in Python.

Rolling Dice using the randint() Function in Python

To implement the rolling dice game in Python using the randint() function, we will initialize two variables min_value and max_value to the lowest and highest number of dice i.e. 1 and 6 respectively. Then, we will use the randint() function to generate a random integer from 1 to 6. The randint() function takes the minimum value and maximum value of a range as its input arguments and returns a random integer within the range. We will pass the variables min_value and max value to the randint() function to imitate dice rolling by generating a random number from 1 to 6.

To implement the functionality to repeatedly roll the dice, we will use a while loop so that the user can choose to roll the dice again. For this, we will ask the user if they want to roll the dice again. We will assign the user input to a variable roll again. If the user inputs "yes" or "y", we will roll the dice by executing the while loop again. Otherwise, we will come out of the while loop.
