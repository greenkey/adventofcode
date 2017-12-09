import unittest
from stream_processing import get_stream_score

class TestStreamScore(unittest.TestCase):

    def test_all(self):
        testcases = [
            ("{}", 1, 0),
            ("{{{}}}", 6, 0),
            ("{{},{}}", 5, 0),
            ("{{{},{},{{}}}}", 16, 0),
            ("{<a>,<a>,<a>,<a>}", 1, 4),
            ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9, 8),
            ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9, 0),
            ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3, 17),
            ("{<<<<>}", 1, 3),
            ("{<<<<}{>}", 1, 5),
        ]

        for test_string, expected_score, expected_removed in testcases:
            score, removed = get_stream_score(test_string)
            self.assertEqual(expected_score, score, msg=f"string: {test_string}")
            self.assertEqual(expected_removed, removed, msg=f"string: {test_string}")


if __name__ == '__main__':
    unittest.main()
