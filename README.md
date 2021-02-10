# Zindi-crop-yield-predicion

A small experiment on gradient boosting methods for wheat yield predictions (CGIAR challenge).
This is a very one-shot experimentation project.

# Setup

The project tree shoul look like

|-data/\
|-models/\
|-notebooks/
|-submissions/

The data folder must have all the data in it and the zip files already unzipped in it.

# Config

If you face some paths errors, you shoul modify the `config.py` file to match your own configuration (especially the paths)

# Usage
First run the `eda.ipynb` in the `notebooks` folder to generate the train & test .csv files (`train_sampled.csv` and `test_sampled.csv`).
Then run tne `train.ipynb` in the `notebooks` folder that generates the submission file into the submissions directory.
