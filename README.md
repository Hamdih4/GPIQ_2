# Hangman Game

The Hangman Game is a mini game that gives user 5 tries to guess the hidden words, for each guessed the player adds 10 points to his score.

```
EX: exe
$ hangman

Ex: Python
$ python hangman.py

Ex: Ruby
$ ruby hangman.rb
```

## Starting the Game

* The game doesn't have a GUI, it can be started from the command line.

```
$ hangman
```

* When starting the game for the first time, the player starts with score 0.

```
$ hangman

Hangman Game 1.0
Score: 0 Level: 1
Guess the word: * * * * *
5 tries left
What is your next guess?
```

* Starting the game afterwards counts how many points were in the player's pocket (Saved in score file or score table).

```
$ hangman

Hangman Game 1.0
Score: 30 Level: 1
Guess the word: * * *
5 tries left
What is your next guess?
```

## Game Play

* The game gives 5 tries for each word to be guessed, the player receives 10 points if the word was guessed, otherwise the player receives no points.

* The game loads a random word from the words DB (or file), the word gets selected randomly for each level. Here is the list of words for the game:

```
hammer
bat
knife
keyboard
mouse
green
table
monitor
water
vehicle
```

* When the player guess the word, the game shows a new word and goes to the next level and updates the player's score.

* The score and the level will be stored for the player, so next time the player starts the game, the game will show his stored score and last level played.

### Scenario 1: Winning

```
$ hangman

Hangman Game 1.0
Score: 0 Level: 1
Guess the word: * * * * *
5 tries left
What is your next guess? w

Guess the word: w * * * *
5 tries left
What is your next guess? e

Guess the word: w * * e *
5 tries left
What is your next guess? s

Guess the word: w * * e *
4 tries left
What is your next guess? o

Guess the word: w * * e *
3 tries left
What is your next guess? r

Guess the word: w * * e r
3 tries left
What is your next guess? a

Guess the word: w a * e r
3 tries left
What is your next guess? t

Correct, the word is: water

Score: 10 Level: 2
Guess the word: * * * * *
5 tries left
What is your next guess? quit

$ ..
```

### Scenario 2: Losing

```
$ hangman

Hangman Game 1.0
Score: 10 Level: 2
Guess the word: * * * * *
5 tries left
What is your next guess? w

Guess the word: * * * * *
4 tries left
What is your next guess? e

Guess the word: * * e e *
4 tries left
What is your next guess? t

Guess the word: * * e e *
3 tries left
What is your next guess? o

Guess the word: * * e e *
2 tries left
What is your next guess? r

Guess the word: * r e e *
2 tries left
What is your next guess? a

Guess the word: * r e e *
Last try left
What is your next guess? t

Sorry, you missed this one, the word was: green

Score: 10 Level: 2
Guess the word: * * * * *
5 tries left
What is your next guess? quit

$ ..
```
