import unittest
import app

class ExamApp(unittest.TestCase):
  def setUp(self):
    self.app = app

  def test_generate_progression(self):
    self.assertEqual(len(app.generateProgression(1, 1, 10)), 10)
    self.assertEqual(len(app.generateProgression(-5, -2, 50)), 50)
    with self.assertRaises(TypeError):
      app.generateProgression('start', 5, 20)
    with self.assertRaises(ValueError):
      app.generateProgression(10, 5, 'n')
  
  def test_count_sum(self):
    self.assertEqual(app.countSum(app.generateProgression(3, 6, 10)), 300)
    self.assertEqual(app.countSum(app.generateProgression(-4, -2, 20)), -460)
    with self.assertRaises(TypeError):
      app.countSum(None)

  def tearDown(self):
    pass

if __name__ == '__main__':
  unittest.main()