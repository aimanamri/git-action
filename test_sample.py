import unittest
from vector2d import Vector2D
from particle import Particle

class TestParticle(unittest.TestCase):
    def test_distance_to(self):
        p1 = Particle(0, 0, 0, 0)
        p2 = Particle(0, 1, 0, 0)
        self.assertEqual(p1.distance_to(p2), 1)

    def test_get_speed(self):
        p = Particle(0, 0, 1, 1)
        self.assertEqual(p.get_speed(), math.sqrt(2))

if __name__ == '__main__':
    unittest.main()
