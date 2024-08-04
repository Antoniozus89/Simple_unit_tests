import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runer = Runner("TestWalker")
        for _ in range(10):
            runer.walk()
        self.assertEqual(runer.distance, 50)

    def test_run(self):
        runer = Runner("TestRunner")
        for _ in range(10):
            runer.run()
        self.assertEqual(runer.distance, 100)

    def test_challenge(self):
        man1 = Runner("Anton")
        man2 = Runner("John")

        for _ in range(10):
            man1.run()
            man2.walk()

if __name__ == '__main__':
    unittest.main()
