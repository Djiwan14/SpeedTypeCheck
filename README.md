# FastTyping

## Overview

FastTyping is a simple speed typing test application built with Python's Tkinter library. It displays a random phrase from a predefined list, and the user must type the phrase as quickly as possible. After typing, the application calculates and displays the typing speed in words per minute.

## Features

- Displays a random phrase for typing practice.
- Measures and displays typing speed in words per minute.
- Provides feedback on whether the typed phrase matches the given phrase.
- Reset button to start a new typing test.

## Using the Application:

- The application will display a random phrase to type.
- Type the phrase into the text entry box and press Enter.
- The application will display your typing speed and feedback based on your input.
- Click the "Reset" button to get a new phrase and start the typing test again.

## Code Explanation
- FastTyping class:

Inherits from Tk and sets up the GUI.
Initializes the main window with labels, an entry widget, and a reset button.
Displays a random phrase and measures typing speed when the user presses Enter.
Resets and updates the phrase after a short delay.
- getNewPhrase method:

Selects a random phrase from the list.
Displays the phrase and clears the entry widget.
Records the start time for timing the typing.
- check_word method:

Compares the typed phrase with the displayed phrase.
Calculates and displays the typing speed if the phrases match.
Provides feedback if the phrases don't match.
Schedules a new phrase to be displayed after 1.5 seconds
