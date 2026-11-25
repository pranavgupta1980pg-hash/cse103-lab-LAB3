"""Unit tests for src/main.py."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import greet


class TestGreet(unittest.TestCase):
    """Basic smoke test for the lab entry point."""

    def test_greet(self) -> None:
        self.assertEqual(greet("CSE103"), "Hello, CSE103!")


if __name__ == "__main__":
    unittest.main()
