# HangmanGame
This is a Git repository that contains the Python script for 
Assignment 3 of _Introduction in Python Programming_ Part Time Course of Cardiff University.

A Python script, named game.py, which enables a user to guess all the letters in a word selected at random from a text file.

The program selects a word at random from the words stored in a text file, displays an asterisk for each letter of the selected word, and prompts the user to enter
a guess at a letter contained in the word. If the letter exists in the word, the asterisk is replaced by the letter at each occurrence of the letter within the
word.

The user is given a specified number of guesses to guess all the letters in the word and, if the user is successful, the message "Well Done" is
displayed on the screen. However, if the user is not successful, the message "Hard Luck" is displayed on the screen.

If all the words to be used by the program are stored in a file words and the user wishes to try and guess all the letters in the randomly selected word
in 8 guesses, the Python script may be executed as follows: **python game.py words 8**.

We assume the content of the file words comprises lowercase letters.
A guess of a single alphabetic character reduces the number of guesses remaining by one. 
The comparison of the letter guess and the letter in the word is case insensitive.
Invalid input does not count as a guess.
