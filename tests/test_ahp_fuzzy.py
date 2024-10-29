import unittest
from ahp_fuzzy_lib import AHP_FuzzyAHP

class TestAHPFuzzyAHP(unittest.TestCase):
    def test_calculate_weights(self):
        ahp_fuzzy = AHP_FuzzyAHP()
        comp_mat = [[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]]
        eval_mat = [[0.8, 0.2, 0.5], [0.6, 0.7, 0.3]]
        
        weights_ahp, weights_fuzzy_ahp, final_scores = ahp_fuzzy.calculate_weights(comp_mat, eval_mat)
        
        # Assert that weights and scores are calculated (example of simple check)
        self.assertEqual(len(weights_ahp), 3)
        self.assertEqual(len(weights_fuzzy_ahp), 3)
        self.assertEqual(len(final_scores), 2)

if __name__ == "__main__":
    unittest.main()