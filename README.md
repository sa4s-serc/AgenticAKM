# AgenticAKM

This repository contains code and data for for our paper: **AgenticAKM : Enroute to Agentic Architecture Knowledge Management**

In this work we propose AgenticAKM, an agent-based approach that automates Architecture Knowledge Management by dividing specific AKM tasks like architecture recovery and documentation into specialized sub-tasks. This repository contains the experimentation for the work.

The experimentation workflow is:
- We ask participants to submit opensource Github repositories which they own, or know very well.
- We generate a sets of ADRs for a given code repository. We generate using AgenticAKM and a also a baseline single LLM call. We also deploy 2 LLMs. This results in 4 sets (2 approach * 2 LLM) of ADRs generated for each repository.
- We give back the the generated ADRs to the participants, and ask them for feedback, in star rating (quantative) as well as comments (qualitative).
- We analyze the feedback and get insights.
- We evaluate with a user study. The details are given in the paper.


## Abstract

Architecture Knowledge Management (AKM) is crucial for maintaining current and comprehensive software Architecture Knowledge (AK) in a software project. However AKM is often a laborious process and is not adopted by developers and architects. While LLMs present an opportunity for automation, a naive, single-prompt approach is often ineffective, constrained by context limits and an inability to grasp the distributed nature of architectural knowledge. To address these limitations, we propose an Agentic approach for AKM, AgenticAKM, where the complex problem of architecture recovery and documentation is decomposed into manageable sub-tasks. Specialized agents for architecture Extraction, Retrieval, Generation, and Validation collaborate in a structured workflow to generate AK. To validate we made an initial instantiation of our approach to generate Architecture Decision Records (ADRs) from code repositories. We validated our approach through a user study with 29 repositories. The results demonstrate that our agentic approach generates better ADRs, and is a promising and practical approach for automating AKM.


## Repository Description

The **Code** directory has all the code, along with input data and data for evaluations.

- **AgenticAdr.xlsx** has 2 sheets, 'Form response 1' and 'Form reponse 2'. 'Form response 1' contains response to the first form we gave out. Here we get the code repository url.
After generating the ADRs, we sent out another form to collect the feedback. The response for this form is stored in 'Form response 2'. Here we get the star rating as well as the qualitative comments for each set of generated ADRs.

- **CodeToAdr.ipynb** has the baseline apporach, where a we try to generate a set of ADRs given a code repository in a single LLM call. Within 1 LLM call we analyze the important sections of the repository and then generate the set of ADRs. We generate ADRs for the given set of repositories, as per the user study.

- The **AdrAgents.py** has the 5 agents defined, i.e. _RepoSummarizer_, _SummaryCheckerAgent_, _AdrWriterAgent_, _AdrCheckerAgent_, and the _OrchestratorAgent_. RepoSummarizer generates a summary given a repository; SummaryCheckerAgent checks if that generated summary is correct; AdrWriterAgent then takes this summary and generates a set of ADRs; AdrCheckerAgent then checks if the generates ADRs are correct. The Orchrestrartor orchrestartes the whole flow.
The **main.ipynb** uses the agents mentioned above from AdrAgents.py, and creates ADRs from repositorie. We generate ADRs for the given set of repositories, as per the user study.

- After getting user responses, we evaluate and analyse it to get valuable insights. These are captured in **evaluations.ipynb**

- **AgenticAdr initialExperiment.ipynb** has some initial experiments. One may look at it for curiosity, or safely ignore it.

___

The **Generated_ADRs** directory has all the generated ADRs.
- The directories name are for each repository. For example _ameykaran_esell_ is for the repo _https://github.com/ameykaran/esell/_ .
- Each directory has 4 sub directories named dir1, dir2, dir3, dir4, which has the 4 sets of generated ADRs.
- The zips are just zips of these directories that were sent out to the participants.
