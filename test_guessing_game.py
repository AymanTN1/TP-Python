from guessing_game import compare_guess


def test_compare_guess_small():
    assert compare_guess(3, 5) == "small"


def test_compare_guess_big():
    assert compare_guess(10, 2) == "big"


def test_compare_guess_correct():
    assert compare_guess(7, 7) == "correct"
