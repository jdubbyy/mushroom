# Mushroom Classification Analysis

This project demonstrates an understanding of information gain (entropy reduction) as a measure of feature importance in classification problems. It contains both a manual implementation using pandas and numpy, as well as a scikit-learn implementation for comparison and verification.

## Project Description

This repository contains an analysis of the UCI Mushroom Dataset to determine which mushroom attributes provide the most information gain for classifying mushrooms as edible or poisonous. The project includes:

1. `MushroomSK.ipynb`: A Jupyter notebook that calculates information gain for each attribute using scikit-learn's mutual_info_classif function.
2. `Mushroom.ipynb`: A Jupyter notebook that manually calculates information gain for each attribute using pandas and numpy, and includes visualizations of entropy vs. proportion for attributes with maximum, median, and minimum information gain.
3. `mushroom_module.py`: A module containing reusable code for the analysis.
4. `UCIrvine_Mushroom_Data/`: A directory containing the UCI Mushroom Dataset.

## Requirements

This project uses the following libraries and versions:
- Python 3.12.9
- pandas 2.2.3 
- numpy 2.2.4
- matplotlib 3.10
- scikit-learn 1.6.1
- jupyter 1.1.1

## How to Use

1. First, run `MushroomSK.ipynb` to see how information gain is calculated for each attribute using scikit-learn.
2. Then, run `Mushroom.ipynb` to see the same values derived through manual calculations using only pandas and numpy.
3. The latter part of `Mushroom.ipynb` contains visualizations showing entropy vs. proportion for attribute values for:
   - The attribute with maximum information gain
   - The attribute with median information gain
   - The attribute with minimum information gain

## Key Findings

The analysis reveals that:

- **Odor** is the best determinant of an edible mushroom, with an information gain of 0.91
- The remaining variables drop off steeply, with **Spore Print Color** being the second best attribute at 0.48 information gain
- **Veil Type** is the worst attribute, providing no informative value over the parent set

## Next Steps

Future work for this project includes:
- Building a decision tree with more layers of nodes
- Exploring more complex feature interactions
- Evaluating how combinations of attributes might improve classification accuracy

## Dataset

The UCI Mushroom Dataset contains descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family. Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended (the latter class was combined with the poisonous one).

The dataset includes 22 attributes such as cap shape, cap surface, odor, gill size, etc., and contains 8,124 instances.

## Disclaimer

**IMPORTANT:** No one should use the information in this data science experiment to determine safety of mushrooms in real life. This is only an exercise to demonstrate understanding of information gain and related concepts. Mushroom identification for consumption purposes should only be done by trained experts with proper field guides and tools.

## Attribution

This project uses the UCI Machine Learning Repository Mushroom Dataset:
- Source: UCI Machine Learning Repository
- Original Dataset: https://archive.ics.uci.edu/dataset/73/mushroom
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)
- Original Source: The Audubon Society Field Guide to North American Mushrooms (1981)

## License

This project is shared under the MIT License.

## Contact

For questions or collaboration opportunities, please contact Josh Wang at josh.wang@utexas.edu.
