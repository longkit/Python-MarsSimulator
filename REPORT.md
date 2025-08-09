
# Mars Explorer Project Report

## Introduction  
Mars Explorer is a hybrid project combining logical programming and graphical simulation to create an intelligent agent (rover) navigating a hazardous environment. The project demonstrates integration between Python and Prolog for AI pathfinding and real-time game visualization.

## Design and Implementation

### Prolog Logic  
- **Dynamic Facts:** Positions of rover, goal, and obstacles are represented as dynamic predicates allowing runtime updates.  
- **Movement Model:** The rover can move in four cardinal directions, with positions validated against grid boundaries and obstacle locations.  
- **Pathfinding Algorithm:** BFS algorithm guarantees shortest path discovery, exploring neighbors in layers until reaching the goal. The path is then reversed for stepwise execution by the rover.

### Python Interface  
- **Pygame Visualization:** The grid, rover, goal, and obstacles are rendered using colored tiles for clarity.  
- **Game Loop:** The rover moves along the path retrieved from Prolog, updating its position and the Prolog knowledge base accordingly.  
- **Dynamic Environment:** Obstacles and goals are randomized on game initialization and after goal completion, demonstrating dynamic updates and re-planning.

## Challenges  
- Integrating Python with Prolog required careful management of facts with `assertz` and `retractall` to keep knowledge synchronized.  
- Handling cases where no path exists gracefully without crashing the application.  
- Ensuring smooth real-time rendering at a reasonable frame rate.

## Future Improvements  
- Implementing heuristic searches like A* for scalability.  
- Adding rover sensors or limited knowledge to simulate partial observability.  
- Introducing diagonal movement and variable terrain costs for realism.  
- Extending GUI with more interactive controls and status display.

## Conclusion  
This project successfully showcases the synergy between declarative logic programming and imperative game programming, providing a compelling example of AI-driven navigation in uncertain environments.
