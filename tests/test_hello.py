#!/usr/bin/env python3
"""
Test insta485generator with published "hello" input.

EECS 485 Project 1

Andrew DeOrio <awdeorio@umich.edu>
"""
import os
import shutil
import unittest
import re
import sh


START_FAIL_STR = "Failed to start insta485 generator, output: {}"


def get_start_fail_str(output):
    """Return exception output string for a startup failure."""
    return START_FAIL_STR.format(output)


class TestHello(unittest.TestCase):
    """Unit tests for insta485generator with published "hello" input."""

    @classmethod
    def setUpClass(cls):
        """Run `insta485generator hello`.

        This function runs once before any member function unit test.
        """
        # pylint: disable=redundant-unittest-assert
        assert os.path.isdir("hello"), "Can't find hello dir"
        if os.path.isdir("hello/html"):
            shutil.rmtree("hello/html")
        try:
            sh.insta485generator("hello")
            cls.assert_str = ""
        except sh.ErrorReturnCode as error:
            output = error.stdout.decode('ascii')
            cls.assert_str = get_start_fail_str(output)

    @classmethod
    def tearDownClass(cls):
        """Clean up generated files `hello/html/*`.

        This function runs once after all member function unit tests.
        """
        if os.path.isdir("hello/html"):
            shutil.rmtree("hello/html")

    def test_files(self):
        """Make sure generated files exist."""
        # pylint: disable=redundant-unittest-assert
        self.assertTrue(
            os.path.isfile("hello/html/index.html"),
            "Can't find hello/html/index.html"
        )

    def setUp(self):
        """Verify startup was successful."""
        started_up = True
        if self.assert_str is not None and self.assert_str != '':
            started_up = False
        self.assertTrue(started_up, self.assert_str)

    def test_index(self):
        """Diff check hello/index.html."""
        # pylint: disable=redundant-unittest-assert
        correct = "<!DOCTYPE html>\n" + \
            "<html lang=\"en\">\n" + \
            "<head><title>Hello world</title></head>\n" + \
            "<body>\n\n" + \
            "hello\n\n" + \
            "world\n\n" + \
            "</body>\n" + \
            "</html>"
        output_dir = "hello/html/"
        filename = os.path.join(output_dir, "index.html")
        with open(filename) as infile:
            student = infile.read()
        correct = re.sub(r"\s+", " ", correct)
        student = re.sub(r"\s+", " ", student)
        self.assertEqual(correct, student, "Hello.html content mismatch!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
