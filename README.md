# Second Python Assignment

This project demonstrates Python file handling, the `os` module, regular expressions, a manually implemented sorting algorithm, and a manually implemented search algorithm.

## Project contents

```text
second_assignment/
├── main.py
├── full_name.txt
├── baby2008.html          # Add the original file supplied with the assignment
├── README.md
├── .gitignore
└── tests/
    ├── test_main.py
    └── fixtures/
        └── sample_baby2008.html
```

## Requirements

- Python 3.8 or newer
- No third-party Python packages are required.
- The program uses the standard-library `os` and `re` modules.

## Important: add the supplied dataset

Place the original instructor-supplied **`baby2008.html`** file in the same folder as `main.py`. Keep its filename exactly as `baby2008.html`.

The program reads the HTML table directly. It does not require you to copy the names into a separate text file. The sample HTML under `tests/fixtures/` is only a small test fixture; it is not a replacement for the complete assignment dataset.

## How to run on Windows

Open Command Prompt in the project folder. You do not need to create a virtual environment or install packages for this assignment, but you may use one if required by your course.

Run:

```cmd
python main.py
```

When prompted, enter a baby name to search for. The search is case-insensitive. For example, `olivia` and `Olivia` are treated as the same search term.

## What the program does

1. **File handling:** reads `full_name.txt` and separates the three name parts using `split()`.
2. **OS module:** displays the current working directory with `os.getcwd()` and the full path of the running Python script with `os.path.abspath(__file__)`.
3. **Regex extraction:** reads `baby2008.html` and uses regular expressions to capture the male and female name cells from each ranked table row. Both columns are combined into one list.
4. **Bubble Sort:** sorts the extracted names alphabetically using comparisons and swaps written in this project. It does not call `list.sort()` or `sorted()`.
5. **Binary Search:** searches the sorted list by repeatedly checking its middle element. It does not use `bisect` or another built-in search algorithm.

## Run the tests

The included tests use Python's built-in `unittest` framework and a small HTML fixture. They check name extraction, sorting, searching, and full-name splitting.

```cmd
python -m unittest discover -s tests -v
```

## Algorithm notes

- Bubble Sort has a worst-case time complexity of **O(n²)**.
- Binary Search has a time complexity of **O(log n)**, provided the list is sorted first.

## Data source acknowledgement

The `baby2008.html` dataset is the 2008 Popular Baby Names table attributed in the supplied HTML to the U.S. Social Security Administration. The project uses the provided file as input and does not modify its source data.
