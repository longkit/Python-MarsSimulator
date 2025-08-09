# Mars Explorer Project

## Project Overview  
Mars Explorer is a grid-based simulation game where a rover autonomously navigates a Mars-like terrain filled with obstacles to reach a randomly assigned goal. The pathfinding logic leverages Prolog’s logical programming capabilities, interfaced seamlessly with Python’s Pygame for visualization and game management.

## Features  
- **Grid Environment:** 12x16 grid representing the Mars surface.  
- **Dynamic Obstacles:** Randomly placed obstacles block the rover’s path.  
- **Autonomous Rover:** The rover moves step-by-step towards the goal using the shortest path.  
- **Prolog BFS Pathfinding:** Breadth-First Search implemented in Prolog finds the optimal path considering obstacles.  
- **Python GUI:** Interactive visualization with Pygame showing rover, obstacles, and goal in real time.  
- **Seamless Python-Prolog Integration:** Uses PySWIP to assert facts and query Prolog dynamically.

## Installation & Setup  
1. Install Python 3.x  
2. Install Pygame:  
   ```bash
   pip install pygame
