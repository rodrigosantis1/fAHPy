import numpy as np
import matplotlib.pyplot as plt

class AHP_FuzzyAHP:
    def __init__(self):
        # Initialize Saaty scale
        self.sclSaaty = {1: 1, 3: 1/3, 5: 1/5, 7: 1/7, 9: 1/9}
        # Random Consistency Index for AHP
        self.RI = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]
        # Fuzzy triangular numbers (TFN) constants
        self.fuzzyTFN = {
            1: ([1, 1, 1], [1, 1, 1]),
            3: ([1, 3/2, 2], [1/2, 2/3, 1]),
            5: ([3/2, 2, 5/2], [2/5, 1/2, 2/3]),
            7: ([2, 5/2, 3], [1/3, 2/5, 1/2]),
            9: ([5/2, 3, 7/2], [2/7, 1/3, 5/2])
        }

    def plot_fuzzy_tfn(self):
        plt.figure(figsize=(10, 6))
        for key, (fuzzy_number, _) in self.fuzzyTFN.items():
            x_vals = [fuzzy_number[0], fuzzy_number[1], fuzzy_number[2]]
            y_vals = [0, 1, 0]
            plt.plot(x_vals, y_vals, label=f'TFN {key}')
        
        plt.title("Triangular Fuzzy Number (TFN) Distribution")
        plt.xlabel("Value")
        plt.ylabel("Membership Degree")
        plt.legend()
        plt.grid(True)
        plt.show()

    def consistency_ahp(self, comp_mat):
        eigvals, _ = np.linalg.eig(comp_mat)
        lambda_max = max(eigvals)
        n = comp_mat.shape[0]
        ci = (lambda_max - n) / (n - 1)
        cr = ci / self.RI[n - 1]
        
        if cr > 0.10:
            print(f'CR is {cr:.2f}. Subjective evaluation is NOT consistent!!!')
        return cr

    def ahp(self, comp_mat):
        m, n = comp_mat.shape
        ahp_comp_mat = np.zeros((m, n))
        
        # Convert comparison matrix using Saaty scale
        for i in range(m):
            for j in range(n):
                criteria = comp_mat[i, j]
                if criteria >= 1:
                    ahp_comp_mat[i, j] = self.sclSaaty[criteria]
                else:
                    ahp_comp_mat[i, j] = self.sclSaaty[round(1 / criteria)]
        
        cr = self.consistency_ahp(ahp_comp_mat)
        print(f'Consistency Rate (CR) of A: {cr}')

        vec = np.prod(ahp_comp_mat, axis=1)**(1 / m)
        weights = vec / np.sum(vec)
        return weights


    def fuzzy_ahp(self, comp_mat):
        m, n = comp_mat.shape
        fuzzy_comp_mat_cell = {}

        # Convert comparison matrix using fuzzy numbers
        for i in range(m):
            for j in range(n):
                criteria = comp_mat[i, j]
                if criteria >= 1:
                    fuzzy_comp_mat_cell[(i, j)] = self.fuzzyTFN[criteria][0]
                else:
                    fuzzy_comp_mat_cell[(i, j)] = self.fuzzyTFN[round(1 / criteria)][1]

        m_extend_analysis = {}
        for i in range(m):
            vec = np.array([fuzzy_comp_mat_cell[(i, j)] for j in range(n)])
            m_extend_analysis[i] = np.sum(vec, axis=0)
        
        m_extend_analysis_sum = np.sum(np.array(list(m_extend_analysis.values())), axis=0)
        weights = np.zeros(m)
        
        for i in range(m):
            weights[i] = min([1 if m_extend_analysis[i][1] >= m_extend_analysis[j][1]
                              else 0 if m_extend_analysis[j][0] >= m_extend_analysis[i][2]
                              else (m_extend_analysis[j][0] - m_extend_analysis[i][2]) / 
                                   ((m_extend_analysis[i][1] - m_extend_analysis[i][2]) -
                                    (m_extend_analysis[j][1] - m_extend_analysis[j][0]))
                              for j in range(m) if i != j])
        
        weights /= np.sum(weights)
        return weights

    def calculate_weights(self, comp_mat, eval_mat):
        # Prepare the A matrix
        m, n = comp_mat.shape
        for i in range(m):
            for j in range(i + 1, m):
                comp_mat[j, i] = 1 / comp_mat[i, j]
        
        # Calculate weights using AHP and Fuzzy AHP methods
        weights_ahp = self.ahp(comp_mat)
        weights_fuzzy_ahp = self.fuzzy_ahp(comp_mat)

        # Proximity index for alternatives
        s = eval_mat @ weights_fuzzy_ahp
        print(f'Final score of suppliers (S): {s}')
        return weights_ahp, weights_fuzzy_ahp, s

# Example usage
if __name__ == "__main__":
    # Define a comparison matrix (example data)
    comp_mat = np.array([
        [1, 3, 5],
        [1/3, 1, 3],
        [1/5, 1/3, 1]
    ])

    comp_mat = np.array([
        [1,   5, 1, 5, 1/5, 1, 1, 1/5],
        [0, 1, 1/3, 1/5, 1/7, 1/5, 1/5, 1/5],
        [0, 0, 1, 1, 1/5, 1, 1, 1/5],
        [0, 0, 0, 1, 1/5, 1, 1, 1/5],
        [0, 0, 0, 0, 1, 5, 5, 5],
        [0, 0, 0, 0, 0, 1, 1, 1/5],
        [0, 0, 0, 0, 0, 0, 1, 1/5],
        [0, 0, 0, 0, 0, 0, 0, 1]        
    ])

    # Define an evaluation matrix (example data)
    eval_mat = np.array([
        [0.8, 0.2, 0.5],
        [0.6, 0.7, 0.3]
    ])

    eval_mat = np.array([
    [0.30, 0.03, 0.20, 0.55, 0.00, 0.48, 0.33, 0.46],
    [0.00, 0.36, 0.20, 0.08, 0.00, 0.00, 0.22, 0.24],
    [0.00, 0.00, 0.20, 0.16, 0.09, 0.00, 0.02, 0.30],
    [0.31, 0.14, 0.20, 0.16, 0.91, 0.48, 0.29, 0.00],
    [0.38, 0.47, 0.20, 0.06, 0.00, 0.04, 0.14, 0.00],
    ])

    # Instantiate the AHP_FuzzyAHP class
    ahp_fuzzy = AHP_FuzzyAHP()

    # Calculate weights using AHP and Fuzzy AHP methods
    weights_ahp, weights_fuzzy_ahp, final_scores = ahp_fuzzy.calculate_weights(comp_mat, eval_mat)

    print("AHP Weights:", weights_ahp)
    print("Fuzzy AHP Weights:", weights_fuzzy_ahp)
    print("Final Scores:", final_scores)

    # Plot the fuzzy triangular number distribution
    ahp_fuzzy.plot_fuzzy_tfn()