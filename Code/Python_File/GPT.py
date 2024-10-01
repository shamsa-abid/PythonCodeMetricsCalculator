# -*- coding: utf-8 -*-
"""ChatGPT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y1QzjPbIjhwdHgUBAkGM192b_8AAfFxw

# **Step 1: Libraries Import and Google Drive Mount**

This is where all the libraires of the code are imported. It is important to run this cell before moving to the next one.
"""

!pip install datasets
!pip install pandas prettytable
!pip install radon
!pip install bandit
!pip install pylint
!pip install autopep8
!pip install complexipy
!pip install openai==0.28
import time
import ast
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
import openai
from numpy.core.defchararray import strip

"""# **Step 2: Folder Creation**"""

def createFolder(completePath):

  os.makedirs(completePath, exist_ok=True)

  print(f"Folder created at: {completePath}")

basePath = 'sample_data/GPT_4_Improved_Prompt'
folderName = 'Dataset'
reportFolderName = 'CSV_Reports'
reportFileCommonName = ''

"""# **Step 3: Loading HumanEval Dataset**"""

dataset = load_dataset("openai/openai_humaneval")

# Convert the dataset to a pandas DataFrame
df = pd.DataFrame(dataset['test'])

# Select the desired columns
columns = ['task_id', 'prompt', 'canonical_solution', 'test', 'entry_point']
df = df[columns]
df['task_id'] = df['task_id'].str.replace('HumanEval/', reportFileCommonName)
df = df.set_index('task_id')
# Convert DataFrame to PrettyTable
table = PrettyTable()

# Set the field names (column names)
table.field_names = df.columns.tolist()

# Add rows to the table
for index, row in df.iterrows():
    table.add_row(row.tolist())


# Print the PrettyTable
print(table)

"""# **Step 4: Prompt and Code Generation from ChatGPT**"""

simplePrompt = """
For given function definition and docstring < {input} > provide the code solution.

Output Format: <code>
"""

instructionTonePrompt = """
For given function definition and docstring < {input} >, your task is to provide the code solution and ensure that your completed code passes the given test case < {testCase} >.

• Provide only the function implementation (no test cases, comments, or any extra code).
• Do not change the function name in the function definition or argument types and names
• Do not change the argument types and names in the function definition
• Identify any external module dependencies and import them before the function definition.
• There should be no nested functions in your code. All helper functions should be top-level, not defined within other functions.
• Do not use undefined functions in your code.
• Make sure there are no syntax or semantic errors in your code

Output Format: <code>
"""

improvedPrompt = """
Here is a query < {input} > and a human-written solution < {solution} >. Your task is to provide a better and innovative code solution than the human-written solution by making your code more optimized, readable, and safe, while reducing complexity. The code must pass the provided test cases < {testCase} >. Follow the guidelines below:

• Provide only the function implementation (no test cases, comments, or any extra code).
• Do not change the function name in the function definition or argument types and names
• Do not change the argument types and names in the function definition
• Identify any external module dependencies and import them before the function definition.
• There should be no nested functions in your code. All helper functions should be top-level, not defined within other functions.
• Do not use undefined functions in your code.
• Make sure there are no syntax or semantic errors in your code
• Ensure error handling is incorporated if applicable to avoid runtime failures.
• Focus on improving performance and code clarity.
• Maintain or improve safety and readability in the solution.

Output format: <code>

"""

openai.api_key = ""
GPTCode = pd.DataFrame(columns=["task_id", "canonical_solution"])
improvedGPTCode = pd.DataFrame(columns=["task_id", "canonical_solution"])


def getOutputFromGPT(query):
  response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      # {"role": "system", "content": "You are a helpful assistant that performs semantic code clone detection."},
      {"role": "user", "content": query}
      # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
      # {"role": "user", "content": "Where was it played?"}
    ]
  )

  output = response["choices"][0]["message"]["content"]
  # print('hello')
  # print(response)


  return strip(output)


def writeGPTCodeInDataFrame(choice):
  #choice 1: Simple Prompts; choice 2: Improved Prompts
  for i in range (len(df)):
    query = None
    if(choice == 1 or choice == 2):
      GPTCode.at[i,"task_id"] = i
      if(choice == 1):
        query = simplePrompt.format(
            input = df.loc[str(i),"prompt"],
        )
        print("simple prompt # " + str(i))
      else:
        query = instructionTonePrompt.format(
            input = df.loc[str(i),"prompt"],
            testCase = df.loc[str(i), "test"]
        )
        print("instruction tone prompt # " + str(i))
      output = getOutputFromGPT(query)
      time.sleep(2)
      GPTCode.at[i,"canonical_solution"] = output
    else:
      improvedGPTCode.at[i,"task_id"] = i
      query = improvedPrompt.format(
          input = df.loc[str(i),"prompt"],
          testCase = df.loc[str(i), "test"],
          solution = df.loc[str(i), "canonical_solution"]
      )
      print("improved prompt # " + str(i))
      output = getOutputFromGPT(query)
      improvedGPTCode.at[i,"canonical_solution"] = output
      time.sleep(2)
  table = PrettyTable()

  # Set the field names (column names)
  table.field_names = GPTCode.columns.tolist() if len(GPTCode) > 0 else improvedGPTCode.columns.tolist()

  # Add rows to the table
  for index, row in GPTCode.iterrows():
      table.add_row(row.tolist())

  print(table)
  print(len(GPTCode))


# writeGPTCodeInDataFrame(2)

"""# **Step 5: Writing Code in File**"""

def preprocessCode(code):
    """Remove markdown-like annotations from the code."""
    # Remove markdown syntax ```python and ```
    return re.sub(r'```[a-zA-Z]*', '', code)

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
    print(code)
    # Remove a specific number of spaces from the beginning of each line
    lines = code.split('\n')
    adjustedLines = [line[numSpaces:] if line.startswith(' ' * numSpaces) else line for line in lines]
    return '\n'.join(adjustedLines)

def removeLinesContaining(text, code):
    # Remove lines containing specific text
    lines = code.split('\n')
    filteredLines = [line for line in lines if text not in line]
    return '\n'.join(filteredLines)

def writeCodeInFile(basePath, folderName,choice):
    completePath = os.path.join(basePath, folderName)
    reportPath = os.path.join(basePath,reportFolderName)
    createFolder(completePath)
    createFolder(reportPath)
    length = len(GPTCode) if len(GPTCode) > 0 else len(improvedGPTCode)
    for i in range(length):
        fileName = reportFileCommonName + str(i) + '.py'
        filePath = os.path.join(completePath, fileName)

        # Extract and clean solution
        if(choice == 1 or choice == 2):
          solution = preprocessCode(str(GPTCode.loc[i, 'canonical_solution']))
        else:
          solution = preprocessCode(str(improvedGPTCode.loc[i, 'canonical_solution']))

        # solution = removeLeadingSpaces(solution, 2)

        # Write the function definition and solution to the file
        with open(filePath, 'w') as file:
            file.write(solution)
    print(f"File created and content written to: {completePath}")

    formatDirectory(completePath)

# Example usage

"""# **Step 6: Running Bandit**"""

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

"""# **Step 7: Running Pylint**"""

def runPylint(folderName):
  completePath = os.path.join(basePath, folderName)
  completePath = os.path.join(completePath,'*.py')
  reportPath = os.path.join(basePath, reportFolderName)
  jsonReport = os.path.join(reportPath,reportFileCommonName + 'pylint.json')
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

"""# **Step 8: Run Complexipy**"""

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

"""# **Step 9: Run Radon**"""

def runRadon(folderName):
  completePath = os.path.join(basePath, folderName)
  reportPath = os.path.join(basePath, reportFolderName)
  radonReport = os.path.join(reportPath, reportFileCommonName +'radon.csv')
  # Prepare the CSV file
  with open(radonReport, 'w', newline='') as csvfile:
      csvwriter = csv.writer(csvfile)
      # Write header
      csvwriter.writerow([
          'File Name', 'LOC', 'LLOC', 'SLOC', 'Comments',
          'Cyclomatic Complexity', 'Maintainability Index',
          'h1', 'h2','h', 'N1', 'N2', 'N',
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

"""# **Step 10: Function Call**"""

# writeGPTCodeInDataFrame(3)
# writeCodeInFile(basePath, folderName,3)
runRadon(folderName)
runComplexipy(folderName)
runPylint(folderName)
runBandit(folderName)

"""# **Step 11: Download Folder to ZIP (Optional)**"""

import shutil
from google.colab import files


# Specify the folder you want to zip and the output zip file name
folder_path = 'sample_data/GPT_4_Improved_Prompt'

# Create a zip file from the folder
shutil.make_archive('sample_data/GPT_4_Improved_Prompt', 'zip', folder_path)
files.download('sample_data/GPT_4_Improved_Prompt')