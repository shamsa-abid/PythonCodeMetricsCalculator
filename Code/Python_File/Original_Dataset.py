# -*- coding: utf-8 -*-
"""Original Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fkdzd6aYzSA08AOsSxUE-yKKjp9jqCN1

# **Step 0: Libraries Import and Google Drive Mount**

This is where all the libraires of the code are imported. It is important to run this cell before moving to the next one.
"""

!pip install datasets
!pip install pandas prettytable
!pip install radon
!pip install bandit
!pip install pylint
!pip install autopep8
!pip install complexipy
import csv
from google.colab import drive
import os
import ast
import re
import autopep8
import pandas as pd
from datasets import load_dataset
from prettytable import PrettyTable
import subprocess
from radon.complexity import cc_rank, cc_visit
from radon.metrics import h_visit, mi_visit
from radon.raw import analyze

"""# **Step 2: Folder Creation**"""

def createFolder(completePath):

  os.makedirs(completePath, exist_ok=True)

  print(f"Folder created at: {completePath}")

basePath = 'sample_data/Human_Eval_Dataset'
folderName = 'Dataset'
reportFolderName = 'CSV_Reports'
reportFileCommonName = 'human_eval_'

"""# **Step 3: Loading HumanEval Dataset**"""

dataset = load_dataset("openai/openai_humaneval")

# Convert the dataset to a pandas DataFrame
df = pd.DataFrame(dataset['test'])

# Select the desired columns
columns = ['task_id', 'prompt', 'canonical_solution', 'test', 'entry_point']
df = df[columns]

# Convert DataFrame to PrettyTable
table = PrettyTable()

# Set the field names (column names)
table.field_names = df.columns.tolist()

# Add rows to the table
for index, row in df.iterrows():
    table.add_row(row.tolist())

# Print the PrettyTable
print(df.loc[0, 'task_id'])

"""# **Step 4: Writing Code in File**"""

def formatCode(filePath):
    with open(filePath, 'r') as file:
        code = file.read()
    formattedCode = autopep8.fix_code(code)
    with open(filePath, 'w') as file:
        file.write(formattedCode)

def formatDirectory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                formatCode(os.path.join(root, file))

def removeComments(code):
    # Remove multiline comments (''' or """ enclosed comments)
    code = re.sub(r'\'\'\'(.*?)\'\'\'|"""(.*?)"""', '', code, flags=re.DOTALL)
    # Remove single-line comments (lines starting with #)
    codeLines = code.split('\n')
    codeWithoutComments = '\n'.join(line for line in codeLines if not line.strip().startswith('#'))
    return codeWithoutComments

def removeLeadingSpaces(code, numSpaces):
    # Remove a specific number of spaces from the beginning of each line
    lines = code.split('\n')
    adjustedLines = [line[numSpaces:] if line.startswith(' ' * numSpaces) else line for line in lines]
    return '\n'.join(adjustedLines)

def removeLinesContaining(text, code):
    # Remove lines containing specific text
    lines = code.split('\n')
    filteredLines = [line for line in lines if text not in line]
    return '\n'.join(filteredLines)

def writeCodeInFile(basePath, folderName):
    completePath = os.path.join(basePath, folderName)
    reportPath = os.path.join(basePath,reportFolderName)
    createFolder(completePath)
    createFolder(reportPath)

    for i in range(len(df)):
        fileName = reportFileCommonName + str(i) + '.py'
        filePath = os.path.join(completePath, fileName)

        # Extract and clean function definition
        functionDefinition = removeComments(df.loc[i, 'prompt']).strip()
        functionDefinition = removeLeadingSpaces(functionDefinition, 2)
        functionDefinition = removeLinesContaining('FIX = ', functionDefinition)  # Remove lines containing 'FIX='

        # Extract and clean solution
        solution = df.loc[i, 'canonical_solution']
        solution = removeLeadingSpaces(solution, 2)

        # Write the function definition and solution to the file
        with open(filePath, 'w') as file:
            file.write(functionDefinition + '\n')
            file.write(solution)

    print(f"File created and content written to: {completePath}")

    formatDirectory(completePath)

# Example usage

"""# **Step 5: Running Bandit**"""

def runBandit(folderName):
  completePath = os.path.join(basePath, folderName)
  reportPath = os.path.join(basePath, reportFolderName)
  banditReport = os.path.join(reportPath, reportFileCommonName + 'bandit.csv')

  # Ensure the report directory exists
  os.makedirs(reportPath, exist_ok=True)

  # Define the command
  command = ['bandit', '-r', completePath, '-f', 'csv', '-vv', '-o', banditReport]

  # Run the command
  try:
      result = subprocess.run(command, check=False, text=True, capture_output=True)
      print("Bandit Command executed successfully.")
  except subprocess.CalledProcessError as e:
      print("Error running command:", e)

# !bandit -r sample_data/Original -f csv -o sample_data/CSVReports/banditResult.csv

"""# **Step 6: Running Pylint**"""

def runPylint(folderName):
  completePath = os.path.join(basePath, folderName)
  completePath = os.path.join(completePath,'*.py')
  reportPath = os.path.join(basePath, reportFolderName)
  jsonReport = os.path.join(reportPath,'human_eval_pylint.json')
  pylintReport = os.path.join(reportPath, reportFileCommonName + 'pylint.csv')

  command = [
    'pylint',
    completePath,
    '--output-format=json:'+ jsonReport
  ]

  # Run the command
  try:
      result = subprocess.run(command, check=False, text=True, capture_output=True)
      print("Pylint Command executed successfully.")
  except subprocess.CalledProcessError as e:
      print("An error occurred while running the command.")
      print("Error message:", e.stderr)
      print("Return code:", e.returncode)
      print("Output:", e.output)
  # Load the JSON file
  df = pd.read_json(jsonReport)

  columns = ['module'] + [col for col in df.columns if col != 'module']
  df = df[columns]

  # Convert the DataFrame to a CSV file
  df.to_csv(pylintReport, index=False)

# !pylint sample_data/Original/*.py --output-format=json:sample_data/CSVReports/pylint_output.json

"""# **Step 7: Run Complexipy**"""

# !pip install complexipy
# !complexipy sample_data/Original | tee sample_data/Human_Eval_Dataset_CSV/human_eval_complexipy.txt

def runComplexipy(folderName):
  completePath = os.path.join(basePath, folderName)
  reportPath = os.path.join(basePath, reportFolderName)
  txtReport = os.path.join(reportPath,reportFileCommonName + 'complexipy.txt')
  complexipyReport = os.path.join(reportPath, reportFileCommonName +'complexipy.csv')

  command = "complexipy " + completePath + " | tee " + txtReport

  # Run the command using subprocess with shell=True
  process = subprocess.run(command, shell=True, stderr=subprocess.PIPE, text=True)

  # Check if the process encountered any errors
  if process.returncode == 0:
      print("Complexipy Command executed successfully.")
  else:
      print(f"An error occurred: {process.stderr}")
  # Initialize an empty list to store rows
  rows = []

  # Read the text file and parse it
  with open(txtReport, 'r') as file:
      lines = file.readlines()
      start_collecting = False
      for line in lines:
          line = line.strip()
          if line.startswith('┏'):
              start_collecting = True
              continue
          if line.startswith('┗'):
              break
          if start_collecting and line.startswith('│'):
              # Split line into columns
              columns = [col.strip() for col in line.split('│')[1:-1]]
              rows.append(columns)

  # Write the rows to a CSV file
  with open(complexipyReport, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      # Writing the header
      writer.writerow(['Path', 'File', 'Function', 'Complexity'])
      # Writing the data rows
      writer.writerows(rows)

  print(f"CSV file has been saved to {complexipyReport}")

"""# **Step 8: Run Radon**"""

def get_radon_metrics(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

        # Calculate metrics
        raw_metrics = analyze(code)
        complexity_metrics = cc_visit(code)
        maintainability_index = mi_visit(code, True)
        halstead_metrics = h_visit(code)

        return raw_metrics, complexity_metrics, maintainability_index, halstead_metrics


def runRadon(folderName):
  completePath = os.path.join(basePath, folderName)
  reportPath = os.path.join(basePath, reportFolderName)
  radonReport = os.path.join(reportPath, reportFileCommonName +'radon.csv')
  # Prepare the CSV file
  with open(radonReport, 'w', newline='') as csvfile:
      csvwriter = csv.writer(csvfile)
      # Write header
      csvwriter.writerow([
          'File Name', 'LOC', 'LLOC', 'SLOC', 'Comments', 'Multi',
          'Cyclomatic Complexity', 'Maintainability Index',
          'h1', 'h2','h' 'N1', 'N2', 'N',
          'Vocabulary', 'Volume', 'Difficulty',
          'Effort', 'Bugs', 'Time'
      ])

      # Process each .py file in the folder
      for file_name in os.listdir(completePath):
          if file_name.endswith('.py'):
              file_path = os.path.join(completePath, file_name)

              # Get Radon metrics
              raw_metrics, complexity_metrics, maintainability_index, halstead_metrics = get_radon_metrics(file_path)

              # Calculate total and average complexity
              total_complexity = sum(block.complexity for block in complexity_metrics)

              # Write metrics to CSV
              csvwriter.writerow([
                  file_name,
                  raw_metrics.loc,
                  raw_metrics.lloc,
                  raw_metrics.sloc,
                  raw_metrics.comments,
                  total_complexity,
                  maintainability_index,
                  halstead_metrics.total.h1,  # Number of distinct operators
                  halstead_metrics.total.h2,  # Number of distinct operands
                  halstead_metrics.total.h1 + halstead_metrics.total.h2,
                  halstead_metrics.total.N1,  # Total number of operators
                  halstead_metrics.total.N2,  # Total number of operands
                  halstead_metrics.total.N1 +halstead_metrics.total.N2,
                  halstead_metrics.total.vocabulary,  # Halstead Vocabulary
                  halstead_metrics.total.volume,  # Halstead Volume
                  halstead_metrics.total.difficulty,  # Halstead Difficulty
                  halstead_metrics.total.effort,  # Halstead Effort
                  halstead_metrics.total.bugs,  # Halstead Estimated Bugs
                  halstead_metrics.total.time  # Halstead Time to Implement
              ])

  print(f'All Radon metrics have been saved to {radonReport}')

"""# **Step 9: Function Call**"""

writeCodeInFile(basePath, folderName)
runRadon(folderName)
runComplexipy(folderName)
runPylint(folderName)
runBandit(folderName)

"""# **Step 10: Download Folder to ZIP (Optional)**"""

import shutil
from google.colab import files


# Specify the folder you want to zip and the output zip file name
folder_path = 'sample_data/Human_Eval_Dataset'

# Create a zip file from the folder
shutil.make_archive('sample_data/Human_Eval_Dataset', 'zip', folder_path)
files.download('sample_data/Human_Eval_Dataset')