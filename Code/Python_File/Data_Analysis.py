import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import textwrap

basePath = '../../Data'
# List of CSV file paths (update with your actual file paths)
def getCsvFile(choice):
    if choice == 1:
        return [
        'human_eval_radon.csv',
        'gpt_3.5_turbo_simple_prompt_radon.csv',
        'gpt_3.5_turbo_instruction_tone_prompt_radon.csv',
        'gpt_3.5_turbo_enhanced_prompt_radon.csv',
        'gpt_4_simple_prompt_radon.csv',
        'gpt_4_instruction_tone_prompt_radon.csv',
        'gpt_4_enhanced_prompt_radon.csv'
        ]
    elif choice == 2:
        return [
            'human_eval_complexipy.csv',
            'gpt_3.5_turbo_simple_prompt_complexipy.csv',
            'gpt_3.5_turbo_instruction_tone_prompt_complexipy.csv',
            'gpt_3.5_turbo_enhanced_prompt_complexipy.csv',
            'gpt_4_simple_prompt_complexipy.csv',
            'gpt_4_instruction_tone_prompt_complexipy.csv',
            'gpt_4_enhanced_prompt_complexipy.csv'
        ]
    elif choice == 3:
        return [
            'human_eval_pylint.csv',
            'gpt_3.5_turbo_simple_prompt_pylint.csv',
            'gpt_3.5_turbo_instruction_tone_prompt_pylint.csv',
            'gpt_3.5_turbo_enhanced_prompt_pylint.csv',
            'gpt_4_simple_prompt_pylint.csv',
            'gpt_4_instruction_tone_prompt_pylint.csv',
            'gpt_4_enhanced_prompt_pylint.csv'
        ]
    elif choice == 4:
        return [
            'human_eval_test_case_check.csv',
            'gpt_3.5_turbo_simple_prompt_test_case_check.csv',
            'gpt_3.5_turbo_instruction_tone_prompt_test_case_check.csv',
            'gpt_3.5_turbo_enhanced_prompt_test_case_check.csv',
            'gpt_4_simple_prompt_test_case_check.csv',
            'gpt_4_instruction_tone_prompt_test_case_check.csv',
            'gpt_4_enhanced_prompt_test_case_check.csv'
        ]
    elif choice == 5:
        return [
            'human_eval_bandit.csv',
            'gpt_3.5_turbo_simple_prompt_bandit.csv',
            'gpt_3.5_turbo_instruction_tone_prompt_bandit.csv',
            'gpt_3.5_turbo_enhanced_prompt_bandit.csv',
            'gpt_4_simple_prompt_bandit.csv',
            'gpt_4_instruction_tone_prompt_bandit.csv',
            'gpt_4_enhanced_prompt_bandit.csv'
        ]

directories = [
    'Human_Eval_Dataset',
    'GPT_3.5_Turbo_Simple_Prompt',
    'GPT_3.5_Turbo_Instruction_Tone_Prompt',
    'GPT_3.5_Turbo_Enhanced_Prompt',
    'GPT_4_Simple_Prompt',
    'GPT_4_Instruction_Tone_Prompt',
    'GPT_4_Enhanced_Prompt'
]
labels = [
    'HE',
    'GPT 3.5 S',
    'GPT 3.5 I',
    'GPT 3.5 E',
    'GPT 4 S',
    'GPT 4 I',
    'GPT 4 E'
]
#################### Box Plots ####################
#################### Tools: Radon, Complexipy ####################

# List to store the volume data for each CSV
# data = []
# j = 0
# title = "LOC"
# # Loop through the CSVs and extract the Volume
# csv_files = getCsvFile(1)
# for file in csv_files:
#     df = pd.read_csv(os.path.join(basePath, directories[j], 'CSV_Reports', file))
#     j += 1
#     data.append(df[title].values)  # Store the Volume values
#
# # Create a box plot using matplotlib
# wrapped_labels = [textwrap.fill(label, width=5) for label in labels]  # Adjust width as needed
#
# plt.figure(figsize=(10, 6))
# plt.boxplot(data, vert=True)  # Vertical box plot
# plt.ylabel(title, fontsize=20)
# plt.xticks(range(1, len(csv_files) + 1), wrapped_labels, fontsize=20)
# plt.yticks(fontsize=18)
# plt.grid(axis='y')  # Optional: add horizontal grid lines for better readability
# plt.tight_layout()
# plt.show()
#################### Box Plots Ends ####################

#################### Bar Charts ####################
#################### Tools: Pylint and For Test case ####################
# frequencyObject = {}

# Pylint
# types = ['error','refactor','warning', 'convention']
# def getType(types, val):
#     for i in range (len(types)):
#         if val == types[i]:
#             return types[i]
# def countFrequency(label,df):
#     if label not in frequencyObject:
#         frequencyObject[label] = {}
#     for i in range (len(types)):
#         frequencyObject[label][types[i]] = 0
#     for i in range (len(df)):
#         frequencyObject[label][getType(types,df.loc[i,'type'])] += 1
#
#
# csv_files = getCsvFile(3)
# j = 0
# for file in csv_files:
#     df = pd.read_csv(os.path.join(basePath, directories[j], 'CSV_Reports', file))
#     countFrequency(labels[j], df)
#     j += 1
#

#test case
# types = ['passed','runtime error','assertion error']
# csv_files = getCsvFile(4)
# def getTestCaseFrequency(label,df):
#     if label not in frequencyObject:
#         frequencyObject[label] = {
#             'passed':0,
#             'runtime error':0,
#             'assertion error':0
#         }
#
#     for i in range (len(df)):
#         if df.loc[i,'Test Case Passed'] == True:
#             frequencyObject[label]['passed'] += 1
#         elif df.loc[i,'Test Case Passed'] == False and df.loc[i,'Error Type'] == "Assertion Error":
#             frequencyObject[label]['assertion error'] += 1
#         else:
#             frequencyObject[label]['runtime error'] += 1
#
# j = 0
# for file in csv_files:
#     df = pd.read_csv(os.path.join(basePath, directories[j], 'CSV_Reports', file))
#     getTestCaseFrequency(labels[j], df)
#     j += 1
#
#
# # For Pylint and Test Case
# def plot_frequency(frequencyObject):
#     # Get dataset labels and types (convention, warning, error)
#     labels = list(frequencyObject.keys())
#     types = list(next(iter(frequencyObject.values())).keys())
#
#     # Extract counts for each type across all datasets
#     type_counts = {t: [frequencyObject[label][t] for label in labels] for t in types}
#
#     x = np.arange(len(labels))  # Label locations (datasets)
#     width = 0.2  # Width of the bars
#
#     # Create figure and axis with larger dimensions
#     fig, ax = plt.subplots(figsize=(12, 6))
#
#     # Plot bars for each type (convention, warning, error)
#     bars_list = []
#     for i, t in enumerate(types):
#         bars = ax.bar(x + i * width, type_counts[t], width, label=t)
#         bars_list.append(bars)
#
#     # Add labels, title, and x-axis ticks
#     ax.set_ylabel('Frequency')
#
#     # Ensure x-tick labels don't overlap and set proper alignment
#     ax.set_xticks(x + width / 2)
#     ax.set_xticklabels(labels,rotation = 90, ha="right")  # Rotate for better readability
#
#     # Move the legend outside the plot
#     ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
#
#     # Add labels on top of the bars
#     def add_labels(bars):
#         for bar in bars:
#             height = bar.get_height()
#             # Calculate a dynamic offset based on the bar height
#             offset = 0.02 * height  # 2% of the height as an offset
#             ax.annotate(f'{height}',
#                         xy=(bar.get_x() + bar.get_width() / 2, height),
#                         xytext=(0, offset),  # Use dynamic offset
#                         textcoords="offset points",
#                         ha='center', va='bottom')
#
#     # Add labels for each group of bars
#     for bars in bars_list:
#         add_labels(bars)
#
#     # Adjust the y-axis limit to allow for the height of the labels
#     max_count = max([max(counts) for counts in type_counts.values()])  # Find the maximum height
#     ax.set_ylim(0, max_count * 1.15)  # Extend y-limit to avoid clipping labels (15% above max)
#
#     # Adjust the layout to prevent clipping of tick-labels and ensure legend fits
#     plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjusting right margin for legend space
#     plt.show()

# Call the function with your frequencyObject
# plot_frequency(frequencyObject)

#################### Bar Charts End ####################

#################### Single Bar Chart ####################
#################### Tools: Bandit ####################
# For Bandit
# csv_files = getCsvFile(5)
# def getBanditFrequency(label,df):
#     if label not in frequencyObject:
#         frequencyObject[label] = len(df)
#
# j = 0
# for file in csv_files:
#     df = pd.read_csv(os.path.join(basePath, directories[j], 'CSV_Reports', file))
#     getBanditFrequency(labels[j], df)
#     j += 1
#
#
# fig = plt.figure(figsize = (10, 5))
# array = []
# for object in frequencyObject:
#     array.append(object)
# # creating the bar plot
# plt.bar(labels,array , color ='maroon',
#         width = 0.4)
#
# plt.ylabel("Frequency")
# plt.show()
#################### Single Bar Chart Ends ####################

#################### Comparison Analysis with Human Eval ####################

humanEvalRadon = pd.read_csv(os.path.join(basePath, "Human_Eval_Dataset", 'CSV_Reports', 'human_eval_radon.csv'))
humanEvalComplexipy = pd.read_csv(os.path.join(basePath, "Human_Eval_Dataset", 'CSV_Reports', 'human_eval_complexipy.csv'))

targetRadon = pd.read_csv(os.path.join(basePath, directories[6], 'CSV_Reports', 'gpt_4_enhanced_prompt_radon.csv'))
targetComplexipy = pd.read_csv(os.path.join(basePath, directories[6], 'CSV_Reports', 'gpt_4_enhanced_prompt_complexipy.csv'))

targetTestCaseCheck = pd.read_csv(os.path.join(basePath, directories[6], 'CSV_Reports', 'gpt_4_enhanced_prompt_test_case_check.csv'))

targetRadon.set_index('File Name', inplace = True)
targetComplexipy.set_index('File', inplace = True)
targetTestCaseCheck.set_index('File Name', inplace = True)

humanEvalRadon.set_index('File Name', inplace = True)
humanEvalComplexipy.set_index('File', inplace = True)

print(targetTestCaseCheck)

loc = CC = cogC = vocab = MI = testCase = 0
for i in range (len(targetTestCaseCheck)):
    if targetTestCaseCheck.loc[i]['Test Case Passed']:
        testCase += 1
        index = str(i) + '.py'

        if(targetRadon.loc[index]['LOC'] < humanEvalRadon.loc[index]['LOC']):
            loc += 1
        if (targetRadon.loc[index]['Cyclomatic Complexity'] < humanEvalRadon.loc[index]['Cyclomatic Complexity']):
            CC += 1
        if (targetRadon.loc[index]['Vocabulary'] < humanEvalRadon.loc[index]['Vocabulary']):
            vocab += 1
        if (targetRadon.loc[index]['Maintainability Index'] > humanEvalRadon.loc[index]['Maintainability Index']):
            MI += 1
        temp = humanEvalComplexipy.loc[index]['Complexity']
        if isinstance(temp, pd.Series) and len(temp) > 1:
            temp = temp.sum()

        target_complexity = targetComplexipy.loc[index]['Complexity']

        if isinstance(target_complexity, pd.Series) and len(target_complexity) > 1:
            target_complexity = target_complexity.sum()
        if target_complexity < temp:
            cogC += 1

print("Test Case " ,testCase)
print("LOC ", (loc/164) * 100)
print("CC ",(CC/164) * 100)
print("Vocab", (vocab/164) * 100)
print("MI ", (MI/164) * 100)
print("CogC ", (cogC/164) * 100)

#################### Comparison Analysis with Huaman Eval Ends ####################