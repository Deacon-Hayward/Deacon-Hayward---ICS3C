import pygame
from collections import deque
import sys

# Initialize Pygame
pygame.init()

# Configuration Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)      # Start Node
RED = (255, 0, 0)        # End Node
BLUE = (0, 120, 255)     # Shortest Path
LIGHT_BLUE = (173, 216, 230) # Visited nodes

# Set up Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame BFS Pathfinding System")

def create_grid(rows, cols):
    """Creates a 2D array representing the map grid (0 = empty, 1 = wall)."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def draw_grid(surface, grid, path, visited):
    """Handles all map rendering."""
    surface.fill(WHITE)
    
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            # Default tile color logic
            if grid[row][col] == 1:
                pygame.draw.rect(surface, BLACK, rect)
            elif (row, col) == start_node:
                pygame.draw.rect(surface, GREEN, rect)
            elif (row, col) == end_node:
                pygame.draw.rect(surface, RED, rect)
            elif (row, col) in path:
                pygame.draw.rect(surface, BLUE, rect)
            elif (row, col) in visited:
                pygame.draw.rect(surface, LIGHT_BLUE, rect)
                
            # Draw grid borders
            pygame.draw.rect(surface, GRAY, rect, 1)

    pygame.display.flip()

def get_bfs_path(grid, start, end):
    """Finds the shortest path on the grid using a Breadth-First Search queue."""
    queue = deque([start])
    came_from = {start: None}
    visited = set([start])
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            break
            
        row, col = current
        # Check 4 cardinal directions (Up, Down, Left, Right)
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        
        for n_row, n_col in neighbors:
            if 0 <= n_row < ROWS and 0 <= n_col < COLS: # Within bounds
                if grid[n_row][n_col] != 1 and (n_row, n_col) not in visited: # Walkable and unvisited
                    queue.append((n_row, n_col))
                    visited.add((n_row, n_col))
                    came_from[(n_row, n_col)] = current

    # Reconstruct the path backwards from end to start
    path = []
    if end in came_from:
        current = end
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
        
    return path, visited

# Core Game Variables
grid = create_grid(ROWS, COLS)
start_node = (2, 2)
end_node = (17, 17)
path, visited = get_bfs_path(grid, start_node, end_node)

# Main Application Loop
drawing_walls = False
erasing_walls = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row = event.pos[1] // CELL_SIZE
            col = event.pos[0] // CELL_SIZE
            if 0 <= row < ROWS and 0 <= col < COLS:
                if event.button == 1: # Left Click draws walls
                    drawing_walls = True
                    if (row, col) not in [start_node, end_node]:
                        grid[row][col] = 1
                elif event.button == 3: # Right Click erases walls
                    erasing_walls = True
                    grid[row][col] = 0
            # Recalculate path instantly
            path, visited = get_bfs_path(grid, start_node, end_node)
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing_walls = False
            erasing_walls = False
            
        elif event.type == pygame.MOUSEMOTION:
            row = event.pos[1] // CELL_SIZE
            col = event.pos[0] // CELL_SIZE
            if 0 <= row < ROWS and 0 <= col < COLS:
                if drawing_walls and (row, col) not in [start_node, end_node]:
                    grid[row][col] = 1
                elif erasing_walls:
                    grid[row][col] = 0
            # Recalculate path instantly as you drag the mouse
            path, visited = get_bfs_path(grid, start_node, end_node)

    draw_grid(screen, grid, path, visited)
