import unittest

from app import DEFAULT_MESSAGE, format_message, main


class AppTest(unittest.TestCase):
    def test_default_message(self) -> None:
        self.assertEqual(
            format_message(),
            f"ChatGPT Remote Test: {DEFAULT_MESSAGE}",
        )

    def test_custom_message(self) -> None:
        self.assertEqual(
            format_message("S22"),
            "ChatGPT Remote Test: S22",
        )

    def test_main_success(self) -> None:
        self.assertEqual(main(["S22", "연동"]), 0)


if __name__ == "__main__":
    unittest.main()

