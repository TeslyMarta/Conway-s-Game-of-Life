# Game Description
This code implements the "Game of Life" (Conway's Game of Life), where cells can be either alive or dead, and their next state depends on the number of living neighbors. If a cell has two or three living neighbors, it stays alive; if it has fewer, it dies; and if it has more, it also dies. If a cell is dead but has exactly three living neighbors, it becomes alive.

# How I Created This Project
I learned about this game from the book "Automate the Boring Stuff with Python" and decided to implement it in my own way. This is my first project in Python; I just started learning it from this book. It took me 2 hours to write the code. Before this, I had experience in programming with C++, so writing this code wasn't difficult for me.

# How the Code Works
The code creates a grid of cells, where live cells are randomly filled. It then checks the cells' states according to the rules of the game and updates them, repeating this until the grid stabilizes or all the cells die.

# Error Handling
The code also checks if the cells are within the grid boundaries and if all parameters are correct. If everything is fine, the game continues. However, if the grid repeats three times or all the cells die, the game stops.
