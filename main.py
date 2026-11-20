"""Second Python assignment: file handling, regex, sorting, and searching."""

import os
import re


# Keep the assignment input files beside this Python script.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FULL_NAME_FILE = os.path.join(BASE_DIR, "full_name.txt")
BABY_NAMES_HTML_FILE = os.path.join(BASE_DIR, "baby2008.html")


# Match a complete row in the 2008 baby-names HTML table.
# The first captured group is the male name; the second is the female name.
BABY_NAME_ROW_PATTERN = re.compile(
    r"<tr\b[^>]*>\s*"
    r"<td\b[^>]*>\s*\d+\s*</td>\s*"
    r"<td\b[^>]*>\s*([^<]+?)\s*</td>\s*"
    r"<td\b[^>]*>\s*([^<]+?)\s*</td>\s*"
    r"</tr>",
    re.IGNORECASE | re.DOTALL,
)

# Accept alphabetic names, including names containing an apostrophe or hyphen.
BABY_NAME_PATTERN = re.compile(r"^[A-Za-z]+(?:[-'][A-Za-z]+)*$")


def read_and_extract_full_name(file_path):
    """Read a three-part name and return first, middle, and last names."""
    with open(file_path, "r", encoding="utf-8") as file:
        full_name = file.read().strip()

    name_parts = full_name.split()
    if len(name_parts) != 3:
        raise ValueError(
            "full_name.txt must contain exactly three parts: first, middle, and last name."
        )

    first_name = name_parts[0]
    middle_name = name_parts[1]
    last_name = name_parts[2]
    return first_name, middle_name, last_name


def extract_baby_names(file_path):
    """Extract male and female baby names from baby2008.html using regular expressions.

    Each matching data row contains a rank, a male name, and a female name.
    The returned list combines both name columns.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    matching_rows = BABY_NAME_ROW_PATTERN.findall(html_content)
    baby_names = []

    for male_name, female_name in matching_rows:
        male_name = male_name.strip()
        female_name = female_name.strip()

        if BABY_NAME_PATTERN.fullmatch(male_name):
            baby_names.append(male_name)

        if BABY_NAME_PATTERN.fullmatch(female_name):
            baby_names.append(female_name)

    if not baby_names:
        raise ValueError(
            "No baby names were extracted. Check that baby2008.html is the original "
            "2008 names table and has not been changed."
        )

    return baby_names


def bubble_sort(names):
    """Return an alphabetically sorted copy using Bubble Sort.

    This function deliberately does not use list.sort() or sorted().
    """
    result = names.copy()
    length = len(result)

    for pass_number in range(length - 1):
        swapped = False

        for index in range(length - pass_number - 1):
            if result[index].casefold() > result[index + 1].casefold():
                result[index], result[index + 1] = (
                    result[index + 1],
                    result[index],
                )
                swapped = True

        # If no values were swapped, the list is already sorted.
        if not swapped:
            break

    return result


def binary_search(sorted_names, target):
    """Return the index of target, or -1 when target is not present.

    The input list must already be sorted alphabetically.
    """
    left = 0
    right = len(sorted_names) - 1
    search_for = target.casefold()

    while left <= right:
        middle = (left + right) // 2
        current_name = sorted_names[middle].casefold()

        if current_name == search_for:
            return middle
        if current_name < search_for:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main():
    """Run each part of the assignment in sequence."""
    print("=" * 56)
    print("             SECOND PYTHON ASSIGNMENT")
    print("=" * 56)

    # 1. Display the working directory and the full path of this script.
    print("\n1. FILE LOCATION (os MODULE)")
    print("Current working directory:", os.getcwd())
    print("Python script path       :", os.path.abspath(__file__))

    # 2. Read the full name and separate it into three parts.
    print("\n2. FULL NAME EXTRACTION")
    try:
        first, middle, last = read_and_extract_full_name(FULL_NAME_FILE)
    except (FileNotFoundError, ValueError) as error:
        print("Could not process full_name.txt:", error)
        return

    print("First name :", first)
    print("Middle name:", middle)
    print("Last name  :", last)

    # 3. Extract both male and female names from the supplied HTML file.
    print("\n3. BABY NAME EXTRACTION USING REGEX")
    try:
        baby_names = extract_baby_names(BABY_NAMES_HTML_FILE)
    except FileNotFoundError:
        print("The file baby2008.html was not found.")
        print("Place the original instructor-supplied baby2008.html beside main.py.")
        return
    except ValueError as error:
        print("Could not extract baby names:", error)
        return

    print("Total names extracted:", len(baby_names))
    print("First 10 extracted names:", ", ".join(baby_names[:10]))

    # 4. Sort the extracted names using the Bubble Sort algorithm.
    print("\n4. ALPHABETICAL SORTING (BUBBLE SORT)")
    sorted_names = bubble_sort(baby_names)
    print("Total names sorted:", len(sorted_names))
    print("First 20 sorted names:", ", ".join(sorted_names[:20]))

    # 5. Search the sorted names using the Binary Search algorithm.
    print("\n5. BABY NAME SEARCH (BINARY SEARCH)")
    target = input("Enter a baby name to search for: ").strip()

    if not target:
        print("No search name was entered.")
        return

    position = binary_search(sorted_names, target)
    if position != -1:
        print(
            "{} was found at position {} in the sorted list.".format(
                sorted_names[position], position + 1
            )
        )
    else:
        print("{} was not found in the baby names file.".format(target))


if __name__ == "__main__":
    main()
