import pygame
import sys
from config import *
from a_star import a_star
from utils import draw_status, draw_maze
from maze import create_empty_maze
from enum import Enum
import time
from maze import create_empty_maze, load_maze


class GameState(Enum):
    SETTING_WALLS = 1
    SELECTING_START = 2
    SELECTING_END = 3
    GAME_RUNNING = 4
    MOVING = 5
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Trò chơi tìm đường trong mê cung")
    clock = pygame.time.Clock()

    maze = create_empty_maze()
    start = None
    end = None
    path = None
    game_state = GameState.SETTING_WALLS  # Sử dụng Enum để quản lý trạng thái
    moving_index = 0  # Chỉ số của bước di chuyển trong đường đi (path)
    moving_position = start  # Vị trí hiện tại của điểm bắt đầu (di chuyển dần dần)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE

                if row < GRID_HEIGHT:
                    if game_state == GameState.SETTING_WALLS:
                        maze[row][col] = 1 if maze[row][col] == 0 else 0
                    elif game_state == GameState.SELECTING_START and maze[row][col] == 0:
                        start = (row, col)
                        game_state = GameState.SELECTING_END
                    elif game_state == GameState.SELECTING_END and maze[row][col] == 0:
                        end = (row, col)
                        game_state = GameState.GAME_RUNNING
                        path = a_star(maze, start, end)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not start and not end:
                    game_state = GameState.SELECTING_START
                elif event.key == pygame.K_r:
                    maze = create_empty_maze()
                    start = None
                    end = None
                    path = None
                    game_state = GameState.SETTING_WALLS
                    moving_index = 0
                    moving_position = start
                elif event.key == pygame.K_1:
                    maze = load_maze(0)  # Chọn Map đầu tiên
                    start, end, path = None, None, None
                    game_state = GameState.SETTING_WALLS
                    moving_index = 0
                    moving_position = start
                elif event.key == pygame.K_2:
                    maze = load_maze(1)  # Chọn Map thứ hai
                    start, end, path = None, None, None
                    game_state = GameState.SETTING_WALLS
                    moving_index = 0
                    moving_position = start
                elif event.key == pygame.K_3:
                    maze = load_maze(2)  # Chọn Map thứ ba
                    start, end, path = None, None, None
                    game_state = GameState.SETTING_WALLS
                    moving_index = 0
                    moving_position = start
                


        screen.fill(WHITE)
        
        if game_state == GameState.GAME_RUNNING and path:
            # Đưa điểm bắt đầu di chuyển dần dần đến điểm kết thúc
            if moving_index < len(path):
                moving_position = path[moving_index]
                moving_index += 1
                # Cập nhật lại mê cung và vẽ lại
                draw_maze(screen, maze, moving_position, end, path)
                draw_status(screen, "Di chuyen den diem ket thuc...")
            else:
                game_state = GameState.GAME_RUNNING  # Đến đích rồi
                draw_maze(screen, maze, moving_position, end, path)
                draw_status(screen, "Da tim thay diem ket thuc!")
        else:
            draw_maze(screen, maze, start, end, path)
            if game_state == GameState.SETTING_WALLS:
                text = "Them tuong: Nhap chuot de ve xoa tuong, Nhan SPACE de chon diem bat dau. Nhan 1, 2, 3 de doi map khac nhau."
            elif game_state == GameState.SELECTING_START:
                text = "Chon diem bat dau: Nhap chuot vao o trong de chon."
            elif game_state == GameState.SELECTING_END:
                text = "Chon diem ket thuc: Nhap chuot vao o trong de chon."
            elif game_state == GameState.GAME_RUNNING:
                text = "Nhan R de khoi dong lai."

            draw_status(screen, text)
        
        pygame.display.flip()
        clock.tick(5)  # Điều chỉnh tốc độ di chuyển của điểm bắt đầu

if __name__ == "__main__":
    main()
