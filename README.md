# FDE Package Sorter

A small Python utility to dispatch packages to the correct stack in FDE’s robotic automation factory, based on volume and mass constraints.

# Project Structure
```bash
.
├── main.py           # Entry point & Package implementation
├── test_package.py   # Unit tests for each predicate & overall sort()
└── README.md         # This documentation
```
---

## Table of Contents

- [Objective](#objective)  
- [Rules](#rules)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Running Tests](#running-tests)
- [Implementation Details](#implementation-details)

---

## Objective

Implement a function to dispatch packages into one of three stacks:

The function sort(width, height, length, mass) should consider
(units are centimeters for the dimensions and kilogram for the mass).
This function must return a string: the name of the stack where the package should go. 

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

This supports a robotic arm that must handle or reject packages based on their dimensions and mass.

---

## Rules

### Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

- **Bulky** if:
  - Volume (W × H × L) ≥ 1 000 000 cm³  
  - **Or** any single dimension ≥ 150 cm  

- **Heavy** if:
  - Mass ≥ 20 kg  

---

## Installation

1. Clone the repository:
    ```bash
        git clone https://github.com/your-username/thoughtful-package-sorter.git
        cd fdeTechnicalScreen
    ```
2. Create and activate a virtual environment:
    ```
        python3 -m venv .venv
        source .venv/bin/activate   # macOS/Linux
        .\.venv\Scripts\activate    # Windows
    ```
3. Install any dependencies (none beyond the standard library)

# Usage
- Run the script below:

    ```bash
   python main.py 
    ```
# Running Tests
- This project uses Python’s built-in unittest framework.
    ```bash
      python -m unittest -v tests/test_package.py
    ```

# Implementation Details
- Constants: defined at top of main.py (VOL, DIMENSION, KILO)
- Package class:
- Predicates: is_bulky(), is_heavy(), rejected(), special(), standard()
- Dispatch logic: sort()
- No side-effects: sort() returns a string without mutating object state. 
- Test coverage: every method and edge-case boundary is covered.
