import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from main import play_game


class TestMysteryIsland(unittest.TestCase):

    def test_starting_energy(self):
        output = StringIO()

        with patch("builtins.input", side_effect=["Alex", "6"]):
            with redirect_stdout(output):
                play_game()

        self.assertIn("Energy: 5", output.getvalue())

    def test_invalid_menu_choice(self):
        output = StringIO()

        with patch("builtins.input", side_effect=["Alex", "9", "6"]):
            with redirect_stdout(output):
                play_game()

        self.assertIn(
            "Invalid choice. Please enter a number between 1 and 6.",
            output.getvalue()
        )

    def test_invalid_jungle_choice(self):
        output = StringIO()

        with patch("builtins.input", side_effect=["Alex", "1", "9", "5", "6"]):
            with redirect_stdout(output):
                play_game()

        self.assertIn("Invalid jungle choice. No energy lost.", output.getvalue())
        self.assertIn("Remaining energy: 5", output.getvalue())
        self.assertNotIn("Rope", output.getvalue())

    def test_invalid_cave_choice(self):
        output = StringIO()

        with patch("builtins.input", side_effect=["Alex", "2", "9", "5", "6"]):
            with redirect_stdout(output):
                play_game()

        self.assertIn("Invalid cave choice. No energy lost", output.getvalue())
        self.assertIn("Remaining energy: 5", output.getvalue())
        self.assertNotIn("Lantern", output.getvalue())

    def test_invalid_bridge_choice(self):
        output = StringIO()

        with patch(
            "builtins.input",
            side_effect=["Alex", "1", "1", "3", "9", "5", "6"]
        ):
            with redirect_stdout(output):
                play_game()

        self.assertIn("Invalid bridge choice. No energy lost.", output.getvalue())
        self.assertIn("Remaining energy: 4", output.getvalue())

    def test_winning_path(self):
        output = StringIO()

        with patch(
            "builtins.input",
            side_effect=["Alex", "1", "1", "3", "1", "2", "1", "4"]
        ):
            with redirect_stdout(output):
                play_game()

        self.assertIn("CONGRATULATIONS! YOU WIN!", output.getvalue())


if __name__ == "__main__":
    unittest.main()

	
