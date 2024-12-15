We thank all three reviewers for their keen observation and insightful comments. We are eager to incorporate all valuable suggestions to refine and improve our work. In this response, we have attempted to clarify all the reviewers concerns. We begin our response by addressing common concerns first and then list responses for each individual reviewer.

# Response to Common Concerns

## Relevance to MSR

Regarding positioning the relevance of our research to MSR, it is noteworthy that we contribute datasets of code quality metrics for human-written and AI-generated code, covering key quality factors. These datasets may serve as a valuable resource for the MSR community, enabling future research in knowledge extraction, benchmarking, and model improvement. Our work may also support MSR tasks that require code datasets, such as identifying vulnerabilities, refactoring suggestions, or understanding historical code evolution patterns.
We would also like to highlight that assessing the quality of AI-generated code and its implications for developers is an emerging topic within the scope of MSR, as evidenced by recent work such as Siddiq et al. (2024) “*Quality assessment of ChatGPT-generated code and their use by developers*” presented at MSR 2024, which we cite while discussing related work.


## Statistical tests
Regarding providing statistical significance results for Figures 6-9, we now perform Friedman's Test and Wilcoxon Signed-Rank Test to evaluate statistical significance. We use Friedman’s test because it is specifically designed for comparing multiple related samples, which is the case in our study where we are evaluating multiple models (HumanEval and various AI-generated code) across different code quality metrics. Since the data are not independent - each model is tested on the same set of code problems - and the distributions may not be normal, Friedman’s test is a non-parametric method that does not require normality assumptions. It ranks the performance of each model on each metric, allowing us to assess relative differences across models in a reliable way. This makes it an appropriate choice for our analysis of the models' performance on multiple related code quality metrics.

| Metric | Friedman's Test Statistic | p-value | 
|--------|---------------------------|---------| 
| LOC | 308.88 | 1.02e-63 | 
| CC | 19.43 | 0.0035 | 
| MI | 170.60 | 3.36e-34 | 
| CogC | 99.44 | 3.28e-19 |

The results from the Friedman’s test show that the metrics (LOC, CC, MI, and CogC) exhibit statistically significant differences (p-values < 0.05 for all metrics). Specifically, LOC has an extremely small p-value (1.02e-63), indicating a very significant difference in the distributions across the models. CC also has a significant p-value (0.0035), but less extreme than LOC, suggesting a notable difference in complexity. MI and CogC show highly significant differences with p-values of 3.36e-34 and 3.28e-19, respectively, confirming that these metrics also differ significantly across the models.

We then used the Wilcoxon test for comparing LOC between HumanEval and various GPT models. It is a non-parametric test that does not assume normality in the data, which is suitable for comparing paired samples like in our study where we are comparing LOC between HumanEval and various GPT models. Since we are testing whether one distribution (e.g., HumanEval_LOC) is significantly different from another (e.g., GPT-3.5S_LOC, GPT-4S), the Wilcoxon signed-rank test allows us to assess whether these differences are statistically significant. 

| LOC Comparison | Test Statistic | p-value | 
|-------------------------------|----------------|--------------------------------| 
| HumanEval_LOC vs GPT3.5S| 502.0 | 1.420628067299295e-22 | 
| HumanEval_LOC vs GPT3.5I | 4588.5 | 0.318894564695125 | 
| HumanEval_LOC vs GPT3.5E | 3651.0 | 0.5751421274133739 | 
| HumanEval_LOC vs GPT4S | 3352.5 | 8.216095195734727e-05 | 
| HumanEval_LOC vs GPT4I | 3055.0 | 0.003502404544579744 | 
| HumanEval_LOC vs GPT4E | 2047.5 | 7.138259819360276e-07 |

The Wilcoxon test shows significant differences in LOC between HumanEval and some of the GPT-generated code. For example, GPT-3.5S and GPT-4E produce significantly different LOC than HumanEval, with p-values indicating strong evidence against the null hypothesis (p-values < 0.05). In contrast, GPT-3.5I and GPT-3.5E show no significant difference (p-values > 0.05), suggesting that their LOC values are similar to those of HumanEval code.

| CC Comparison | Test Statistic | p-value | 
|-----------------------------------------------|----------------|--------------------------------| 
| HumanEval_Cyclomatic Complexity vs GPT3.5S | 1852.0 | 0.2552544850155303 | 
| HumanEval_Cyclomatic Complexity vs GPT3.5I | 2121.0 | 0.8007871137740373 | 
| HumanEval_Cyclomatic Complexity vs GPT3.5E | 1148.0 | 0.01378374602863343 | 
| HumanEval_Cyclomatic Complexity vs GPT4S | 1343.0 | 0.12872155602923252 | 
| HumanEval_Cyclomatic Complexity vs GPT4I | 1305.0 | 0.01973004103675469 | 
| HumanEval_Cyclomatic Complexity vs GPT4E | 1875.5 | 0.00473501481561283 |

GPT-3.5E, GPT-4I, and GPT-4E all show significant differences (p-values < 0.05), indicating these models produce code with notably different Cyclomatic Complexity. The smallest p-value (0.0047) is seen for GPT-4E, suggesting it is the most distinct from HumanEval in terms of Cyclomatic Complexity, followed by GPT-4I.

| Maintainability Index Comparison                                       | Test Statistic | p-value                        |
|--------------------------------------------------|----------------|--------------------------------|
| HumanEval_Maintainability Index vs GPT3.5S    | 467.0          | 1.8811418083423235e-22         |
| HumanEval_Maintainability Index vs GPT3.5I       | 4566.0         | 0.05288720486079904            |
| HumanEval_Maintainability Index vs GPT3.5E       | 2932.0         | 3.005958655961956e-07          |
| HumanEval_Maintainability Index vs GPT4S         | 2272.0         | 1.8473281691106275e-08         |
| HumanEval_Maintainability Index vs GPT4I         | 2507.5         | 4.791099099169721e-06          |
| HumanEval_Maintainability Index vs GPT4E         | 2308.0         | 8.503161857581495e-10         |

GPT-3.5S shows a strong difference with a very low p-value (1.88e-22), indicating that its maintainability is significantly different from HumanEval. The GPT-3.5I model is almost indistinguishable from HumanEval with a p-value of 0.0529, which is close to the threshold for significance. However, all other models (GPT-3.5E, GPT-4S, GPT-4I, and GPT-4E) show highly significant differences with p-values well below 0.05, indicating that these models generate code with significantly different maintainability than HumanEval.

| CogC Comparison | Test Statistic | p-value | 
|--------------------------------------------------|----------------|--------------------------------|
|HumanEval_Complexity vs GPT3.5S | 2387.0 | 0.7576440001614906 | 
|HumanEval_Complexity vs GPT3.5I | 2225.5 | 0.4754973976804916 |                                                   |HumanEval_Complexity vs GPT3.5E | 761.0 | 3.093187015486396e-07 | 
|HumanEval_Complexity vs GPT4S | 1602.0 | 0.016611742877961713 | 
|HumanEval_Complexity vs GPT4I | 944.0 | 2.7772156242416405e-06 | 
|HumanEval_Complexity vs GPT4E | 975.0 | 1.3470173722438046e-09 |

Both GPT-3.5S and GPT-3.5I show no significant differences in complexity from HumanEval, with p-values of 0.7576 and 0.4755, respectively, indicating that their complexity is similar to HumanEval. However, the other models show highly significant differences. GPT-3.5E, with a p-value of 3.09e-07, indicates a significant difference, while GPT-4S (p-value 0.0166), GPT-4I (p-value 2.78e-06), and GPT-4E (p-value 1.35e-09) all exhibit notable differences in complexity compared to HumanEval.

## Calculation of TOPSIS

Please refer to the attached zipped file containing a reference example of a complete TOPSIS analysis. Including the whole example in the paper may not be possible due to space limitations, so we will upload it on our GitHub repository as auxiliary material.

# Individual Response to Reviewer 1

### Test case coverage and reliability

The HumanEval benchmark includes a comprehensive test suite for each problem. However, as the reviewer notes, test coverage information can help to make a more reliable judgment as to whether a solution is correct. We explored the CoverageEval dataset (currently on arxiv: https://arxiv.org/pdf/2307.13383v1), an extension of HumanEval that augments problems with detailed coverage metrics, offering an additional layer of insight into code quality and correctness. While our study currently uses test case pass rate for code correctness evaluations, future work could incorporate techniques like CoverageEval for a deeper analysis of code coverage and robustness. We can cite CoverageEval (https://arxiv.org/pdf/2307.13383v1) for future work.

### Explanation for security risks
Our results indicating that GPT-generated code can be less prone to security risks with simpler prompts, while more detailed prompts may slightly increase security concerns, could potentially be explained by the inclusion of HumanEval code in the Enhanced Prompt. This might expose the model to vulnerabilities inherent in the human-written code, which the model could replicate or amplify. This is, however, a speculative explanation. To validate it, further experiments are needed to provide a deeper understanding of the interplay between prompt design and security outcomes.


### Bandit Issue Summary

| Dataset       | File Name                                                 | Issue Severity | CWE |
|---------------|-----------------------------------------------------------|----------------|-----|
| Human Eval    | sample_data/Human_Eval_Dataset/Dataset/105.py             | LOW            | 703 |
|               | sample_data/Human_Eval_Dataset/Dataset/160.py             | MEDIUM         | 78  |
|               | sample_data/Human_Eval_Dataset/Dataset/162.py             | HIGH           | 327 |
|---------------|-----------------------------------------------------------|----------------|-----|
| GPT 3.5 S     | sample_data/GPT_3.5_Simple_Prompts/Dataset/162.py         | HIGH           | 327 |
|---------------|-----------------------------------------------------------|----------------|-----|
| GPT 3.5 I     | sample_data/GPT_3.5_Instruction_Tone_Prompt/Dataset/162.py| HIGH           | 327 |
|---------------|-----------------------------------------------------------|----------------|-----|
| GPT 3.5 E     | sample_data/GPT_3.5_Turbo_Enhanced_Prompt/Dataset/160.py  | MEDIUM         | 78  |
|               | sample_data/GPT_3.5_Turbo_Enhanced_Prompt/Dataset/162.py  | HIGH           | 327 |
|---------------|-----------------------------------------------------------|----------------|-----|
| GPT 4 S       | sample_data/GPT_4_Simple_Prompt/Dataset/162.py            | HIGH           | 327 |
|---------------|-----------------------------------------------------------|----------------|-----|
| GPT 4 I       | sample_data/GPT_4_Instruction_Tone_Prompt/Dataset/160.py  | MEDIUM         | 78  |
|               | sample_data/GPT_4_Instruction_Tone_Prompt/Dataset/162.py  | HIGH           | 327 |
|---------------|-----------------------------------------------------------|----------------|-----|
| GPT 4 E       | sample_data/GPT_4_Enhanced_Prompt/Dataset/162.py          | HIGH           | 327 |


### TOPSIS Normalization

The normalized value \( r_{ij} \) for an element \( x_{ij} \) in Table VI is calculated as:

\[
r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}
\]

where:
- \( x_{ij} \): The value of the \( i \)-th alternative for the \( j \)-th criterion.
- \( m \): The total number of alternatives. Each criterion's values are normalized to ensure comparability on a unit scale.

### Notion of Quality
For the reviewer's concern regarding our statement "*Our results indicate that LLMs specifically GPT-3.5-Turbo and GPT-4 are capable of producing better quality code than humans.": It's a bit more complicated than that. Does your notion of "quality" include correctness?*" We can rephrase as follows: GPT-3.5-Turbo and GPT-4 demonstrate the ability to generate higher-quality code, though this ability is not consistent; for example, Maintainability Index (MI) improves in only 54% of functionally correct model-generated solutions.

# Individual Response to Reviewer 2

### Rephrasing and Addition of RQs

We wholeheartedly accept the rephrased versions of the RQs. We can definitely revise our current RQs and include the two other additional RQs as suggested.

### Tool Selection Justification

The selection of Radon, Bandit, Pylint, and Complexipy for our study was driven by their alignment with our study's focus on evaluating a combination human-centric and critical code quality metrics. These tools provide complementary metrics that collectively address diverse aspects of code quality, enabling a balanced analysis of AI-generated code. Additionally, they are widely used, well-validated in both academic and industry contexts, and readily integrable into automated evaluation pipelines, ensuring practical applicability. While we acknowledge the existence of other tools and metrics, our selection was guided by their relevance to the study's objectives.

### Expanding Table V

Thank you for the very interesting insight on the challenges of manually recognizing buggy programs produced by LLMs. It gives us a great idea for future work, where we can perform more experiments and analyses to explore the hallucination aspect of code generation. For now, we have calculated the requested percentage of code samples (1) failing test cases and producing better metrics than HumanEval, (2) passing tests but producing worse metrics, and (3) failing tests and producing worse metrics.

**Percentage of Code Samples Failing Test Cases and Producing Better Metrics than Human Eval**

| Model       | LOC    | Cyclomatic Complexity | Vocabulary | Maintainability Index | Cognitive Complexity  |
|-------------|--------|-----------------------|------------|-----------------------|-----------------------|
| GPT 3.5 S   | 4.88   | 6.71                  | 10.98      | 25.00                 | 9.76                  |
| GPT 3.5 I   | 16.46  | 8.54                  | 12.20      | 19.51                 | 10.37                 |
| GPT 3.5 E   | 11.59  | 11.59                 | 13.41      | 16.46                 | 10.98                 |
| GPT 4 S     | 13.41  | 11.59                 | 9.15       | 19.51                 | 10.98                 |
| GPT 4 I     | 20.12  | 10.98                 | 10.98      | 16.46                 | 12.20                 |
| GPT 4 E     | 9.15   | 6.71                  | 9.15       | 10.37                 | 6.71                  |



**Percentage of Code Samples Failing Test Cases and Producing Worse Metrics than Human Eval**

| Model       | LOC    | Cyclomatic Complexity | Vocabulary | Maintainability Index | Cognitive Complexity  |
|-------------|--------|-----------------------|------------|-----------------------|-----------------------|
| GPT 3.5 S   | 23.78  | 21.95                 | 17.68      | 3.66                  | 18.90                 |
| GPT 3.5 I   | 18.29  | 26.22                 | 22.56      | 15.24                 | 24.39                 |
| GPT 3.5 E   | 12.80  | 12.80                 | 10.98      | 7.93                  | 13.41                 |
| GPT 4 S     | 17.07  | 18.90                 | 21.34      | 10.98                 | 19.51                 |
| GPT 4 I     | 7.93   | 17.07                 | 17.07      | 11.59                 | 15.85                 |
| GPT 4 E     | 3.66   | 6.10                  | 3.66       | 2.44                  | 6.10                  |


**Percentage of Code Samples Passing Test Cases and Producing Worse Metrics than Human Eval**

| Model       | LOC    | Cyclomatic Complexity | Vocabulary | Maintainability Index | Cognitive Complexity  |
|-------------|--------|-----------------------|------------|-----------------------|-----------------------|
| GPT 3.5 S   | 67.68  | 50.61                 | 51.22      | 17.07                 | 53.66                 |
| GPT 3.5 I   | 42.68  | 44.51                 | 42.68      | 37.20                 | 43.90                 |
| GPT 3.5 E   | 48.17  | 56.10                 | 43.90      | 34.15                 | 46.34                 |
| GPT 4 S     | 50.00  | 53.05                 | 38.41      | 29.88                 | 45.12                 |
| GPT 4 I     | 41.46  | 49.39                 | 43.29      | 34.76                 | 42.68                 |
| GPT 4 E     | 40.24  | 53.05                 | 48.17      | 33.54                 | 41.46                 |


### README.md
We will upload the README on our GitHub repo. For now, please refer to the attached file for README contents.


# Individual Response to Reviewer 3

We thank the reviewer for the detailed and thought-provoking review. It has helped us immensely to improve the positioning of our work. 

### Conclusions 
We first address the concern regarding the conclusions being unsurprising. Indeed the general trends indicate that large language model-generated code is easier to understand yet prone to correctness issues, as further evidenced in unit test generation. Our study provides a novel perspective by systematically analyzing and quantifying these trends using a diverse set of code quality metrics. By extending the analysis to encompass code metrics from a security perspective, human-perspective, and performance perspective in addition to correctness, we offer a deeper understanding of how these quality perspectives vary between human-written and model-generated code. Furthermore, our work lays the groundwork for leveraging these metrics to design improved benchmarks and tools that can guide future model development toward generating not just readable but also correct and trustworthy code.

It is important to note that correctness alone does not guarantee trustworthiness. Trustworthy code must also be reliable, secure, and aligned with best practices, which are not captured by correctness metrics. While our current work does not yet introduce explicit trustworthiness metrics, it lays the foundation for incorporating such measures in the future. By evaluating models across a spectrum of quality attributes, our work is a step toward developing frameworks for trustworthy code evaluation. This broader perspective highlights the importance of our contribution in advancing the discourse on trustworthiness in code generation.

### Enhanced Prompt Reliance of Human-written Solutions

We acknowledge that the dependency of the Enhanced Prompt approach on human-written solutions may raise questions about the validity of the evaluation outcomes when applied to autonomous code generation scenarios. However, the Enhanced Prompt approach was not intended as a standalone solution but rather as a method to explore how incorporating baseline examples influences model outputs. Our results demonstrate the capability of GPT models to produce better quality code against given baseline code. For code improvement workflows, where developers interact with models to iteratively refine code, the Enhanced Prompt approach may be useful.

### HumanEval of High Quality?

We explicitly acknowledge that the HumanEval dataset is not designed to represent gold-standard, optimal-quality code. However, its functional correctness makes it a reliable baseline for assessing code generation models, as it reflects real-world human practices and priorities in coding. Our findings aim to demonstrate the potential of GPT models to exceed these human benchmarks in quality, paving the way for broader adoption of code generation tools that prioritize both correctness and quality.

### Separate ranking of metrics

The decision to rank human-centric metrics and critical code quality metrics separately stems from our concern regarding the assignment of weights to these factors. Combining them into a single ranking requires determining appropriate weights for each metric, but the challenge arises in deciding how to allocate those weights fairly. If we were to apply equal weights across all metrics, we risk oversimplifying the complexity of the trade-offs between human-centric and critical factors. Alternatively, if we prioritize critical factors with higher weights, this could lead to a ranking that is disproportionately influenced by those metrics, potentially overshadowing human-centric considerations like readability or maintainability.

To avoid this bias and ensure transparency, we chose to present two separate rankings—one for human-centric metrics and one for critical code quality metrics. This approach allows for clearer interpretation and avoids conflating the two dimensions in a single score, thus maintaining the integrity of both sets of factors. However, we do recognize that a cumulative assessment could be valuable, and we hope that future work can explore appropriate ways to balance these dimensions, either by using domain expertise or data-driven approaches to assign weights.

### Model Configurations

Following are the technical details of the models used:
GPT 3.5 - Turbo
- Context Window: 16,385 tokens  
- Max Output Token: 4,096 tokens  
- Training Data: Up to Sep 2021  
- Hyper-parameter Setting: Default  Temperature: 1.0

GPT 4
- Context Window: 8,192 tokens  
- Max Output Token: 8,192 tokens  
- Training Data: Up to Sep 2021  
- Hyper-parameter Setting: Default  Temperature: 1.0

### Prompt Engineering

We appreciate the reviewer’s observation regarding the rationale behind our chosen prompts. Our approach was guided by OpenAI's guidelines for prompt engineering (https://platform.openai.com/docs/guides/prompt-engineering), which emphasize simplicity, clarity, and relevance to the task at hand. Our “simple” prompt serves as the simplest possible instruction, enabling us to assess the model's baseline capabilities without any contextual assistance. Its purpose was to establish how the model performs with minimal guidance. Building on the simple prompt, the instructional prompt provides explicit and structured guidance aligned with OpenAI’s recommended practices. This addition ensures that the model has a clear understanding of the expected output. The enhanced prompt incorporates additional context, including examples of human-written code, to simulate real-world use cases where developers refine code iteratively. This choice aligns with OpenAI’s guideline to use “few-shot” prompting for complex tasks, offering the model richer context to enhance its performance. By systematically designing and evaluating these prompts, we aim to contribute to the broader understanding of prompt engineering’s role in enhancing the performance and quality of AI-generated code. 

### LLM's Inherent Skill

We appreciate the reviewer’s insightful perspective on the distinction between the inherent code generation skill of LLMs and their post-exposure code generation skill. This is indeed an important consideration, and we believe our experimental setup accounts for both scenarios.
Specifically, we designed the instructional prompt to represent the pre-exposure scenario, where the model generates code based purely on the problem description, without additional context. Any observed improvement in this setting can be attributed to the model's inherent capability to generate functionally correct and high-quality code independently.
On the other hand, the enhanced prompt represents the post-exposure scenario, where the model is exposed to human-written code and tasked with generating better-quality code. In this case, any improvement reflects the model's inherent capability to leverage a wider context effectively, using the provided code as a baseline for improvement.
Importantly, in both scenarios, the output is always a product of the model’s inherent capabilities—either by generating high-quality code independently (instructional prompt) or by improving upon a given baseline (enhanced prompt). The distinction lies in the context provided: while the former is limited to problem constraints, the latter includes additional baseline parameters aimed at improving quality.

### Results Leading to Concrete Suggestions

We appreciate the reviewer’s question regarding the implications of our empirical results for improving code generation. We would like to clarify that our study goes beyond merely demonstrating that LLMs can produce understandable code. We highlight that multiple human-centric and critical quality factors, such as maintainability, modularity, and readability, are often improved in LLM-generated code compared to human-written baselines. Our empirical results emphasize the potential of LLMs to generate code that is of higher quality across critical quality dimensions and human-centric dimensions. By sharing our dataset and associated quality metrics, we enable the research community to address correctness issues while retaining human-centric and critical quality improvements. Our provided datasets can serve as a benchmark for subsequent studies aiming to improve code generation.

**Concrete Suggestions for Improving Code Generation:**

1. Optimize Prompts for Better Code:
Our findings emphasize the role of prompt design. Structuring prompts with clear instructions or examples of code can help LLMs generate higher-quality code. 

2. Train Models with Critical and Human-centric Quality Metrics:
Our results demonstrate that GPT models generate code that often surpasses human-written code in specific quality metrics. This highlights the potential for further improvement if critical and human-centric quality metrics are explicitly incorporated into the training process. By aligning the training objectives of LLMs with these metrics—reflected in our dataset and analysis—models could be better guided to generate code that balances correctness with other important quality factors.

3. Expand Evaluation Benchmarks for Comprehensive Code Quality Assessment:
Our study highlights the limitations of current evaluation benchmarks, such as HumanEval, which primarily focus on correctness. Our results show that LLM-generated code often performs better than human-written code in human-centric metrics like readability and maintainability, while sometimes falling short in critical factors like security. Our findings suggest that existing benchmarks should evolve to include a wider range of human-centric and critical quality metrics. Such expanded benchmarks would enable more comprehensive assessments of generated code, guiding both model evaluation and improvements in generating code that is not only correct but also aligned with developer needs and critical quality standards.

**Suggestion for Mining and Knowledge Extraction**
By providing a dataset of code quality metrics for human-written and AI-generated code, our work contributes to advancing the evaluation of code generation models beyond correctness, offering a comprehensive perspective on code quality. This dataset can serve as a valuable resource for the MSR community, enabling future research that explores how AI-generated code influences the overall quality of software repositories. Researchers can leverage these metrics to study patterns in AI-generated code, identify potential risks, and optimize code generation practices for integration into large-scale projects, ultimately improving the overall quality of software development.
