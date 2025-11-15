# AgenticAKM

This repository contains the codebase, data, and experimental artifacts associated with our paper **_AgenticAKM: Enroute to Agentic Architecture Knowledge Management_**.

In this work, we propose **AgenticAKM**, an agent-based approach that automates Architecture Knowledge Management (AKM) by decomposing complex AKM activities—such as architecture recovery and architectural documentation—into specialized sub-tasks. The repository provides the full experimentation workflow used in the study.


---

## Experimentation Workflow

The evaluation procedure conducted in our user study consists of the following steps:

1. **Repository Collection**  
   Participants submitted open-source GitHub repositories that they either owned or were highly familiar with.

2. **Generation of ADR Sets**  
   For each repository, we generated multiple sets of ADRs:  
   - ADRs generated using the **AgenticAKM** approach  
   - ADRs generated using a **baseline single-LLM-call** approach  
   - Both approaches were executed using **two different LLMs**, yielding **four ADR sets** per repository (2 approaches × 2 LLMs)

3. **Feedback Collection**  
   Participants received the generated ADRs and provided:  
   - Quantitative feedback (star ratings)  
   - Qualitative feedback (comments)  

4. **Analysis**  
   We analyzed the participant responses to derive insights into ADR quality and the comparative performance of the approaches. The details and results are provided in the paper.

---

## Abstract

Architecture Knowledge Management (AKM) is crucial for maintaining current and comprehensive software Architecture Knowledge (AK) in a software project. However AKM is often a laborious process and is not adopted by developers and architects. While LLMs present an opportunity for automation, a naive, single-prompt approach is often ineffective, constrained by context limits and an inability to grasp the distributed nature of architectural knowledge. To address these limitations, we propose an Agentic approach for AKM, AgenticAKM, where the complex problem of architecture recovery and documentation is decomposed into manageable sub-tasks. Specialized agents for architecture Extraction, Retrieval, Generation, and Validation collaborate in a structured workflow to generate AK. To validate we made an initial instantiation of our approach to generate Architecture Decision Records (ADRs) from code repositories. We validated our approach through a user study with 29 repositories. The results demonstrate that our agentic approach generates better ADRs, and is a promising and practical approach for automating AKM.

---

## Repository Structure and Description

### **Code/**  
Contains all implementation code, input data, and evaluation-related data used in the study.

### **AgenticAdr.xlsx**  
Includes two sheets:
- **Form response 1** — participant submissions of repository URLs  
- **Form response 2** — participant ratings and qualitative feedback for each ADR set

### **CodeToAdr.ipynb**  
Implements the **baseline approach**, where a single LLM call:
1. Analyzes salient parts of a repository  
2. Generates a corresponding set of ADRs  

This notebook was used to produce baseline ADR sets for all repositories in the user study.

### **AdrAgents.py**  
Defines the five agents used in the AgenticAKM workflow:

- **RepoSummarizer** — generates a summary of the repository  
- **SummaryCheckerAgent** — verifies correctness of the generated summary  
- **AdrWriterAgent** — generates ADRs using the validated summary  
- **AdrCheckerAgent** — checks correctness of the generated ADRs  
- **OrchestratorAgent** — coordinates the entire agentic workflow

### **main.ipynb**  
Runs the full AgenticAKM workflow using the agents in `AdrAgents.py` to generate ADRs for each repository included in the study.

### **evaluations.ipynb**  
Contains the quantitative and qualitative analysis of participant feedback and summarizes insights derived from the data.

### **AgenticAdr initialExperiment.ipynb**  
Includes early exploratory experiments. This notebook is optional for understanding or reproducing the main results.

---

### **Generated_ADRs/**  
Contains all ADRs generated in the study.

- Each repository has its own directory (e.g., `ameykaran_esell` corresponds to the repository at `https://github.com/ameykaran/esell/`).  
- Each repository directory contains four subdirectories (`dir1`, `dir2`, `dir3`, `dir4`), corresponding to the four ADR sets (2 approaches × 2 LLMs).  
- ZIP archives of these directories contain the ADR packages shared with participants.

