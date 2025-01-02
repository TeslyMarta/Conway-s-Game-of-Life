import random
import time

def check_and_update(matrix):
    """
    Updates the state of the matrix according to the rules of the "Game of Life" (Conway's Game of Life).
    
    Parameters:
    matrix (list of list of int): The input matrix representing the state of cells.

    Returns:
    list of list of int: The updated matrix with new states of cells.
    """
    rows, columns = len(matrix), len(matrix[0])
    new_matrix = [[matrix[i][j] for j in range(columns)] for i in range(rows)]  # Copy of the matrix

    for i in range(rows):
        for j in range(columns):
            sum_ones = 0

            # Checking neighbors (cells adjacent to the current one)
            for a in [-1, 0, 1]:  # Checking row neighbors
                for b in [-1, 0, 1]:  # Checking column neighbors
                    if (a != 0 or b != 0) and 0 <= i + a < rows and 0 <= j + b < columns:
                        if matrix[i + a][j + b] == 1:  # If the neighbor is alive (1)
                            sum_ones += 1

            # Applying rules to decide if the cell should live or die
            if matrix[i][j] == 1 and (sum_ones < 2 or sum_ones > 3):
                new_matrix[i][j] = 0  # Cell dies due to underpopulation or overpopulation
            elif matrix[i][j] == 0 and sum_ones == 3:
                new_matrix[i][j] = 1  # Cell becomes alive due to reproduction

    return new_matrix 

def print_matrix(matrix):
    """
    Prints the matrix to the screen.
    """
    print("\n".join(" ".join(str(cell) for cell in row) for row in matrix))
    print()

def main():
    """
    Main function to run the "Game of Life".
    """
    rows, columns = 5, 5
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]  # Initial matrix, all cells are dead
    
    # Randomly choose 5 positions to set as alive cells (1)
    num_ones = 5
    positions = random.sample(range(rows * columns), num_ones)
    for pos in positions:
        matrix[pos // columns][pos % columns] = 1

    previous_matrix = None
    repeat_count = 0

    while True:
        print_matrix(matrix)  
        time.sleep(1)  # Sleep for 1 second before updating the matrix
        matrix = check_and_update(matrix)  # Update the matrix with new state

        # Check if the matrix repeats (i.e., no change for 3 consecutive iterations)
        if matrix == previous_matrix:
            repeat_count += 1
        else:
            repeat_count = 0  # Reset count if matrix changes

        previous_matrix = matrix

        # If the matrix repeats 3 times, stop the game
        if repeat_count >= 3:
            print("Game stopped! The matrix repeats 3 times.")
            break

        # If there are no alive cells left, end the game
        if not any(1 in row for row in matrix):
            print("Game over! All cells are dead.")
            break

main()