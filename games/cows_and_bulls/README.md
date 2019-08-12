Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end. 
Say the number generated by the computer is 1038. An example interaction could look like this: 

Welcome to the Cows and Bulls Game! 
Enter a number: 
>>> 1234
2 cows, 0 bulls
>>> 1286
1 cow, 1 bull
...

cows - correct place and digit
bulls - correct digit and wrong place
Unlimited chances
Game ends when user guesses the number 
number og tries should be displayed at the end

Steps:
- Creat a variable that is a random 4 digit number between 1000 and 9999 and then covert it into a string.
- Function that takes the number you typed in and displays the cows and bulls messege.
- Create a while loop and start the game (and end it).
- Say # of tries at the end.