# CONTINUE.md – Project Guide

Welcome to the project guide! This document is intended to help developers new to the codebase quickly understand its purpose, structure, and workflow. Feel free to edit and expand sections as you learn more about the project.

---

## 1. Project Overview
- **Purpose**: This repository contains a collection of small Python example scripts that demonstrate basic programming concepts such as input handling, conditionals, loops, and simple algorithms.
- **Key Technologies**: Python 3, basic scripting.
- **High‑Level Architecture**: Each script is a standalone `.py` file located in the project root. The scripts are not part of a larger application but serve as learning material or quick reference examples.

---

## 2. Getting Started
### Prerequisites
- Python 3.x installed on your machine.
- A text editor or IDE capable of running Python scripts.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repo-directory>
   ```
2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

### Basic Usage
Run any script directly with Python:
```bash
python hello.py
python main.py
```

### Running Tests
If you add your own tests, you can run them using `unittest` or `pytest` once those dependencies are installed.

---

## 3. Project Structure
```
.
├── hello.py          # Simple grade/mark script
├── main.py           # Collection of various small scripts
└── .continue/
    └── rules/
        └── CONTINUE.md   # This documentation file
```

- **Root directory**: Holds all example Python scripts.
- **.continue/rules**: Contains custom rules and documentation for the Continue AI assistant.

---

## 4. Development Workflow
- **Coding Standards**: Follow standard Python PEP 8 style guide.
- **Version Control**: Commit changes frequently, write clear commit messages.
- **Testing**: Write simple unit tests for new scripts; place them alongside the code with a `test_*.py` naming convention.
- **Formatting**: Use `black` or `autopep8` to auto‑format code before committing.

---

## 5. Key Concepts
- **Input Handling**: Use `input()` to collect user data and `int()`/`float()` to convert to numeric types.
- **Control Flow**: `if`, `elif`, `else` statements for conditional logic.
- **Loops**: `for` loops with `range()` for iterating a known number of times.
- **Data Structures**: Basic usage of lists and membership operators (`in`).

---

## 6. Common Tasks
### Adding a New Example Script
1. Create a new `.py` file in the root directory.
2. Write the script, keeping it self‑contained.
3. Add a brief comment header describing its purpose.
4. Optionally add a corresponding test file.
5. Commit the change.

### Updating Documentation
- Edit this `CONTINUE.md` file to reflect new structure or concepts.
- If new directories or concepts emerge, update the **Project Structure** or **Key Concepts** sections accordingly.

---

## 7. Troubleshooting
| Issue | Solution |
|-------|----------|
| Python script fails to run | Ensure you are using Python 3.x and that all syntax is correct. |
| ModuleNotFoundError | Verify that any third‑party libraries are installed in your virtual environment. |
| Unclear script purpose | Review the comment headers; add documentation if needed. |

---

## 8. References
- Python Documentation: https://docs.python.org/3/
- Continue AI Documentation: https://docs.continue.dev/
- Python Style Guide (PEP 8): https://peps.python.org/pep-0008/

---

**Note:** This guide is a living document. If you encounter any gaps or have suggestions for improvement, please update the relevant sections or open an issue for discussion.