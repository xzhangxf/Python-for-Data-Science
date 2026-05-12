# Python for Data Science

This repository contains a full Python for Data Science piscine-style learning path with progressive exercises, from basic Python scripts to arrays, data tables, OOP, and data-oriented design.

It is organized into 5 modules:

1. Python - 0 - Starting
2. Python - 1 - Array
3. Python - 2 - DataTable
4. Python - 3 - OOP
5. Python - 4 - Dod

## Repository Overview

This repository is a hands-on training project built around small, focused exercises.

It was created to:

- Practice Python fundamentals through short executable tasks
- Build clean coding habits (functions, error handling, explicit imports)
- Introduce scientific/data tooling used in data science workflows
- Move progressively from procedural scripts to object-oriented and data-oriented design

Who this repository is for:

- Beginners learning Python step by step
- Students preparing for piscine-style peer evaluations
- Recruiters/reviewers who want to see incremental skill growth in real code

## Subject / Project Context

Based on the provided subject PDFs, this piscine expects:

- Python 3.10
- Explicit imports (`import numpy as np` style)
- No global variable usage
- Function-based structure (`main()` + `if __name__ == "__main__":`)
- Error handling (uncaught exceptions can invalidate exercises)
- Progress through modules in order (0 -> 1 -> 2 -> 3 -> 4)

Main learning outcomes:

- Core Python syntax and scripting
- Type checking and argument validation
- Arrays and image manipulation
- Data loading, cleaning, and visualization
- OOP fundamentals (abstract classes, inheritance, properties)
- Data-oriented utility patterns (decorators, closures, dataclasses)

Submission/evaluation notes from the subjects:

- Work is graded from Git repository content
- Peer evaluation is required
- Flake8-style norm is referenced in multiple module subjects

## Module Overview

| Module | Topic | Main Learning Goal |
|---|---|---|
| Python - 0 - Starting | Python basics | Learn core syntax, CLI scripts, types, basic utilities, and first package creation |
| Python - 1 - Array | Arrays and images | Practice NumPy-style thinking, slicing, image loading, zoom/rotate/filter operations |
| Python - 2 - DataTable | Tabular data and plotting | Load CSV data with pandas and build visualizations with matplotlib |
| Python - 3 - OOP | Object-Oriented Programming | Build abstract/base classes, inheritance models, properties, and vector calculators |
| Python - 4 - Dod | Data-Oriented Design | Implement statistical utilities, closures, decorators, and dataclass-based modeling |

## Technologies Used

| Technology | How It Is Used |
|---|---|
| Python 3 | Main language for all exercises and scripts |
| NumPy | BMI computations, array validation, image array handling |
| pandas | CSV loading and tabular data handling in DataTable module |
| matplotlib | Data and image plotting (line charts, scatter, image display) |
| Pillow (PIL) | Image file loading into NumPy arrays |
| `abc` (standard library) | Abstract base class design in OOP module |
| `dataclasses` (standard library) | Student data model in DOD module |
| `typing` (standard library) | Type hints for clarity and exercise constraints |
| `tqdm` | Used in a comparison tester for custom progress bar exercise |
| setuptools / wheel / pyproject.toml | Packaging metadata and build setup in `ex09/ft_package` |

## Repository Structure

```text
Python-for-Data-Science/
├── Python - 0 - Starting/
│   ├── en.subject.pdf
│   └── Training Piscine Python for datascience - 0/
│       ├── ex00/ ... ex09/
│       └── venv/
├── Python - 1 - Array/
│   ├── en.subject (1).pdf
│   └── Training Piscine Python for datascience- 1/
│       └── ex00/ ... ex05/
├── Python - 2 - DataTable/
│   ├── en.subject.pdf
│   ├── venvrun.txt
│   └── Training Piscine Python for datascience - 2/
│       └── ex00/ ... ex03/
├── Python - 3 - OOP/
│   ├── en.subject (1).pdf
│   └── Training Piscine Python for datascience- 3/
│       └── ex00/ ... ex04/
├── Python - 4 - Dod/
│   ├── en.subject.pdf
│   └── Training Piscine Python for datascience - 4/
│       └── ex00/ ... ex03/
├── en.subject.pdf
├── README.md
├── LICENSE
├── .gitignore
└── virtual/
```

| Path | Purpose |
|---|---|
| Python - 0 - Starting/ | First module focused on Python basics |
| Python - 1 - Array/ | Array and image manipulation exercises |
| Python - 2 - DataTable/ | CSV/data table loading and visualization exercises |
| Python - 3 - OOP/ | Class design, inheritance, and object behavior |
| Python - 4 - Dod/ | Data-oriented design patterns and utilities |
| en.subject.pdf | Root piscine overview (module sequence and context) |
| README.md | Main repository documentation |
| LICENSE | MIT license text |
| virtual/ | Local environment directory |

## Learning Path

Recommended study order:

1. **Python - 0 - Starting**
	Focus on syntax, types, command-line arguments, and small reusable functions.
2. **Python - 1 - Array**
	Focus on numeric arrays, slicing, shapes, and image data as arrays.
3. **Python - 2 - DataTable**
	Focus on loading CSVs, preparing values, and plotting insights.
4. **Python - 3 - OOP**
	Focus on classes, inheritance, abstract classes, and method organization.
5. **Python - 4 - Dod**
	Focus on function composition, decorators, closures, and dataclasses.

## How to Set Up the Project

```bash
git clone https://github.com/xzhangxf/Python-for-Data-Science.git
cd Python-for-Data-Science
```

Optional virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Dependencies are not centralized in a root requirements file.

No `requirements.txt` file was found. Dependencies should be verified from the imports used in each exercise.

Typical dependencies inferred from code:

```bash
pip install numpy pandas matplotlib pillow tqdm
```

## How to Run Exercises

General form:

```bash
python3 "path/to/file.py"
```

Examples:

```bash
python3 "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex04/whatis.py" 14
python3 "Python - 1 - Array/Training Piscine Python for datascience- 1/ex00/tester.py"
python3 "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex04/tester.py"
```

Some scripts are meant as utility modules and are normally executed via their tester or importing script.

## Testing / Manual Verification

No unified automated test suite (pytest/unittest) is defined at repository root.
Most exercises include `tester.py` or executable script examples.

| Module | Example Command | Expected Result |
|---|---|---|
| Python - 0 - Starting | `cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex06" && python3 filterstring.py 'Hello the World' 4` | Prints `['Hello', 'World']` |
| Python - 1 - Array | `python3 "Python - 1 - Array/Training Piscine Python for datascience- 1/ex00/tester.py"` | Prints BMI list and threshold comparison |
| Python - 2 - DataTable | `cd "Python - 2 - DataTable/Training Piscine Python for datascience - 2/ex01" && python3 aff_life.py` | Loads CSV and plots life expectancy for Singapore |
| Python - 3 - OOP | `python3 "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex04/tester.py"` | Prints dot product / vector add / vector subtract |
| Python - 4 - Dod | `python3 "Python - 4 - Dod/Training Piscine Python for datascience - 4/ex00/tester.py"` | Prints mean/median/quartile/std/var and `ERROR` cases |

Known verification note:

- `Python - 2 - DataTable/.../ex00/test_load.py` imports `from ex03.load_csv import load` and fails directly with `ModuleNotFoundError` when run as-is. **This part should be verified.**

## Skills Demonstrated

- Python scripting and CLI argument parsing
- Type hints and input validation
- Exception handling
- List comprehensions and lambda usage
- Custom iterator/progress behavior with `yield`
- Basic package creation with `pyproject.toml`
- NumPy array operations and slicing
- Image loading and pixel-level transformation
- pandas DataFrame loading and filtering
- Data visualization with matplotlib
- OOP with abstract classes and inheritance
- Decorators, closures, and dataclasses
- Basic code organization by module/exercise

## Notes for Recruiters / Reviewers

This repository demonstrates progressive, practical Python learning in a structured curriculum.
It shows iterative skill growth from small scripts to data handling and class-based design, with many exercises that include input checks and explicit outputs.

## License

This project is licensed under the MIT License. See LICENSE for details.

## Final Summary

`Python-for-Data-Science` is a complete step-by-step training repository for learning Python in a data science context.
By working through the modules in order, learners practice core Python, array/data operations, visualization, OOP design, and data-oriented programming techniques.
