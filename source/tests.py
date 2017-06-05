import sys
import unittest
from io import StringIO

from source.solvers import Solver


class SolverTest(unittest.TestCase):

    def test_determine_genuity(self):
        solver = Solver(["@Twitter costam lalal Wodecki nie żyje",
                         "@Twitter costam lalal Wodecki nie żyje",
                         "@Twitter costam lalal Wodecki nie żyje",
                         "@Twitter costam lalal Wodecki nie żyje"]
                        , "Wodecki nie żyje")
        capturedoutput = StringIO()
        sys.stdout = capturedoutput
        solver.determine_genuity()
        sys.stdout = sys.__stdout__
        # print('Captured', capturedOutput.getvalue())
        self.assertEqual(capturedoutput.getvalue(), "This is presumably true")

        # dla pustej listy
        solver2 = Solver([], "Wodecki nie żyje")
        capturedoutput2 = StringIO()
        sys.stdout = capturedoutput
        solver2.determine_genuity()
        sys.stdout = sys.__stdout__
        # print('Captured', capturedOutput.getvalue())
        self.assertEqual(capturedoutput2.getvalue(), "This is fake :(, presumably..")

unittest.main()
