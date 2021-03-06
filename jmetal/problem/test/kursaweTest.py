import unittest

from jmetal.problem.multiobjective.kursawe import Kursawe

__author__ = "Antonio J. Nebro"


class TestMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_should_constructor_create_a_non_null_object(self):
        problem = Kursawe(3)
        self.assertIsNotNone(problem)

    def test_should_constructor_create_a_valid_problem_with_default_settings(self):
        problem = Kursawe()
        self.assertEqual(3, problem.number_of_variables)
        self.assertEqual(2, problem.number_of_objectives)
        self.assertEqual(0, problem.number_of_constraints)

        self.assertEqual([-5.0, -5.0, -5.0], problem.lower_bound)
        self.assertEqual([5.0, 5.0, 5.0], problem.upper_bound)

    def test_should_constructor_create_a_valid_problem_with_5_variables(self):
        problem = Kursawe(5)
        self.assertEqual(5, problem.number_of_variables)
        self.assertEqual(2, problem.number_of_objectives)
        self.assertEqual(0, problem.number_of_constraints)

        self.assertEqual([-5.0, -5.0, -5.0, -5.0, -5.0], problem.lower_bound)
        self.assertEqual([5.0, 5.0, 5.0, 5.0, 5.0], problem.upper_bound)

    def test_should_create_solution_create_a_valid_float_solution(self):
        problem = Kursawe(3)
        solution = problem.create_solution()

        self.assertEqual(3, solution.number_of_variables)
        self.assertEqual(3, len(solution.variables))
        self.assertEqual(2, solution.number_of_objectives)
        self.assertEqual(2, len(solution.objectives))
        self.assertEqual(0, problem.number_of_constraints)

        self.assertEqual([-5.0, -5.0, -5.0], problem.lower_bound)
        self.assertEqual([5.0, 5.0, 5.0], problem.upper_bound)

        self.assertTrue(solution.variables[0] >= -5.0)
        self.assertTrue(solution.variables[0] <= 5.0)

    def test_should_get_name_return_the_right_name(self):
        problem = Kursawe()
        self.assertEqual("Kursawe", problem.get_name())

if __name__ == '__main__':
    unittest.main()

