import tkinter as tk


class FakeTk(object):
    def __init__(self):
        pass
    def __getattr__(self, name):
        return ""
    def mainloop(self):
        print("hello")
        pass

tk.__dict__['Tk'] = FakeTk
import unittest
from main import *
from unittest.mock import Mock,MagicMock, patch


class GameTest(unittest.TestCase):
    def test_example(self):
        l = []
        app = towerDefense()
        app.run()
        app.newEnemyWave()
        with patch.object(towerDefense.enemyWave.wave, l):
            app.addEnemyToWave()
            assert len(l) == 1
        #app.enemyWave.wave.remove = MagicMock()
        #app.enemyWave.wave.remove.assert_called_once_with(enemymock)
    def test_shot(self):
        return
        board = [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3]]
        enemy = Mock()
        redTower = RedTower(0, 0, board, 40)
        before = len(redTower.shots)
        redTower.fireShot(enemy)
        after = len(redTower.shots)
        assert before+1 == after


if __name__ == '__main__':
    unittest.main()
