#!/usr/bin/env python3
"""
UNIT TESTS FOR ACME RETRO TETRIS ENGINE
"""
import unittest
from tetris import TetrisEngine, BOARD_WIDTH, BOARD_HEIGHT

class TestTetrisEngine(unittest.TestCase):
    def setUp(self):
        self.engine = TetrisEngine(width=10, height=20)

    def test_initial_state(self):
        self.assertFalse(self.engine.game_over)
        self.assertEqual(self.engine.score, 0)
        self.assertEqual(self.engine.lines_cleared, 0)

    def test_line_clear_logic(self):
        # En alt satırı doldur (1 blok hariç)
        self.engine.grid[19] = [1] * 9 + [0]
        self.assertEqual(self.engine.lines_cleared, 0)
        
        # Son bloğu da doldur
        self.engine.grid[19][9] = 1
        self.engine.clear_lines()
        
        # 1 satır temizlenmiş olmalı ve en üst sıfırlanmalı
        self.assertEqual(self.engine.lines_cleared, 1)
        self.assertEqual(self.engine.score, 100)
        self.assertEqual(self.engine.grid[19], [0] * 10)

    def test_boundary_collision(self):
        # Parçayı sol duvara kadar it
        for _ in range(10):
            self.engine.move(-1)
        # Sola daha fazla gidememeli (çarpışma koruması)
        min_x = min(bx for bx, by in self.engine.get_blocks(self.engine.piece_x, self.engine.piece_y, self.engine.rotation_index))
        self.assertGreaterEqual(min_x, 0)

if __name__ == "__main__":
    unittest.main()
