import Assignment4
import unittest

class TestSequence(unittest.TestCase):

    def test_possible1(self):
        self.assertEqual(Assignment4.Count_kmers_possible('ATTTGGATT', 2), 8)
    def test_possible2(self):
        self.assertRaises(ValueError, Assignment4.Count_kmers_possible,'',2)
    def test_possible3(self):
        self.assertEqual(Assignment4.Count_kmers_possible('AAAAAAAAA', 2), 8)

    def test_observe(self):
        self.assertEqual(len(Assignment4.Count_kmers_observed('ATTTGGATT')), 9)
    def test_observe1(self):
        self.assertEqual(len(Assignment4.Count_kmers_observed('')), 0)
    def test_observe2(self):
        self.assertEqual(Assignment4.Count_kmers_observed('AAAAAAAAA')['observed'].sum(), 9)
    def test_observe3(self):
        self.assertEqual(Assignment4.Count_kmers_observed('AAAAAAAAA')['posibility'].sum(),40)

if __name__ == '__main__':
    unittest.main()
