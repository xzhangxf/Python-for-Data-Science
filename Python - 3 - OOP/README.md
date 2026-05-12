# Python - 3 - OOP

This module focuses on object-oriented programming: abstract classes, inheritance, multiple inheritance, properties, and class design for vector operations.

## Module Overview

What this module teaches:

- Building abstract and concrete classes
- Inheritance relationships and family models
- Property-based encapsulation in multiple inheritance
- Operator overloading for vector-scalar calculations
- Static/class-style vector operations without object instantiation

How it connects to the full repository:

- Moves from data scripts to reusable object models
- Introduces architecture choices useful in larger codebases

Prerequisites:

- Python functions and module imports
- Basic understanding of classes

## Learning Goals

- Define and use abstract base classes
- Implement inherited attributes and methods
- Use properties (`@property`) for controlled mutation
- Overload arithmetic operators
- Use static-like method style for utility calculations

## Folder Structure

```text
Python - 3 - OOP/
├── en.subject (1).pdf
└── Training Piscine Python for datascience- 3/
    ├── ex00/S1E9.py, tester.py, test_abstract.py
    ├── ex01/S1E9.py, S1E7.py, tester.py
    ├── ex02/S1E9.py, S1E7.py, DiamondTrap.py, tester.py
    ├── ex03/ft_calculator.py, tester.py
    └── ex04/ft_calculator.py, tester.py
```

| File / Folder | Purpose |
|---|---|
| ex00 | Abstract base class (`Character`) + `Stark` implementation |
| ex01 | `Baratheon` and `Lannister` inherited families |
| ex02 | `King` class using multiple inheritance + properties |
| ex03 | Vector-scalar calculator using overloaded operators |
| ex04 | Static vector operations: dot/add/subtract |

## Exercise-by-Exercise Explanation

### ex00 - S1E9.py (+ tester.py, test_abstract.py)

**Path:** `Training Piscine Python for datascience- 3/ex00/S1E9.py`
**Purpose:** Build abstract `Character` and concrete `Stark`.
**Important Classes:** `Character(ABC)`, `Stark(Character)`.
**Input:** Constructor values `first_name`, optional `is_alive`.
**Output:** Object state changes via `die()`.
**Main Logic:** Abstract `__str__` prevents direct `Character` instantiation.
**How to Run:**
```bash
cd "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex00"
python3 tester.py
python3 test_abstract.py
```
**Example Result:** `test_abstract.py` raises expected `TypeError`.
**What I Learned:** Abstract class contracts and inheritance basics.

### ex01 - S1E7.py (+ inherited S1E9.py)

**Path:** `.../ex01/S1E7.py`
**Purpose:** Create instantiable inherited family classes.
**Important Classes:** `Baratheon`, `Lannister`.
**Important Methods:** `__str__`, `__repr__`, classmethod `create_lannister`.
**Input:** First name and alive state.
**Output:** Family identity representation and inherited behavior (`die`).
**How to Run:**
```bash
cd "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex01"
python3 tester.py
```
**What I Learned:** Class attributes, representation methods, classmethod factory.

### ex02 - DiamondTrap.py (+ S1E7/S1E9 copies)

**Path:** `.../ex02/DiamondTrap.py`
**Purpose:** Multiple inheritance with controlled attribute updates.
**Important Class:** `King(Baratheon, Lannister)`.
**Important Methods:** `eyes` and `hairs` properties + set/get methods.
**Input:** King name and optional alive state.
**Output:** Mutable trait values (`eyes`, `hairs`).
**How to Run:**
```bash
cd "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex02"
python3 tester.py
```
**What I Learned:** C3 linearization context and property encapsulation.

### ex03 - ft_calculator.py

**Path:** `.../ex03/ft_calculator.py`
**Purpose:** Vector-scalar arithmetic through operator overloading.
**Important Class:** `calculator`.
**Important Methods:** `__add__`, `__sub__`, `__mul__`, `__truediv__`.
**Input:** List of numbers + scalar values.
**Output:** Printed transformed vectors.
**How to Run:**
```bash
cd "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex03"
python3 tester.py
```
**What I Learned:** Operator overloading and scalar broadcast style logic.

### ex04 - ft_calculator.py

**Path:** `.../ex04/ft_calculator.py`
**Purpose:** Dot product and vector arithmetic without instance creation.
**Important Methods:** `dotproduct`, `add_vec`, `sous_vec` (staticmethod style).
**Input:** Two vectors of same size.
**Output:** Printed dot/add/sub vectors.
**How to Run:**
```bash
python3 "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex04/tester.py"
```
**Example Output:**
`Dot product is: 56`
`Add Vector is : [7.0, 14.0, 5.0]`
`Sous Vector is: [3.0, 6.0, -1.0]`
**What I Learned:** Method design for class-level utilities.

## Important Concepts

- `abc.ABC` and abstract methods
- Inheritance and subclass specialization
- Multiple inheritance + properties
- Class/static method patterns
- Operator overloading in Python classes

## Data / Control Flow

```text
Initialize class with state
       ↓
Call methods / overloaded operators
       ↓
Apply transformations or state mutation
       ↓
Print resulting vectors or attributes
```

## Common Errors / Edge Cases

| Case | Where It Is Handled | Behavior |
|---|---|---|
| Instantiating abstract class | `ex00/test_abstract.py` | Raises `TypeError` |
| Division by zero | `ex03/ft_calculator.py` | Prints explicit error message |
| Inheritance attribute override consistency | `ex02/DiamondTrap.py` | Uses property-backed fields |
| Vector size mismatch | ex04 subject says identical sizes assumed | No extra handling by design |

## How to Test This Module

| Test | Command | Expected Result |
|---|---|---|
| Abstract check | `cd "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex00" && python3 test_abstract.py` | `TypeError` for abstract class instantiation |
| Family classes | `cd "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex01" && python3 tester.py` | Family dict and method outputs |
| King properties | `cd "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex02" && python3 tester.py` | Eye/hair updates reflected |
| Scalar calculator | `cd "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex03" && python3 tester.py` | Printed transformed vectors |
| Dot product calculator | `python3 "Python - 3 - OOP/Training Piscine Python for datascience- 3/ex04/tester.py"` | Dot/add/sub outputs |

## Key Takeaways

- Abstract classes enforce implementation contracts.
- Inheritance helps organize shared behavior cleanly.
- Properties are useful when multiple inheritance becomes complex.
- Operator overloading can make numeric classes expressive.
