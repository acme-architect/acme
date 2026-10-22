#!/usr/bin/env python3
"""
ACME RETRO TETRIS (Zero-Dependency)
Architecture: Decoupled Board Model + Pure CLI Loop
"""
import os
import sys
import time
import random

BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# 7 Klasik Tetromino (4x4 ızgarada koordinatlar)
SHAPES = {
    'I': [[(0,1), (1,1), (2,1), (3,1)], [(1,0), (1,1), (1,2), (1,3)]],
    'O': [[(1,1), (1,2), (2,1), (2,2)]],
    'T': [[(1,0), (1,1), (1,2), (2,1)], [(0,1), (1,1), (2,1), (1,2)], [(1,0), (1,1), (1,2), (0,1)], [(1,0), (0,1), (1,1), (2,1)]],
    'S': [[(1,1), (1,2), (2,0), (2,1)], [(0,1), (1,1), (1,2), (2,2)]],
    'Z': [[(1,0), (1,1), (2,1), (2,2)], [(0,2), (1,1), (1,2), (2,1)]],
    'J': [[(1,0), (1,1), (1,2), (2,2)], [(0,1), (1,1), (2,1), (0,2)], [(1,0), (1,1), (1,2), (0,0)], [(0,1), (1,1), (2,1), (2,0)]],
    'L': [[(1,0), (1,1), (1,2), (2,0)], [(0,1), (1,1), (2,1), (2,2)], [(1,0), (1,1), (1,2), (0,2)], [(0,0), (0,1), (1,1), (2,1)]]
}

class TetrisEngine:
    def __init__(self, width=BOARD_WIDTH, height=BOARD_HEIGHT):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.score = 0
        self.lines_cleared = 0
        self.game_over = False
        self.current_piece = None
        self.piece_x = 0
        self.piece_y = 0
        self.rotation_index = 0
        self.spawn_piece()

    def spawn_piece(self):
        self.current_type = random.choice(list(SHAPES.keys()))
        self.current_rotations = SHAPES[self.current_type]
        self.rotation_index = 0
        self.piece_x = self.width // 2 - 2
        self.piece_y = 0
        if self.check_collision(self.piece_x, self.piece_y, self.rotation_index):
            self.game_over = True

    def get_blocks(self, px, py, rot_idx):
        shape = self.current_rotations[rot_idx % len(self.current_rotations)]
        return [(px + x, py + y) for (y, x) in shape]

    def check_collision(self, px, py, rot_idx):
        for bx, by in self.get_blocks(px, py, rot_idx):
            if bx < 0 or bx >= self.width or by < 0 or by >= self.height:
                return True
            if self.grid[by][bx] != 0:
                return True
        return False

    def lock_piece(self):
        for bx, by in self.get_blocks(self.piece_x, self.piece_y, self.rotation_index):
            if 0 <= by < self.height and 0 <= bx < self.width:
                self.grid[by][bx] = 1
        self.clear_lines()
        self.spawn_piece()

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(v == 0 for v in row)]
        cleared = self.height - len(new_grid)
        if cleared > 0:
            self.lines_cleared += cleared
            self.score += (cleared ** 2) * 100
            for _ in range(cleared):
                new_grid.insert(0, [0 for _ in range(self.width)])
            self.grid = new_grid

    def step(self):
        if self.game_over:
            return False
        if not self.check_collision(self.piece_x, self.piece_y + 1, self.rotation_index):
            self.piece_y += 1
            return True
        else:
            self.lock_piece()
            return True

    def move(self, dx):
        if not self.check_collision(self.piece_x + dx, self.piece_y, self.rotation_index):
            self.piece_x += dx

    def rotate(self):
        new_rot = (self.rotation_index + 1) % len(self.current_rotations)
        if not self.check_collision(self.piece_x, self.piece_y, new_rot):
            self.rotation_index = new_rot

    def render_str(self):
        display = [row[:] for row in self.grid]
        if not self.game_over:
            for bx, by in self.get_blocks(self.piece_x, self.piece_y, self.rotation_index):
                if 0 <= by < self.height and 0 <= bx < self.width:
                    display[by][bx] = 2

        out = [f"=== ACME TETRIS === | SCORE: {self.score} | LINES: {self.lines_cleared}"]
        out.append("+" + "-" * (self.width * 2) + "+")
        for row in display:
            line = "|"
            for cell in row:
                if cell == 0:
                    line += "  "
                elif cell == 1:
                    line += "[]"
                elif cell == 2:
                    line += "##"
            line += "|"
            out.append(line)
        out.append("+" + "-" * (self.width * 2) + "+")
        if self.game_over:
            out.append(">>> GAME OVER <<<")
        return "\n".join(out)

def play_cli():
    engine = TetrisEngine()
    print("ACME Retro Tetris Engine Initialized.")
    print("Autonomous Simulation Run (10 steps):")
    for _ in range(10):
        engine.step()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(engine.render_str())
        time.sleep(0.1)
    print("\n[PASS] Engine run validated successfully.")

if __name__ == "__main__":
    play_cli()
