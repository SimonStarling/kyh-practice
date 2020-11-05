from Övning36.pwstrength import compute_strength


def test_password_with_length_11_gives_1_points():
    pw = "1" * 11
    assert compute_strength(pw) == 1


def test_password_with_length_9_gives_0_points():
    pw = "1" * 9
    assert compute_strength(pw) == 0


def test_password_with_specialchar_gives_1_points():
    pw = "!!"
    assert compute_strength(pw) == 0


def test_password_bug():
    pw = "!" * 10
    assert compute_strength(pw) == 0
