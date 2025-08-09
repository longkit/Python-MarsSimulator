import pygame
import sys
import random
from pyswip import Prolog

# مقداردهی اولیه Pygame
pygame.init()

# مقداردهی اولیه Prolog
prolog = Prolog()
print("Loading Prolog file...")
prolog.consult("mars_explorer_logic.pl")  # بارگذاری فایل پرولوگ
print("Prolog file loaded successfully!")

# تنظیمات صفحه
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# مقداردهی اولیه صفحه
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mars Explorer")

# متغیرهای اصلی بازی
goal = None
obstacles = set()
rover = None
path_to_goal = []


def random_position():
    return random.randint(0, ROWS - 1), random.randint(0, COLS - 1)


def is_valid(pos):
    x, y = pos
    return 0 <= x < ROWS and 0 <= y < COLS and pos not in obstacles


def draw_grid():
    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    for obs in obstacles:
        x, y = obs
        pygame.draw.rect(screen, RED, (y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    if goal:
        gx, gy = goal
        pygame.draw.rect(screen, BLUE, (gy * TILE_SIZE, gx * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    if rover:
        rx, ry = rover
        pygame.draw.rect(screen, GREEN, (ry * TILE_SIZE, rx * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.flip()


def update_path():
    global path_to_goal
    print("Querying Prolog for path...")
    result = list(prolog.query("find_path(Path)"))
    if result and result[0]["Path"]:
        path_to_goal = result[0]["Path"]
        print("Optimized Path from Prolog:", path_to_goal)
    else:
        print("No path found! Retrying...")
        path_to_goal = []  # جلوگیری از کرش


def initialize_game():
    global goal, rover, obstacles, path_to_goal

    obstacles.clear()
    rover = random_position()
    goal = random_position()

    while goal in obstacles or goal == rover:
        goal = random_position()

    while len(obstacles) < (ROWS * COLS) // 5:
        obs = random_position()
        if obs != rover and obs != goal:
            obstacles.add(obs)

    print("Initializing Prolog facts...")
    prolog.retractall("rover(_, _)")
    prolog.assertz(f"rover({rover[0]}, {rover[1]})")
    prolog.retractall("goal(_, _)")
    prolog.assertz(f"goal({goal[0]}, {goal[1]})")
    prolog.retractall("obstacle(_, _)")

    for obs in obstacles:
        prolog.assertz(f"obstacle({obs[0]}, {obs[1]})")

    print("Prolog facts initialized successfully!")
    update_path()


def set_new_goal():
    global goal, path_to_goal

    goal = random_position()
    while goal in obstacles or goal == rover:
        goal = random_position()

    prolog.retractall("goal(_, _)")
    prolog.assertz(f"goal({goal[0]}, {goal[1]})")

    update_path()


def main():
    clock = pygame.time.Clock()
    print("Initializing game...")
    initialize_game()
    print("Game initialized successfully!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if path_to_goal:
            global rover
            next_step = path_to_goal.pop(0)
            rover = next_step
            prolog.retractall("rover(_, _)")
            prolog.assertz(f"rover({rover[0]}, {rover[1]})")

        draw_grid()
        clock.tick(5)

        if rover == goal:
            print("Reached the goal! Generating a new target...")
            pygame.time.delay(1000)
            set_new_goal()


if __name__ == "__main__":
    main()
