# Slot Machine 🎰

## Overview
Implement a slot machine game in Python. The user decides the initial amount of money and is asked how many lines they want to bet on (1 to 3) and how much money to bet per line. 
Afterward, a spin is generated using letters (A, B, C, D) as symbols. If there is a match of three identical symbols in a row, the user wins an amount based on which symbol appears (three A's give the most money, as they are less likely to appear than D's).

## Files
**`constants`**: Defines the size of the slot machine, min and max bet possible, symbols count and symbols values.  
**`utils`**: Functions for specific tasks.  
**`core`**: Contains the two principal functions `deposit` and `spin` to run the machine.  
**`main`**: Script for executing the game.  
