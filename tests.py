import unittest
from solvers import Solver


class SolverTest(unittest.TestCase):

    def determine_genuity(self):

        solver = Solver(["@Twitter costam lalal Wodecki nie żyje",
                         "@Twitter costam lalal Wodecki nie żyje",
                         "@Twitter costam lalal Wodecki nie żyje",
                         "@Twitter costam lalal Wodecki nie żyje"]
                        , "Wodecki nie żyje")
        self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

unittest.main()
