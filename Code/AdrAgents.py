"""
Imports and LLM Caller class for interacting with various LLMs (Gemini, GPT-5, etc.)
"""

import os
import subprocess
import tempfile
import shutil
from pathlib import Path
from dotenv import load_dotenv
import re
import json
from typing import List, Dict, Union
from datetime import datetime
from pydantic import BaseModel
import google.generativeai as genai
from openai import OpenAI

# --- Configuration ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE")
OPENAI_API_KEY = os.getenv("OPENAI")

genai.configure(api_key=GOOGLE_API_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

class LLMCaller:
    """
    A model-agnostic class for interacting with various LLMs (Gemini, GPT-5, etc.)
    """

    def __init__(self, model_name: str = "gemini-pro"):
        print(f"Initializing LLMCaller with model: {model_name}")
        self.model_name = model_name
        self.client = None

        if model_name.startswith("gpt"):
            # Initialize OpenAI client only if needed
            self.client = OpenAI(api_key=OPENAI_API_KEY)

    def call(self, prompt: str) -> str:
        """
        Sends a prompt to the selected LLM and returns the text response.
        """
        if self.model_name == "gemini-2.5-pro":
            llm = genai.GenerativeModel(self.model_name)
            response = llm.generate_content(prompt)
            return response.text

        elif self.model_name == "gpt-5":
            response = self.client.chat.completions.create(
                model="gpt-5",
                messages=[{"role": "user", "content": prompt}]
            )
            # print("ran with gpt-5")
            return response.choices[0].message.content

        else:
            raise ValueError(f"Unsupported model: {self.model_name}")
        
    

"""
RepoSummarizer
"""

class RepoSummarizer:
    """
    An agent to summarize a code repository using an LLM.
    """

    def __init__(self, model_name: str = "gemini-2.5-pro"):
        """
        Initializes the summarizer with a specific Gemini model.
        """
        print(f"Initializing with model: {model_name}")
        self.model = LLMCaller(model_name)
        self.ignore_patterns = [
            '.git', '__pycache__', 'node_modules', 'dist', 'build',
            '.DS_Store', '*.pyc', '*.log', '*.tmp', '*.swp'
        ]
        self.text_file_extensions = [
            '.py', '.js', '.ts', '.java', '.c', '.cpp', '.h', '.hpp', '.cs',
            '.go', '.rs', '.rb', '.php', '.html', '.css', '.scss', '.json',
            '.xml', '.yaml', '.yml', '.md', '.txt', '.sh', '.toml', '.ini',
            'Dockerfile', 'Makefile'
        ]


    def _is_text_file(self, file_path):
        """Checks if a file is likely a text file based on its extension."""
        return any(file_path.name.endswith(ext) for ext in self.text_file_extensions)


    def _get_repo_structure(self, repo_path):
        """
        Creates a string representation of the repository's file structure.
        """
        tree_str = ""
        for root, dirs, files in os.walk(repo_path):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if d not in self.ignore_patterns]
            
            level = root.replace(repo_path, '').count(os.sep)
            indent = ' ' * 4 * level
            tree_str += f"{indent}📁 {os.path.basename(root)}/\n"
            
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                if f not in self.ignore_patterns:
                    tree_str += f"{sub_indent}📄 {f}\n"
        return tree_str


    def _get_dependencies(self, repo_path):
        """
        Finds and reads common dependency files.
        """
        dependency_files = {
            "Python": "requirements.txt",
            "Node.js": "package.json",
            "Java (Maven)": "pom.xml",
            "Java (Gradle)": "build.gradle",
            "Ruby": "Gemfile",
        }
        found_deps = "No common dependency files found."
        for tech, filename in dependency_files.items():
            path = Path(repo_path) / filename
            if path.exists():
                try:
                    found_deps = f"--- {tech} Dependencies ({filename}) ---\n"
                    found_deps += path.read_text(encoding='utf-8') + "\n\n"
                except Exception as e:
                    found_deps += f"Could not read {filename}: {e}\n\n"
        return found_deps


    def _summarize_key_files(self, repo_path, num_files=5):
        """
        Finds the largest text files and generates a summary for each.
        """
        file_sizes = []
        for root, _, files in os.walk(repo_path):
            if any(part in root for part in self.ignore_patterns):
                continue
            for file in files:
                file_path = Path(root) / file
                if self._is_text_file(file_path):
                    try:
                        size = file_path.stat().st_size
                        if size > 100: # Ignore very small files
                            file_sizes.append((file_path, size))
                    except FileNotFoundError:
                        continue

        # Sort files by size in descending order and get the top N
        file_sizes.sort(key=lambda x: x[1], reverse=True)
        key_files = [f[0] for f in file_sizes[:num_files]]

        print(f"\nSummarizing the {len(key_files)} largest files...")
        summaries = []
        for file_path in key_files:
            relative_path = file_path.relative_to(repo_path)
            print(f"  - Reading: {relative_path}")
            try:
                content = file_path.read_text(encoding='utf-8')
                if len(content.strip()) == 0:
                    continue

                prompt = f"""
                Analyze the following code from the file '{relative_path}'.
                Provide a concise, high-level summary (2-3 sentences) of its purpose and key functionality.

                ```
                {content[:4000]}
                ```
                """
                response = self.model.call(prompt)
                summaries.append(f"📄 **File: {relative_path}**\n{response}\n")
            except Exception as e:
                summaries.append(f"📄 **File: {relative_path}**\n   - Could not summarize: {e}\n")

        return "\n".join(summaries)


    def summarize_repo(self, repo_path: str, feedback: str = None) -> str:
        """
        Summarizes a repository from a local path, using optional feedback to improve accuracy.
        """
        if not os.path.isdir(repo_path):
            return "Error: Provided repository path is not a directory."

        # Add a header for regeneration attempts
        if feedback:
            print("\nRe-generating summary with feedback...")
        else:
            print("\nAnalyzing repository structure...")
        
        structure = self._get_repo_structure(repo_path)
        dependencies = self._get_dependencies(repo_path)
        file_summaries = self._summarize_key_files(repo_path)

        feedback_prompt_section = ""
        if feedback:
            feedback_prompt_section = f"""
            --- PREVIOUS ATTEMPT FEEDBACK ---
            A previous attempt to summarize this repository was found to be inaccurate.
            Use the following feedback to create a new, more accurate summary.
            Do not repeat the previous mistakes.

            Feedback: {feedback}
            ---
            """

        final_prompt = f"""
        You are a senior software architect...
        Based on the information provided below, generate a comprehensive, high-level summary.
        {feedback_prompt_section}
        --- REPOSITORY INFORMATION ---
        **1. File & Directory Structure:**
        ```
        {structure[:4000]}
        ```
        **2. Detected Dependencies:**
        ```
        {dependencies}
        ```
        **3. Summaries of Key Files:**
        ```
        {file_summaries}
        ```
        --- END OF INFORMATION ---
        Provide the final summary in a clear, well-structured markdown format.
        """
        final_response = self.model.call(final_prompt)
        return final_response
    


"""
SummaryChecker
"""
class SummaryCheckerAgent:
    """
    Verifies a summary and provides actionable feedback for correction if it's inaccurate.
    """
    def __init__(self,  model_name: str = "gemini-2.5-pro"):
        print("Initializing SummaryCheckerAgent...")
        self.model = LLMCaller(model_name)

    def verify_summary(self, summary: str, repo_path: str) -> (bool, str):
        """
        Verifies the summary and generates corrective feedback if needed.

        Returns:
            A tuple containing:
            - A boolean: True if the summary is correct, False otherwise.
            - A string: A justification if correct, or actionable feedback if incorrect.
        """
        print(f"Verifying summary against the code in {repo_path}...")
        tree_str = ""
        # (The logic to get tree_str remains the same as before)
        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules']]
            level = root.replace(repo_path, '').count(os.sep)
            indent = ' ' * 4 * level
            tree_str += f"{indent}{os.path.basename(root)}/\n"
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                tree_str += f"{sub_indent}{f}\n"

        prompt = f"""
        You are a meticulous code reviewer. Your task is to determine if the given **Summary**
        accurately reflects the provided **Repository Context**.

        **Repository Context (File and Directory Structure):**
        ---
        {tree_str[:4000]}
        ---

        **Summary to Verify:**
        ---
        {summary}
        ---

        First, provide your verdict as a single word: **CORRECT** or **INCORRECT**.
        - If the verdict is **CORRECT**, follow it with a colon and a brief justification.
        - If the verdict is **INCORRECT**, follow it with a colon and then, on a new line, provide actionable **FEEDBACK** for the summarizer agent on how to fix the summary. This feedback should be a clear instruction.

        Example CORRECT response:
        CORRECT: The summary accurately identifies this as a Java project.

        Example INCORRECT response:
        INCORRECT: The summary incorrectly identifies this as a Python project.
        FEEDBACK: The repository contains `pom.xml` and Java source files, not Python files. Please regenerate the summary identifying the project as a Java Maven application.
        """
        response = self.model.call(prompt)
        result_text = response.strip()
        
        is_correct = result_text.startswith("CORRECT")
        feedback = result_text

        if is_correct:
            print(f"-> Verification Result: CORRECT")
        else:
            print(f"-> Verification Result: INCORRECT")
        
        return is_correct, feedback
    

"""
AdrWriterAgent
"""
# --- Data Model for an ADR ---
class ADR(BaseModel):
    """Represents a single Architecture Decision Record."""
    title: str
    context: str
    decision: str
    # Accept either a simple string or a structured dictionary for consequences
    consequences: Union[str, Dict[str, List[str]]]

# --- ADR Writer Agent ---
class AdrWriterAgent:
    """
    An agent that analyzes a repository summary to identify, format,
    and save key design decisions as Architecture Decision Records (ADRs).
    """
    def __init__(self,  model_name: str = "gemini-2.5-pro"):
        print("Initializing AdrWriterAgent...")
        self.model = LLMCaller(model_name)


    def _extract_design_decisions(self, summary: str, feedback: str = None) -> List[Dict]:
        """
        Uses the LLM to extract design decisions, with a more robust prompt.
        """
        if feedback:
            print("Re-extracting design decisions with new feedback...")
        else:
            print("Extracting design decisions from the summary...")

        feedback_prompt_section = ""
        if feedback:
            feedback_prompt_section = f"""
            --- PREVIOUS ATTEMPT FEEDBACK ---
            A previous attempt to generate ADRs was found to be inaccurate.
            Use the following feedback to create a new, more accurate set of ADRs based on the summary.

            Feedback: {feedback}
            ---
            """

        prompt = f"""
        You are an expert senior software architect. Your task is to analyze the provided repository summary
        and extract the most critical architectural and technological design decisions.
        {feedback_prompt_section}
        **Repository Summary**:
        ---
        {summary}
        ---

        Return your response as a valid JSON array of objects.
        **It is critical that each object in the array has the following four string keys exactly as written: `title`, `context`, `decision`, `consequences`.**
        
        Do not use any other key names. For example, do not use `decision_point` instead of `title`. The format must be strictly followed.
        """
        response = self.model.call(prompt)
        clean_response = response.strip().replace("```json", "").replace("```", "").strip()
        
        try:
            decisions = json.loads(clean_response)
            print(f"Successfully extracted {len(decisions)} design decisions.")
            return decisions
        except json.JSONDecodeError:
            print(f"Error: The model did not return a valid JSON. Raw response:\n{clean_response}")
            # Return an empty list to prevent crashes, allowing the feedback loop to potentially correct it.
            return []

    def _format_adrs(self, adrs: List[ADR]) -> List[str]:
        """
        Formats a list of ADR objects into a list of markdown strings.
        This method NO LONGER saves files.
        """
        if not adrs:
            return []

        formatted_adrs_list = []
        for i, adr in enumerate(adrs, start=1):
            consequences_text = ""
            if isinstance(adr.consequences, dict):
                pros = adr.consequences.get("pros", [])
                cons = adr.consequences.get("cons", [])
                if pros:
                    consequences_text += "**Pros:**\n" + "\n".join(f"- {item}" for item in pros) + "\n\n"
                if cons:
                    consequences_text += "**Cons:**\n" + "\n".join(f"- {item}" for item in cons)
            else:
                consequences_text = adr.consequences

            adr_text = f"""# ADR-{i:03d}: {adr.title}

**Date**: {datetime.now().strftime('%Y-%m-%d')}
**Status**: Proposed

## Context
{adr.context}

## Decision
{adr.decision}

## Consequences
{consequences_text.strip()}
"""
            formatted_adrs_list.append(adr_text.strip())
        
        return formatted_adrs_list

    def write_adrs(self, summary: str, feedback: str = None) -> (List[ADR], List[str]):
        """
        Main method to generate and format ADRs.

        Returns:
            A tuple containing:
            - A list of the structured ADR Pydantic objects.
            - A list of the formatted ADR strings.
        """
        decisions_data = self._extract_design_decisions(summary, feedback)
        if not decisions_data:
            return [], [] # Return empty lists if extraction fails
        
        # print(type(decisions_data))
        # print(decisions_data)
        adrs = [ADR(**data) for data in decisions_data]
        formatted_adrs = self._format_adrs(adrs)
        return adrs, formatted_adrs


"""
ADR Checker
"""
class AdrCheckerAgent:
    """
    Verifies that a list of ADRs is logical, well-formed, and consistent
    with the provided repository summary. Provides feedback for correction.
    """
    def __init__(self,  model_name: str = "gemini-2.5-pro"):
        print("Initializing AdrCheckerAgent...")
        self.model = LLMCaller(model_name)

    def verify_adrs(self, summary: str, adrs: List[str]) -> (bool, str):
        """
        Verifies the ADRs against the repository summary.

        Returns:
            A tuple containing:
            - A boolean: True if the ADRs are deemed correct, False otherwise.
            - A string: A justification if correct, or actionable feedback if incorrect.
        """
        print("Verifying generated ADRs against the summary...")
        # Join the list of ADR strings into a single block for the prompt
        adrs_text = "\n\n---\n\n".join(adrs)

        prompt = f"""
        You are a principal software architect reviewing a set of auto-generated
        Architecture Decision Records (ADRs). Your task is to ensure the ADRs are logical,
        well-written, and directly supported by the provided **Repository Summary**.

        **Repository Summary:**
        ---
        {summary}
        ---

        **ADRs to Verify:**
        ---
        {adrs_text}
        ---

        Analyze the ADRs. Do they capture the most important architectural decisions
        mentioned in the summary (e.g., choice of framework, database, architecture pattern)?
        Are the 'Context', 'Decision', and 'Consequences' sections plausible for a project
        as described in the summary?

        Your final answer MUST begin with a single word: **CORRECT** or **INCORRECT**.
        - If **CORRECT**, provide a brief justification.
        - If **INCORRECT**, provide actionable **FEEDBACK** for the ADR writing agent.

        Example CORRECT response:
        CORRECT: The ADRs accurately capture the key decisions regarding the multi-module Maven structure and the use of AngularJS on the frontend.

        Example INCORRECT response:
        INCORRECT: ADR-2, which discusses PostgreSQL, is not supported by the summary that explicitly mentions an H2 embedded database.
        FEEDBACK: Please correct ADR-2 to reflect the use of the H2 database as stated in the summary. Additionally, add a new ADR for the decision to use a multi-module Maven monorepo, as this is a key architectural choice mentioned in the summary.
        """
        response = self.model.call(prompt)
        result_text = response.strip()

        is_correct = result_text.startswith("CORRECT")
        feedback = result_text

        if is_correct:
            print("-> Verification Result: ADRs are CORRECT")
        else:
            print("-> Verification Result: ADRs are INCORRECT")

        return is_correct, feedback


"""
Orchestrator
"""
class OrchestratorAgent:
    """
    Orchestrates the workflow with a self-correcting feedback loop for summarization.
    1. Clone a repo.
    2. Summarize it.
    3. Verify the summary.
    4. Generate ADRs from the verified summary.
    """
    def __init__(self,  model_name: str = "gemini-2.5-pro"):
        print("Initializing the Orchestrator Agent...")
        self.summarizer_agent = RepoSummarizer(model_name=model_name)
        self.summary_checker_agent = SummaryCheckerAgent(model_name=model_name)
        self.adr_writer_agent = AdrWriterAgent(model_name=model_name)
        self.adr_checker_agent = AdrCheckerAgent(model_name=model_name)
        print("Orchestrator is ready with all subordinate agents.")

    def _clone_repo(self, repo_url: str) -> str:
        """
        Clones a repository into a temporary directory.
        Returns the path to the temporary directory.
        """ 
        temp_dir = tempfile.mkdtemp()
        try:
            print(f"Cloning {repo_url} into temporary directory {temp_dir}...")
            subprocess.check_call(['git', 'clone', repo_url, temp_dir], stderr=subprocess.DEVNULL)
            print("Cloning successful.")
            return temp_dir
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"Error cloning repository: {e}. Please check the URL and that Git is installed.")
            # Clean up the failed clone attempt
            shutil.rmtree(temp_dir)
            return None
        
    def _sanitize_filename(self, name: str) -> str:
        """
        Helper method now owned by the orchestrator.
        """
        name = name.replace(' ', '_')
        name = re.sub(r'[^\w\.-]', '', name)
        return name[:100]

    def _save_adrs(self, adrs: List[ADR], formatted_adrs: List[str], output_path: str):
        """
        Saves the final, verified ADRs to disk.
        """
        if not adrs:
            print("No ADRs to save.")
            return

        os.makedirs(output_path, exist_ok=True)
        print(f"Saving final ADRs to directory: '{os.path.abspath(output_path)}'")

        for i, (adr_object, adr_content) in enumerate(zip(adrs, formatted_adrs), start=1):
            safe_filename = self._sanitize_filename(adr_object.title)
            filename = f"{i:03d}_{safe_filename}.md"
            file_path = os.path.join(output_path, filename)
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(adr_content)
                print(f"  -> Successfully saved {filename}")
            except IOError as e:
                print(f"  -> Failed to save {filename}. Error: {e}")

    def run(self, repo_url: str, adr_output_path: str, max_attempts: int = 3):
        print("\n" + "="*50)
        print("🚀 Starting Orchestration Workflow")
        print("="*50)

        repo_path = self._clone_repo(repo_url)
        if not repo_path: return []

        # --- LOOP 1: Summary Generation and Verification ---
        summary = ""
        summary_feedback = None
        is_summary_correct = False
        for attempt in range(max_attempts):
            print("-" * 50)
            print(f"🔥 Summary Generation Attempt {attempt + 1} of {max_attempts}")
            print("-" * 50)
            
            summary = self.summarizer_agent.summarize_repo(repo_path=repo_path, feedback=summary_feedback)
            is_summary_correct, summary_feedback = self.summary_checker_agent.verify_summary(summary=summary, repo_path=repo_path)
            print(f"Feedback Received: {summary_feedback}")

            if is_summary_correct:
                print("\n✅ Summary confirmed accurate. Proceeding to ADR generation.")
                break
            else:
                print("\n❌ Summary incorrect. Will attempt to regenerate.")
        
        # if not is_summary_correct:
        #     print(f"\n🚨 Workflow Halted: Failed to generate an accurate summary after {max_attempts} attempts.")
        #     return []

        # --- LOOP 2: ADR Generation and Verification ---
        list_of_adr_objects = []
        list_of_adr_strings = []
        adr_feedback = None
        are_adrs_correct = False
        for attempt in range(max_attempts):
            print("-" * 50)
            print(f"🔥 ADR Generation Attempt {attempt + 1} of {max_attempts}")
            print("-" * 50)

            # 1. GENERATE ADRs (content only, no saving yet)
            list_of_adr_objects, list_of_adr_strings = self.adr_writer_agent.write_adrs(summary=summary, feedback=adr_feedback)
            
            # 2. VERIFY the generated ADRs
            if not list_of_adr_strings:
                print("ADR writer returned no content. Continuing attempt.")
                adr_feedback = "The previous attempt returned no content. Please try again, ensuring you generate valid ADRs from the summary."
                continue

            are_adrs_correct, adr_feedback = self.adr_checker_agent.verify_adrs(summary=summary, adrs=list_of_adr_strings)
            print(f"Feedback Received: {adr_feedback}")

            if are_adrs_correct:
                print("\n✅ ADRs confirmed accurate.")
                break
            else:
                print("\n❌ ADRs incorrect. Will attempt to regenerate.")

        # if not are_adrs_correct:
        #     print(f"\n🚨 Workflow Halted: Failed to generate accurate ADRs after {max_attempts} attempts.")
        #     return []

        # --- FINAL STEP: Save the approved ADRs ---
        print("\n" + "="*50)
        print("💾 Saving verified ADRs to disk...")
        self._save_adrs(list_of_adr_objects, list_of_adr_strings, adr_output_path)
        
        print("\n🎉 Orchestration Workflow Finished Successfully!")
        print("="*50)
        return list_of_adr_strings
    
