# Maze Runner

This repository contains Python scripts for generating and solving mazes using a graphical user interface (GUI) built with tkinter.

## Contents

- `blackpill.py`: Python script for generating and solving mazes, with one entrance and exit point.
- `whitepill.py`: Python script for generating and solving mazes, with additional starting and ending points.

## How to Use

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Run either `redpill.py` or `bluepill.py` using Python.
4. Click the "Generate Maze" button to generate a maze and its solution (if exists).
5. The generated maze will be displayed on the tkinter canvas.

## Maze Generation Algorithm

The maze generation algorithm used is a randomized version of the depth-first search algorithm. It creates a maze by randomly removing walls between cells while ensuring connectivity between the entrance and exit points.

## Maze Solving Algorithm

The maze solving algorithm used is a depth-first search (DFS) algorithm. It explores the maze to find a path from the entrance to the exit, if one exists.

## Dependencies

- Python 3.x
- tkinter (Python's standard GUI toolkit)
