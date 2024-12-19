import pygame
from config import *

def draw_status(screen, text):
    """Vẽ trạng thái phía dưới mê cung"""
    font = pygame.font.Font(None, 24)
    instruction = font.render(text, True, BLACK)
    screen.fill(WHITE, (0, CELL_SIZE * GRID_HEIGHT, SCREEN_WIDTH, STATUS_HEIGHT))  # Làm sạch vùng trạng thái
    screen.blit(instruction, (10, CELL_SIZE * GRID_HEIGHT + 10))  # Hiển thị trạng thái


def draw_maze(screen, maze, start, end, path):
    """Vẽ mê cung, điểm bắt đầu, kết thúc và đường đi"""
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = WHITE
            if maze[row][col] == 1:
                color = BLACK
            elif start == (row, col):
                color = GREEN
            elif end == (row, col):
                color = RED
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    if path:
        for node in path:
            pygame.draw.rect(screen, YELLOW, (node[1] * CELL_SIZE + 10, node[0] * CELL_SIZE + 10, CELL_SIZE - 20, CELL_SIZE - 20))