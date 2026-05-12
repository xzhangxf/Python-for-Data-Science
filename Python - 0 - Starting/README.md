# Python - 0 - Starting

This module introduces Python fundamentals through 10 small exercises (`ex00` to `ex09`), including data types, formatting, functions, CLI scripts, filtering, Morse encoding, generators, and first package creation.

## Module Overview

What this module teaches:

- Basic Python syntax and built-in data structures
- Function writing with simple return contracts
- Command-line argument parsing and error handling
- Text processing and filtering
- Dictionary-based encoding
- Generator-style progress display
- Packaging basics (`pyproject.toml`, `setup.cfg`, package install flow)

Before starting:

- Python 3.10 is expected in the subject
- Basic terminal usage is helpful (`python3`, passing arguments)

How it connects to the full repository:

- This is the foundation module; all later modules build on these scripting and validation skills.

## Learning Goals

- Understand list/tuple/set/dict differences
- Format values and dates in strings
- Detect and classify object types
- Handle null-like Python values
- Build CLI tools with argument validation
- Re-implement a simplified built-in function (`filter`)
- Use dictionary mappings for encoding
- Implement a generator-like progress bar
- Create a minimal installable Python package

## Folder Structure

```text
Python - 0 - Starting/
├── en.subject.pdf
└── Training Piscine Python for datascience - 0/
    ├── ex00/Hello.py
    ├── ex01/format_ft_time.py
    ├── ex02/find_ft_type.py, tester.py
    ├── ex03/NULL_not_found.py, tester.py
    ├── ex04/whatis.py
    ├── ex05/building.py
    ├── ex06/ft_filter.py, filterstring.py
    ├── ex07/sos.py
    ├── ex08/Loading.py, test.py
    └── ex09/ft_package/, test.py
```

| File / Folder | Purpose |
|---|---|
| ex00 | Modify values in basic container types and print results |
| ex01 | Format epoch time and date output |
| ex02 | Print object type categories and return fixed status value |
| ex03 | Detect NULL-like values and print matching labels |
| ex04 | CLI odd/even checker with assertion-style errors |
| ex05 | Character counting utility (upper/lower/punctuation/space/digits) |
| ex06 | Custom `ft_filter` + argument-based string filtering program |
| ex07 | Convert alphanumeric text to Morse code |
| ex08 | Custom `ft_tqdm` iterator/progress bar |
| ex09 | Minimal Python package (`ft_package`) with build metadata |

## Exercise-by-Exercise Explanation

### ex00 - Hello.py

**Path:** `Training Piscine Python for datascience - 0/ex00/Hello.py`
**Purpose:** Practice mutability and value updates in built-in containers.
**What It Does:** Updates predefined list/tuple/set/dict values and prints them.
**Important Functions / Classes:** None (script-level operations).
**Input:** None.
**Output:** Printed updated structures.
**Main Logic:** Change second/value entries -> print all containers.
**How to Run:**
```bash
python3 "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex00/Hello.py"
```
**What I Learned:** Data structure behavior (mutable vs immutable).

### ex01 - format_ft_time.py

**Path:** `.../ex01/format_ft_time.py`
**Purpose:** Learn formatting with f-strings and datetime handling.
**What It Does:** Prints epoch seconds with commas/scientific notation and current date.
**Important Functions:** `time.time()`, `datetime.now().strftime()`.
**Input:** None.
**Output:** 2 formatted lines.
**How to Run:**
```bash
python3 "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex01/format_ft_time.py"
```
**What I Learned:** Numeric/date formatting patterns.

### ex02 - find_ft_type.py + tester.py

**Path:** `.../ex02/find_ft_type.py`
**Purpose:** Type inspection and controlled output.
**What It Does:** Function `all_thing_is_obj` prints a message based on object type; returns `42`.
**Input:** Any Python object.
**Output:** Type label prints + return value.
**Main Logic:** `isinstance` chain for list/tuple/set/dict/str/other.
**How to Run:**
```bash
cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex02"
python3 tester.py
```
**Example Output:** Includes lines like `List : <class 'list'>` and final `42`.
**What I Learned:** Type checking and output contracts.

### ex03 - NULL_not_found.py + tester.py

**Path:** `.../ex03/NULL_not_found.py`
**Purpose:** Detect specific null-like values (`None`, `NaN`, `0`, empty string, `False`).
**What It Does:** Prints standardized labels and returns `0`/`1`.
**Important Function:** `NULL_not_found(object: any) -> int`.
**Input:** Any object.
**Output:** Type message and status code.
**How to Run:**
```bash
cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex03"
python3 tester.py
```
**Verification Note:** NaN check implementation appears unusual and may match more float values than intended. **This part should be verified.**
**What I Learned:** Edge-case branching and return-based status signaling.

### ex04 - whatis.py

**Path:** `.../ex04/whatis.py`
**Purpose:** CLI validation and parity checking.
**What It Does:** Reads one numeric argument and prints odd/even message.
**Input:** One integer argument.
**Output:** `I'm even.` / `I'm odd.` or assertion error text.
**How to Run:**
```bash
python3 "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex04/whatis.py" 14
```
**What I Learned:** `sys.argv` validation and exception messaging.

### ex05 - building.py

**Path:** `.../ex05/building.py`
**Purpose:** Text statistics by character class.
**What It Does:** Counts total chars, uppercase, lowercase, punctuation, spaces, digits.
**Important Functions:** `count(text)`, `main()`.
**Input:** CLI string or interactive input.
**Output:** Multi-line count summary.
**How to Run:**
```bash
python3 "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex05/building.py" "Hello World!"
```
**What I Learned:** String analysis with generator expressions.

### ex06 - ft_filter.py + filterstring.py

**Path:** `.../ex06/ft_filter.py`, `.../ex06/filterstring.py`
**Purpose:** Recreate simplified `filter` and apply to words by length.
**What It Does:** Returns words whose length is greater than `N`.
**Important Functions:** `ft_filter(function, iterable)`, lambda in `filterstring.py`.
**Input:** String + integer threshold via CLI.
**Output:** Python list of matching words.
**How to Run:**
```bash
cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex06"
python3 filterstring.py "Hello the World" 4
```
**Example Output:** `['Hello', 'World']`
**What I Learned:** List comprehensions, lambda, argument validation.

### ex07 - sos.py

**Path:** `.../ex07/sos.py`
**Purpose:** Encode text to Morse using dictionary mapping.
**What It Does:** Converts alphanumeric input and spaces into Morse tokens.
**Input:** One CLI string argument.
**Output:** Encoded Morse string separated by spaces (`/` for spaces).
**How to Run:**
```bash
python3 "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex07/sos.py" "sos 42"
```
**What I Learned:** Dictionary-driven encoding and input validation.

### ex08 - Loading.py + test.py

**Path:** `.../ex08/Loading.py`
**Purpose:** Build a tqdm-like iterator with `yield`.
**What It Does:** Iterates through range values while printing a progress bar.
**Important Function:** `ft_tqdm(lst: range)`.
**Input:** Iterable/range.
**Output:** Progress line updates in terminal.
**How to Run:**
```bash
cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex08"
python3 test.py
```
**What I Learned:** Generator behavior and stdout control.

### ex09 - ft_package + test.py

**Path:** `.../ex09/ft_package/__init__.py`
**Purpose:** First Python package creation.
**What It Does:** Exposes `count_in_list(lst, item)` and package metadata files.
**Important Files:** `pyproject.toml`, `setup.cfg`, `LICENSE`, package `README.md`.
**Input:** List + item (function call).
**Output:** Count of item occurrences.
**How to Run (local test):**
```bash
cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex09"
python3 test.py
```
**What I Learned:** Packaging structure and distribution basics.

## Important Concepts

- Variables and built-in data types
- Functions and return values
- CLI argument parsing with `sys.argv`
- Type checking with `isinstance`
- String formatting and datetime
- List comprehensions and lambda
- Dictionary mapping
- Generators and `yield`
- Basic Python packaging (`pyproject.toml`)

## Data / Control Flow

```text
CLI input / hardcoded test data
        ↓
Validation (arg count/type)
        ↓
Transformation (type check, filter, encode, count)
        ↓
Formatted print output / return status
```

## Common Errors / Edge Cases

| Case | Where It Is Handled | Behavior |
|---|---|---|
| Wrong number of CLI args | `whatis.py`, `filterstring.py`, `sos.py`, `building.py` | Prints `AssertionError` message |
| Non-integer numeric argument | `whatis.py`, `filterstring.py` | Prints error message |
| Empty/no input path | `building.py` | Prompts user for text |
| Unsupported character in Morse input | `sos.py` | Prints assertion error |
| Null-like non-matching type | `NULL_not_found.py` | Prints `Type not found` and returns `1` |

## How to Test This Module

| Test | Command | Expected Result |
|---|---|---|
| Type detection | `cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex02" && python3 tester.py` | Prints detected types and final `42` |
| Odd/even CLI | `python3 "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex04/whatis.py" -5` | Prints odd result |
| String filtering | `cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex06" && python3 filterstring.py 'Hello the World' 4` | `['Hello', 'World']` |
| Morse encoding | `python3 "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex07/sos.py" "sos"` | `... --- ...` |
| Package test | `cd "Python - 0 - Starting/Training Piscine Python for datascience - 0/ex09" && python3 test.py` | Prints count values |

## Key Takeaways

- You can build useful CLI tools with basic Python only.
- Validation and explicit error messages are essential.
- List comprehensions, lambdas, and dictionaries are core building blocks.
- Packaging a tiny utility introduces real Python project structure.
