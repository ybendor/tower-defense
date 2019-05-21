# import tkinter as tk
#
#
# class FakeTk(object):
#     def __init__(self):
#         pass
#     def __getattr__(self, name):
#         return ""
#     def mainloop(self):
#         print("hello")
#         pass
#
# tk.__dict__['Tk'] = FakeTk
import unittest
import main
from mock import Mock, MagicMock, patch


class GameTest(unittest.TestCase):
    # Tk, Canvas, ALL
    @patch('animation.Tk')
    @patch('animation.Canvas')
    @patch('animation.ALL')
    def test_example(self, mock_ALL, mock_Canvas, mock_Tk):
        l = []
        app = main.towerDefense()
        app.run()
        app.newEnemyWave()
        with patch.object(towerDefense.enemyWave.wave, l):
            app.addEnemyToWave()
        self.assertEqual(len(app.enemyWave.wave), 1)
        # app.enemyWave.wave.remove = MagicMock()
        # app.enemyWave.wave.remove.assert_called_once_with(enemymock)
