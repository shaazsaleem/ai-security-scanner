import os
import sys
from dotenv import load_dotenv
import google.genai as genai
from colorama import init, Fore, Style
# Initialize colorama and autoreset colors back to normal after each run
init(autoreset=True)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model = genai.Client(api_key=api_key)

security_prompt = """
Analyze this code for security vulnerabilities. Be concise.

For each issue use this exact format:

---
SEVERITY: [CRITICAL/HIGH/MEDIUM/LOW]
TYPE: [Vulnerability Name]
DESCRIPTION: [One sentence explaining the issue]
IMPACT: [One sentence on potential damage]
FIX: [Code snippet only]
---

Code:
{code}
"""

def color_code_output(outputtedText):
    outputtedText = outputtedText.replace("SEVERITY: CRITICAL", f"SEVERITY: {Fore.RED}{Style.BRIGHT}CRITICAL{Style.RESET_ALL}")
    outputtedText = outputtedText.replace("SEVERITY: HIGH", f"SEVERITY: {Fore.YELLOW}{Style.BRIGHT}HIGH{Style.RESET_ALL}")
    outputtedText = outputtedText.replace("SEVERITY: MEDIUM", f"SEVERITY: {Fore.BLUE}MEDIUM{Style.RESET_ALL}")
    outputtedText = outputtedText.replace("SEVERITY: LOW", f"SEVERITY: {Fore.GREEN}LOW{Style.RESET_ALL}")
    return outputtedText

# File path from command line: python3.13 scanner.py <file_path>
if len(sys.argv) < 2:
    print("Usage: python3.13 scanner.py <file_path>")
    sys.exit(1)

codePath = sys.argv[1]
with open(codePath, "r") as fileName:
    code = fileName.read()

prompt = security_prompt.format(code=code)

try:
    response = model.models.generate_content(model = 'gemini-2.5-flash', contents=prompt)
    print(color_code_output(response.text))
except Exception as e:
    print(f"Connection failed: {e}")