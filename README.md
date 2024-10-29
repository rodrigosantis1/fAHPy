# AHP Fuzzy Library

A library for performing AHP and Fuzzy AHP calculations and plotting triangular fuzzy number distributions.

## Installation

You can install the library using:

```bash
pip install git+https://github.com/username/ahp_fuzzy_lib.git
```

## Usage
``` python
from ahp_fuzzy_lib import AHP_FuzzyAHP

# Initialize the AHP_FuzzyAHP object
ahp_fuzzy = AHP_FuzzyAHP()

# Define a comparison matrix and evaluation matrix
comp_mat = [[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]]
eval_mat = [[0.8, 0.2, 0.5], [0.6, 0.7, 0.3]]

# Calculate weights and scores
weights_ahp, weights_fuzzy_ahp, final_scores = ahp_fuzzy.calculate_weights(comp_mat, eval_mat)

# Plot fuzzy triangular number distribution
ahp_fuzzy.plot_fuzzy_tfn()
```

## Citation

If you use this library for research or academic purposes, please cite the following reference:

de Santis, R. B., Golliat, L., & de Aguiar, E. P. (2017). Multi-criteria supplier selection using fuzzy analytic hierarchy process: case study from a Brazilian railway operator. Brazilian Journal of Operations & Production Management, 14(3), 428-437.

```
@article{de2017multi,
  title={Multi-criteria supplier selection using fuzzy analytic hierarchy process: case study from a Brazilian railway operator},
  author={de Santis, Rodrigo Barbosa and Golliat, Leonardo and de Aguiar, Eduardo Pestana},
  journal={Brazilian Journal of Operations \& Production Management},
  volume={14},
  number={3},
  pages={428--437},
  year={2017}
}
```

