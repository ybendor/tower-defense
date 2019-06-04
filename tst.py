import unittest
import enemy
import tower
from unittest.mock import patch
import random



class GameTest(unittest.TestCase):
    # Tk, Canvas, ALL
    @patch('animation.Tk')
    @patch('animation.Canvas')
    @patch('animation.ALL')
    def test_example(self, mock_ALL, mock_Canvas, mock_Tk):
        # l = []
        # app = main.towerDefense()
        # app.run()
        # app.newEnemyWave()
        # with patch.object(main.towerDefense.enemyWave.wave, l):
        #    app.addEnemyToWave()
        # self.assertEqual(len(app.enemyWave.wave), 1)
        # app.enemyWave.wave.remove = MagicMock()
        # app.enemyWave.wave.remove.assert_called_once_with(enemymock)
        pass

    def test_shot(self):
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

    def test_isOffScreen(self):
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

        shot = Shot(dummy_tower,dummy_enemy,board,40)
        nshot = copy.deepcopy(shot)
        index = random.randint(0, 1)
        value = random.randint(0,100)
        nshot.location[index] = -value
        self.assertEqual(nshot.isOffScreen(),True)
        self.assertEqual(shot.isOffScreen(), False)

    def test_slowSpeed(self):
        enemy_colours = ["white", "pink", "yellow", "cyan", "maroon"]
        colour = random.choice(enemy_colours)
        dummy_enemy = enemy.Enemy(15, 15, 40, (0, 1), [[]], 5, colour)
        dummy_enemy.slowSpeed()
        assert(dummy_enemy.speedFactor == 0.2)

    def test_setSpeedFactor(self):
        enemy_colours = ["white", "pink", "yellow", "cyan", "maroon"]
        colour = random.choice(enemy_colours)
        dummy_enemy = enemy.Enemy(15, 15, 40, (0, 1), [[]], 5, colour)
        if colour == "pink" or colour == "yellow":
            assert(dummy_enemy.speedFactor == 8.0/5)
        elif colour == "cyan" or colour == "maroon":
            assert(dummy_enemy.speedFactor == 2.0)
        else:
            assert(dummy_enemy.speedFactor == 1)

    def test_checkCanBuyTower(self):
        # dummy_game = main.towerDefense()
        # money = random.randint(0, 100)
        # dummy_game.money = money
        # tower_colours = ["Orange", "Red", "Green", "Purple"]
        # colour = random.choice(tower_colours)
        # colours += "Tower"
        # dummy_game.checkCanBuyTower(colour)
        # assert(self.money >= tower.colour.cost)
        pass
