
import unittest
import os
from helper_functions.helpers import *


class HeaderSetTest(unittest.TestCase):
    def test_empty_data(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        target_file = os.path.join(
            currentDir, "test_samples", "test_empty.json")
        expect_result = {}
        actual_result = get_header_set(json_data(target_file))
        self.assertEqual(expect_result, actual_result)

    def test_single_row_data(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        target_file = os.path.join(
            currentDir, "test_samples", "test_single_row.json")
        expect_result = {"view_grades", "view_classes"}
        actual_result = get_header_set(json_data(target_file))
        self.assertEqual(expect_result, actual_result)

    def test_multiple_row_data(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        target_file = os.path.join(
            currentDir, "test_samples", "test_multiple_row.json")
        expect_result = {"view_classes",	"view_grades",	"delete_grades",	"add_classes",
                         "change_grades",	"change_classes",	"add_grades",	"delete_classes"}
        actual_result = get_header_set(json_data(target_file))
        self.assertEqual(expect_result, actual_result)

class ExportResult(unittest.TestCase):
    # test on empty file would be unneccesary for this case,I just skip it.

    def test_single_row_data(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        target_file =  os.path.join(
            currentDir, "test_samples", "test_single_row.json")
        expect_result = [{'': 'student1', 'view_grades': 1, 'view_classes': 1}]
        actual_result = get_data_dict(target_file)
        self.assertEqual(expect_result, actual_result)
        
    def test_multiple_row_data(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        target_file =  os.path.join(
            currentDir, "test_samples", "test_multiple_row.json")
        expect_result = [{'': 'student1', 'view_grades': 1, 'view_classes': 1, 'delete_classes': 0, 'add_grades': 0, 'change_grades': 0, 'delete_grades': 0, 'add_classes': 0, 'change_classes': 0}, {'': 'student2', 'view_grades': 1, 'view_classes': 1, 'delete_classes': 0, 'add_grades': 0, 'change_grades': 0, 'delete_grades': 0, 'add_classes': 0, 'change_classes': 0}, {'': 'teacher', 'view_classes': 1, 'add_grades': 1, 'change_grades': 1, 'delete_grades': 1, 'view_grades': 1, 'add_classes': 0, 'delete_classes': 0, 'change_classes': 0}, {'': 'principle', 'view_classes': 1, 'delete_classes': 1, 'view_grades': 1, 'add_classes': 1, 'change_classes': 1, 'add_grades': 0, 'change_grades': 0, 'delete_grades': 0}]
        actual_result = get_data_dict(target_file)
        self.assertEqual(expect_result, actual_result)
if __name__ == '__main__':
    unittest.main()
