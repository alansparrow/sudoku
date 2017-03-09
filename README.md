# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: I used the property of Naked Twins boxes to reduce the set of possible digits 
of other boxes in the same unit (as these boxes have Sudoku's constraints). 
After each round of Nake Twins Elimination, I can see that constraints for other
parts of the unit appear, so my search space is reduced gradually (the constraints are propagated to other region) 
(Constrain Propagation is about using local constraints in a space to reduce the search space. 
As we enforce each constraint, we see how it introduces new constraints for other parts of the board
that can help us further reduce the number of possibilities.)

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: I added 2 new units which are 2 diagonal units to unitlist . 
These units introduce new constraints when the algorithm does the elimination.
(some boxes have more peers than others). Round after round runing 
the algorithm, the constraints will be propagated to new region (other boxes).

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.