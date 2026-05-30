# 🔒 AI Security Scanner for Python

A command-line tool that uses Google's Gemini AI to scan Python code for security vulnerabilities with color-coded severity ratings.

## What It Does

Paste or scan Python code and get instant AI-powered security analysis that detects:

- 💉 **SQL Injection** vulnerabilities
- 🔑 **Hardcoded Secrets** (API keys, passwords)
- 🔓 **Weak Cryptography** (insecure hashing, outdated algorithms)
- ⚠️ Other common security anti-patterns

Results are displayed with color-coded severity levels:
- 🔴 **CRITICAL** — Needs immediate attention
- 🟡 **HIGH** — Should be fixed soon
- 🔵 **MEDIUM** — Moderate risk
- 🟢 **LOW** — Minor issue

## Tech Stack

- **Python 3.13**
- **Google Gemini API** — AI-powered code analysis
- **python-dotenv** — Secure API key management
- **colorama** — Color-coded terminal output

## Getting Started

### Prerequisites
- Python 3.13+
- A free [Google Gemini API key](https://aistudio.google.com/apikey)

### Installation

```bash
# Clone the repo
git clone https://github.com/shaazsaleem/ai-security-scanner.git
cd ai-security-scanner

# Create and activate a virtual environment
python3.13 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

### Usage

```bash
python3.13 scanner.py <file_to_check>
```

## Built With

This project was built as part of [NextWork's](https://learn.nextwork.org) AI Security Scanner project.

## License

MIT
