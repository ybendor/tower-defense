import copy
import random
import unittest
from unittest.mock import MagicMock, patch

import enemy
import tower
from extras import Shot
from main import towerDefense


class GameTest(unittest.TestCase):
    def tearDown(self):
        towerDefense._instance = None

    @patch('extras.pygame')
    def test_shot(self, mock_pygame):
        enemy_colours = ["white", "pink", "yellow", "cyan", "maroon"]
        colour = random.choice(enemy_colours)
        dummy_enemy = enemy.Enemy(0, 0, 40, (0, 0), [[]], 5, colour)
        dummy_tower = tower.OrangeTower(0, 0, [[]], 40)
        self.assertEqual(0, len(dummy_tower.shots))
        r = random.randint(0, 10)
        print(r)
        print(colour)
        for i in range(r):
            dummy_tower.fireShot(dummy_enemy)
        self.assertEqual(r, len(dummy_tower.shots))

    def test_getRowCol(self):
        enemy_colours = ["white", "pink", "yellow", "cyan", "maroon"]
        colour = random.choice(enemy_colours)
        dummy_enemy = enemy.Enemy(15, 15, 40, (0, 1), [[]], 5, colour)
        l1 = dummy_enemy.location
        c1 = dummy_enemy.center
        dummy_enemy.moveEnemy()
        l2 = dummy_enemy.location
        c2 = dummy_enemy.center
        print(l1)
        print(l2)
        print(c1)
        print(c2)

    def test_get_color(self):
        tower_classes = (tower.OrangeTower, tower.RedTower,
                         tower.PurpleTower, tower.GreenTower)
        tower_class = random.choice(tower_classes)
        dummy_tower_colour = tower_class.__name__.replace("Tower", "").lower()
        if dummy_tower_colour == "purple":
            dummy_tower_colour = "#8C489F"
        dummy_tower = tower_class(0, 0, [[]], 40)
        self.assertEqual(dummy_tower_colour, dummy_tower.get_color())

    @patch('extras.pygame')
    def test_isOffScreen(self, mock_pygame):
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

        tower_classes = (tower.OrangeTower, tower.RedTower,
                         tower.PurpleTower, tower.GreenTower)
        tower_class = random.choice(tower_classes)
        dummy_tower = tower_class(0, 0, [[]], 40)

        enemy_colours = ["white", "pink", "yellow", "cyan", "maroon"]
        colour = random.choice(enemy_colours)
        dummy_enemy = enemy.Enemy(15, 15, 40, (0, 1), [[]], 5, colour)

        shot = Shot(dummy_tower, dummy_enemy, board, 40)
        nshot = copy.deepcopy(shot)
        index = random.randint(0, 1)
        value = random.randint(0, 100)
        nshot.location[index] = -value
        self.assertEqual(nshot.isOffScreen(), True)
        self.assertEqual(shot.isOffScreen(), False)

    def test_slowSpeed(self):
        enemy_colours = ["white", "pink", "yellow", "cyan", "maroon"]
        colour = random.choice(enemy_colours)
        dummy_enemy = enemy.Enemy(15, 15, 40, (0, 1), [[]], 5, colour)
        dummy_enemy.slowSpeed()
        assert (dummy_enemy.speedFactor == 0.2)

    def test_setSpeedFactor(self):
        enemy_colours = ["white", "pink", "yellow", "cyan", "maroon"]
        colour = random.choice(enemy_colours)
        dummy_enemy = enemy.Enemy(15, 15, 40, (0, 1), [[]], 5, colour)
        if colour == "pink" or colour == "yellow":
            assert (dummy_enemy.speedFactor == 8.0 / 5)
        elif colour == "cyan" or colour == "maroon":
            assert (dummy_enemy.speedFactor == 2.0)
        else:
            assert (dummy_enemy.speedFactor == 1)

    def test_tower_defense_is_a_singleton(self):
        instance = towerDefense()
        self.assertEqual(instance, instance._instance)
        self.assertRaisesRegexp(RuntimeError,
                                expected_regex="This class is a singleton!",
                                callable=towerDefense)

    def test_draw_tower_desc_uses_correct_tower(self):
        def get_tower_defense(boardDim, width, height):
            towerDefense._instance = None
            _td = towerDefense()
            _td.orangeTower = 'Orange'
            _td.redTower = 'Red'
            _td.greenTower = 'Green'
            _td.purpleTower = 'Purple'
            _td.boardDim = boardDim
            _td.width = width
            _td.height = height
            _td.drawTowerIcon = lambda _: None
            _td.drawTowerChars = MagicMock()
            _td.getText = lambda _: 'dummy_text'
            _td.canvas = MagicMock()
            return _td

        button = MagicMock()
        for color in ('Orange', 'Red', 'Green', 'Purple'):
            td = get_tower_defense(1, 2, 3)
            button.iconColor = color
            td.drawTowerDesc(button)
            td.drawTowerChars.assert_called_with(color)
            td.canvas.create_text.assert_called_with(
                -98.5,
                -42,
                text='dummy_text',
                fill='white',
                justify='center')
        td = get_tower_defense(None, None, None)
        button.iconColor = None
        self.assertRaisesRegexp(RuntimeError,
                                'Invalid button icon color.',
                                td.drawTowerDesc,
                                button)
