#!/usr/bin/env python3
"""
Test insta485generator with published "hello_css" input.

EECS 485 Project 1

Andrew DeOrio <awdeorio@umich.edu>
"""
import os
import shutil
import unittest
import re
import sh


def get_start_fail_str(output):
    """Return exception output string for a startup failure."""
    start_fail_str = "Failed to start insta485 generator, output: {}"
    return start_fail_str.format(output)


class TestHelloCSS(unittest.TestCase):
    """Unit tests for insta485generator with published "hello_css" input."""

    @classmethod
    def setUpClass(cls):
        """Run `insta485generator ./hello_css`.

        This function runs once before any member function unit test.
        """
        # pylint: disable=redundant-unittest-assert
        assert os.path.isdir("hello_css"), "Can't find ./hello_css dir"
        if os.path.isdir("hello_css/html"):
            shutil.rmtree("hello_css/html")
        try:
            sh.insta485generator("hello_css")
            cls.assert_str = ""
        except sh.ErrorReturnCode as error:
            output = error.stdout.decode('ascii')
            cls.assert_str = get_start_fail_str(output)

    @classmethod
    def tearDownClass(cls):
        """Clean up generated files `./hello_css/html/*`.

        This function runs once after all member function unit tests.
        """
        print(os.path.isdir("hello_css/html"))
        if os.path.isdir("hello_css/html"):
            shutil.rmtree("hello_css/html")

    def test_files(self):
        """Make sure generated files exist."""
        # pylint: disable=redundant-unittest-assert
        self.assertTrue(
            os.path.isfile("hello_css/html/index.html"),
            "Can't find hello_css/html/index.html"
        )
        self.assertTrue(
            os.path.isfile("hello_css/html/css/style.css"),
            "Can't find hello_css/html/css/style.css"
        )

    def test_index(self):
        """Diff check hello/index.html."""
        # pylint: disable=redundant-unittest-assert
        correct = '<!DOCTYPE html>\n<html lang="en">\n  <head>\n' + \
            '<title>Hello world</title>\n    <link rel="stylesheet" ' + \
            'type="text/css" href="/css/style.css">\n  </head>\n ' + \
            '<body>\n    \n    <div class="important">hello</div>\n' + \
            '\n    <div class="important">world</div>\n    \n' + \
            '</body>\n</html>'
        output_dir = "hello_css/html/"
        filename = os.path.join(output_dir, "index.html")
        with open(filename) as infile:
            student = infile.read()
        correct = re.sub(r"\s+", " ", correct)
        student = re.sub(r"\s+", " ", student)

        self.assertEqual(correct, student, "Hello_css.html content mismatch!")

    def setUp(self):
        """Verify startup was successful."""
        started_up = True
        if self.assert_str is not None and self.assert_str != '':
            started_up = False
        self.assertTrue(started_up, self.assert_str)

    def test_css_dir(self):
        """Diff check css/style.css."""
        # pylint: disable=redundant-unittest-assert
        correct = 'body {\n    background: pink;\n}\n\n\ndiv.important \
                {\n    font-weight: bold;\n    font-size: 1000%;\n}\n'
        output_dir = "hello_css/html/"
        filename = os.path.join(output_dir, "css/style.css")
        with open(filename) as infile:
            student = infile.read()
        correct = re.sub(r"\s+", " ", correct)
        student = re.sub(r"\s+", " ", student)

        self.assertEqual(correct, student)


if __name__ == "__main__":
    unittest.main(verbosity=2)
