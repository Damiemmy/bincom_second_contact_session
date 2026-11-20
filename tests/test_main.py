import os
import tempfile
import unittest

from main import (
    bubble_sort,
    binary_search,
    extract_baby_names,
    read_and_extract_full_name,
)


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLE_HTML = os.path.join(
    PROJECT_DIR, "tests", "fixtures", "sample_baby2008.html"
)


class AssignmentTests(unittest.TestCase):
    def test_full_name_is_split_into_three_parts(self):
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", delete=False
        ) as file:
            file.write("Damisa Rufai Emmanuel")
            file_path = file.name

        try:
            self.assertEqual(
                read_and_extract_full_name(file_path),
                ("Damisa", "Rufai", "Emmanuel"),
            )
        finally:
            os.remove(file_path)

    def test_regex_extracts_both_name_columns_from_html(self):
        names = extract_baby_names(SAMPLE_HTML)
        self.assertEqual(
            names,
            ["Jacob", "Emma", "Michael", "Isabella", "Owen", "Anne-Marie"],
        )

    def test_bubble_sort_orders_names_without_changing_original(self):
        original = ["Zara", "Amara", "David"]
        sorted_names = bubble_sort(original)
        self.assertEqual(sorted_names, ["Amara", "David", "Zara"])
        self.assertEqual(original, ["Zara", "Amara", "David"])

    def test_binary_search_finds_name_case_insensitively(self):
        sorted_names = ["Amara", "David", "Emma", "Jacob"]
        self.assertEqual(binary_search(sorted_names, "eMmA"), 2)

    def test_binary_search_returns_minus_one_when_missing(self):
        sorted_names = ["Amara", "David", "Emma", "Jacob"]
        self.assertEqual(binary_search(sorted_names, "Olivia"), -1)


if __name__ == "__main__":
    unittest.main()
