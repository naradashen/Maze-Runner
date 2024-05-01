import tkinter as tk
import random

# Maze parameters
MAZE_WIDTH = 25
MAZE_HEIGHT = 20
CELL_SIZE = 30

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def generate_maze(self):
        # Initialize grid with walls
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]

        # Make random starting point
        stack = [(random.randint(0, self.height - 1), random.randint(0, self.width - 1))]

        while stack:
            current = stack[-1]
            neighbors = [(current[0] - 2, current[1]), (current[0] + 2, current[1]), (current[0], current[1] - 2),
                         (current[0], current[1] + 2)]
            unvisited_neighbors = []
            for n in neighbors:
                if 0 <= n[0] < self.height and 0 <= n[1] < self.width and self.grid[n[0]][n[1]] == 1:
                    unvisited_neighbors.append(n)

            if unvisited_neighbors:
                next_cell = random.choice(unvisited_neighbors)
                self.grid[next_cell[0]][next_cell[1]] = 0
                self.grid[current[0] + (next_cell[0] - current[0]) // 2][current[1] + (next_cell[1] - current[1]) // 2] = 0
                stack.append(next_cell)
            else:
                stack.pop()

        # Make sure the entrance and exit are open
        self.grid[0][1] = 0  # Entrance
        self.grid[self.height - 1][self.width - 2] = 0  # Exit

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()
        self.solutions = []

    def solve_maze(self, start, end):
        self.dfs(start, end, [])
        return self.solutions

    def dfs(self, current, end, path):
        path.append(current)
        if current == end:
            self.solutions.append(path)
            return
        self.visited.add(current)
        for neighbor in self.get_neighbors(current):
            if neighbor not in self.visited:
                self.dfs(neighbor, end, path[:])  # Pass a copy of the current path
        path.pop()  # Backtrack

    def get_neighbors(self, cell):
        row, col = cell
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(self.maze) and 0 <= nc < len(self.maze[0]) and self.maze[nr][nc] == 0:
                neighbors.append((nr, nc))
        return neighbors

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=MAZE_WIDTH*CELL_SIZE, height=MAZE_HEIGHT*CELL_SIZE)
        self.canvas.pack()
        self.generate_button = tk.Button(root, text="Generate Maze", command=self.generate_and_solve_maze)
        self.generate_button.pack()
        self.maze_generator = MazeGenerator(MAZE_WIDTH, MAZE_HEIGHT)
        self.maze_solver = None
        self.solution_id = None

        # Generate initial maze
        self.generate_and_solve_maze()

    def generate_and_solve_maze(self):
        # Clear previous maze and solution
        self.canvas.delete("all")
        if self.solution_id:
            self.canvas.delete(self.solution_id)

        # Generate maze
        self.maze_generator.generate_maze()
        self.draw_maze()

        # Solve maze
        self.maze_solver = MazeSolver(self.maze_generator.grid)
        start = (0, 0)
        end = (MAZE_HEIGHT - 1, MAZE_WIDTH - 1)
        solutions = self.maze_solver.solve_maze(start, end)
        if solutions:
            print("Maze solved!")
            print("Solution paths:", solutions)
            self.draw_solution(solutions[0])  # Draw the first solution found
        else:
            print("No solution found!")

    def draw_maze(self):
        for i in range(MAZE_HEIGHT):
            for j in range(MAZE_WIDTH):
                if self.maze_generator.grid[i][j] == 1:
                    self.canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill="black")
                elif (i, j) == (0, 1):  # Starting point
                    self.canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill="green")
                elif (i, j) == (MAZE_HEIGHT - 1, MAZE_WIDTH - 2):  # End point
                    self.canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill="green")

    def draw_solution(self, solution):
        for i in range(len(solution) - 1):
            current = solution[i]
            next_cell = solution[i + 1]
            self.solution_id = self.canvas.create_line(current[1]*CELL_SIZE + CELL_SIZE//2, current[0]*CELL_SIZE + CELL_SIZE//2,
                                    next_cell[1]*CELL_SIZE + CELL_SIZE//2, next_cell[0]*CELL_SIZE + CELL_SIZE//2,
                                    fill="red", width=2)

root = tk.Tk()
app = MazeApp(root)
root.mainloop()
