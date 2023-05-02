# Pytest Example

This repo is a companion to the debugging and testing in python for LunarVim.

## Setup Virtual Environment

Use whatever virtual environment manager you want, I'll be using conda.

```sh
conda create -n pytest python -y

conda activate pytest

conda install pytest
```

## Code Explanation

Here's a brief explanation of each file and directory:

1. pytest_example/: The root directory for the project.
2. calculator/: A directory containing the Calculator class.
    - __init__.py: An empty file that tells Python that the directory should be treated as a package.
    - calculator.py: The file containing the Calculator class.
3. tests/: A directory containing the unit tests for the Calculator class.
    - __init__.py: An empty file that tells Python that the directory should be treated as a package.
    - test_calculator.py: The file containing the pytest unit tests for the Calculator class.

You can run all tests from the cli with:

```sh
pytest tests/
```
