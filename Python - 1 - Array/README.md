# Python - 1 - Array

This module focuses on array manipulation and image processing using NumPy-style operations and plotting libraries.

## Module Overview

What this module teaches:

- Working with numeric arrays and shapes
- Slicing 2D data
- Loading image files into arrays
- Cropping, grayscale conversion, and transpose logic
- Color filters and channel-based operations

Connection to full repository:

- Extends Python basics into scientific/data formats
- Prepares you for CSV/DataFrame work in Module 2

Prerequisites:

- Comfortable with Python lists, loops, and functions
- Basic understanding of indexing

## Learning Goals

- Compute values vectorially (BMI)
- Slice arrays safely with input checks
- Understand image array shape `(H, W, C)`
- Perform manual transformations without relying on forbidden shortcuts
- Display transformed arrays/images

## Folder Structure

```text
Python - 1 - Array/
├── en.subject (1).pdf
└── Training Piscine Python for datascience- 1/
    ├── ex00/give_bmi.py, tester.py
    ├── ex01/array2D.py, tester.py
    ├── ex02/load_image.py, landscape.jpg
    ├── ex03/load_image.py, zoom.py, animal.jpeg
    ├── ex04/load_image.py, rotate.py, animal.jpeg
    └── ex05/load_image.py, pimp.py, landscape.jpg
```

| File / Folder | Purpose |
|---|---|
| ex00 | BMI computation and threshold evaluation |
| ex01 | 2D array slicing and shape reporting |
| ex02 | Generic image loading function |
| ex03 | Zoom/crop image + grayscale output |
| ex04 | Manual rotation/transpose exercise |
| ex05 | Apply image color filters |

## Exercise-by-Exercise Explanation

### ex00 - give_bmi.py

**Path:** `Training Piscine Python for datascience- 1/ex00/give_bmi.py`
**Purpose:** Compute BMI from height/weight lists and compare against limit.
**Important Functions:** `give_bmi`, `apply_limit`.
**Input:** Lists of numeric values and integer limit.
**Output:** List of BMI values and list of booleans.
**Main Logic:** Validate types/length -> NumPy conversion -> compute BMI -> compare to limit.
**How to Run:**
```bash
python3 "Python - 1 - Array/Training Piscine Python for datascience- 1/ex00/tester.py"
```
**Example Output:**
`[22.507863455018317, 29.0359168241966] <class 'list'>` then `[False, True]`
**What I Learned:** Vector-style operations + defensive checks.

### ex01 - array2D.py

**Path:** `.../ex01/array2D.py`
**Purpose:** Slice a 2D array and report shape before/after slicing.
**Important Function:** `slice_me(family, start, end)`.
**Input:** 2D list + slice bounds.
**Output:** Truncated 2D list.
**Main Logic:** Validate 2D structure and element types -> convert to array -> slice -> print shapes.
**How to Run:**
```bash
python3 "Python - 1 - Array/Training Piscine Python for datascience- 1/ex01/tester.py"
```
**What I Learned:** Shape-aware slicing and data validation.

### ex02 - load_image.py

**Path:** `.../ex02/load_image.py`
**Purpose:** Load JPG/JPEG into array and print shape.
**Important Function:** `ft_load(path: str)`.
**Input:** Image path string.
**Output:** NumPy array + shape print.
**Main Logic:** Type check path -> `PIL.Image.open` -> `np.array` conversion -> return array.
**How to Run:**
```bash
cd "Python - 1 - Array/Training Piscine Python for datascience- 1/ex02"
python3 load_image.py
```
**What I Learned:** Bridge between image file and numeric tensor.

### ex03 - zoom.py (+ load_image.py)

**Path:** `.../ex03/zoom.py`
**Purpose:** Crop central image region and convert to grayscale.
**Important Functions:** `zoom(image)`, `ft_load` (module local).
**Input:** `animal.jpeg`.
**Output:** Printed old/new shapes + displayed grayscale image.
**Main Logic:** Validate size -> compute crop bounds -> crop -> grayscale weighted sum -> display with axes.
**How to Run:**
```bash
cd "Python - 1 - Array/Training Piscine Python for datascience- 1/ex03"
python3 zoom.py
```
**What I Learned:** Cropping and channel reduction.

### ex04 - rotate.py (+ load_image.py)

**Path:** `.../ex04/rotate.py`
**Purpose:** Rotate image 90 degrees counterclockwise using manual logic.
**Important Functions:** `rotate_90_ccw`, `zoom`.
**Input:** `animal.jpeg`.
**Output:** New shape and rotated display.
**Main Logic:** Optional zoom stage -> build new array -> nested loop remapping pixels.
**How to Run:**
```bash
cd "Python - 1 - Array/Training Piscine Python for datascience- 1/ex04"
python3 rotate.py
```
**What I Learned:** Manual transpose/rotation mapping.

### ex05 - pimp.py (+ load_image.py)

**Path:** `.../ex05/pimp.py`
**Purpose:** Apply multiple color filters without changing image shape.
**Important Functions / Classes:** `ft_invert`, `ft_red`, `ft_green`, `ft_blue`, `ft_grey`.
**Input:** Image array (`landscape.jpg`).
**Output:** Filtered images displayed in subplot grid.
**Main Logic:** Load image -> normalize shape -> apply per-filter channel rules -> plot.
**How to Run:**
```bash
cd "Python - 1 - Array/Training Piscine Python for datascience- 1/ex05"
python3 pimp.py
```
**Verification Note:** Subject names expected file as `pimp_image.py`, repository uses `pimp.py`. **This part should be verified.**
**What I Learned:** Channel operations and visualization.

## Important Concepts

- NumPy arrays and shape metadata
- Slicing and index boundaries
- RGB vs grayscale representation
- Manual pixel remapping
- Plot rendering with matplotlib
- Input type and dimension validation

## Data / Control Flow

```text
Image/File input
    ↓
Load to NumPy array
    ↓
Validate shape/type
    ↓
Transform (slice / rotate / filter)
    ↓
Print shape/data + display plot
```

## Common Errors / Edge Cases

| Case | Where It Is Handled | Behavior |
|---|---|---|
| Non-list / invalid numeric lists | `ex00/give_bmi.py` | Raises `TypeError` / `ValueError` |
| Different list lengths | `ex00/give_bmi.py` | Raises `ValueError` |
| Invalid 2D array structure | `ex01/array2D.py` | Raises type/value errors |
| Missing image file | `ex02..ex05/load_image.py` | Raises file-related error |
| Too-small image for crop | `ex03/zoom.py` | Raises `ValueError` |

## How to Test This Module

| Test | Command | Expected Result |
|---|---|---|
| BMI test | `python3 "Python - 1 - Array/Training Piscine Python for datascience- 1/ex00/tester.py"` | BMI list and threshold boolean list |
| 2D slice test | `python3 "Python - 1 - Array/Training Piscine Python for datascience- 1/ex01/tester.py"` | Shape prints and sliced array |
| Load image | `cd "Python - 1 - Array/Training Piscine Python for datascience- 1/ex02" && python3 load_image.py` | Shape + array print |
| Zoom view | `cd "Python - 1 - Array/Training Piscine Python for datascience- 1/ex03" && python3 zoom.py` | New sliced shape and grayscale display |
| Rotate view | `cd "Python - 1 - Array/Training Piscine Python for datascience- 1/ex04" && python3 rotate.py` | Transposed/rotated output |

## Key Takeaways

- Arrays are a core abstraction for data and images.
- Shape management is critical before transformations.
- Even simple loops can implement geometric image operations.
- Validation makes numeric/image code more reliable.
