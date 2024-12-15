# Python Code Metrics Calculator

## Overview

This repository, **Python Code Metrics Calculator**, was developed as part of a research project focusing on evaluating and analyzing the quality of Python code snippets generated under various conditions. The project involved calculating key metrics that assess code complexity, maintainability, and security, among others, using tools such as **Radon**, **Pylint**, **Bandit**, and **Complexipy**. The code, data and results was uploaded for the research work from paper **Can LLMs Generate Higher Quality Code than Humans? An Empirical Study.**

## Key Features

- **Static Code Analysis**: Extracts metrics such as cyclomatic complexity, maintainability index, and Halstead metrics.
- **Security Checks**: Identifies potential vulnerabilities in Python code using Bandit.
- **Formatting and Linting**: Evaluates code style and adherence to PEP8 standards with Pylint.
- **Integration with CSV**: Outputs results in CSV format for easy post-processing and analysis.
- **Customizable Workflows**: Supports modular extensions for specific research requirements.

## Research Context

This repository was created to automate the evaluation of Python code quality as part of a research study. The study involved:

1. Generating Python code snippets using GPT-based models.
2. Measuring various quality metrics for each snippet.
3. Analyzing and comparing the metrics to draw insights into code quality trends under different prompt designs and configurations.

The metrics and insights obtained were instrumental in assessing the effectiveness of different approaches in generating high-quality Python code.

## Requirements

To use the repository, ensure the following dependencies are installed:

- Python 3.8 or higher
- Radon
- Pylint
- Bandit
- Complexipy
- pandas

## Usage

1. Clone the repository:

```bash
git clone https://github.com/shamsa-abid/PythonCodeMetricsCalculator.git
```

2. Add the Python files or folder to be analyzed in the specified directory.

3. Run the script present in the `Code/` folder to calculate metrics:

4. The results will be saved in a CSV file in the output folder.

## Folder Structure

- `PythonCodeMetricsCalculator/`: Root directory containing the main script and subdirectories.
  - `Code/`: Contains the automation script for code generation and data analysis.
  - `Data/`: Contains the python code snippets generated by GPT models based on different prompts and results of python code snippets prodcued by tools. The results are stored in CSV format.
  - `Results/`: The overall results of the code generated by GPT model and their representation.

## Acknowledgments

This project would not have been possible without the support of the open-source community and the tools that made automated code analysis feasible. Special thanks to the developers of Radon, Bandit, Pylint, and Complexipy.

---



