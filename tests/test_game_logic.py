from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# BUG FIX #1 TEST: Verify dynamic range respects difficulty selection
def test_easy_difficulty_range():
    # Easy difficulty should return range 1-20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_difficulty_range():
    # Normal difficulty should return range 1-100
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_difficulty_range():
    # Hard difficulty should return range 1-200
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200

def test_invalid_difficulty_defaults_to_normal():
    # Invalid difficulty should default to Normal range (1-100)
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100

# BUG FIX #2 TEST: Verify proper numeric comparison without type conversion bugs
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_numeric_comparison_edge_case():
    # BUG FIX #2: Ensure integer comparisons work correctly without type issues
    outcome, message = check_guess(1, 100)
    assert outcome == "Too Low"
    
def test_numeric_comparison_high_edge_case():
    # BUG FIX #2: Ensure integer comparisons work correctly without type issues
    outcome, message = check_guess(100, 1)
    assert outcome == "Too High"


def test_parse_guess_rejects_float_string():
    # BUG FIX #13 TEST: Float input should not be silently truncated.
    ok, value, err = parse_guess("3.9")
    assert ok is False
    assert value is None
    assert "not a number" in err.lower()


def test_parse_guess_accepts_integer_string_with_spaces():
    ok, value, err = parse_guess(" 42 ")
    assert ok is True
    assert value == 42
    assert err is None


def test_score_penalty_is_symmetric_for_misses():
    # BUG FIX #10 TEST: Miss penalties should be the same for high/low outcomes.
    assert update_score(0, "Too High", 1) == -5
    assert update_score(0, "Too Low", 2) == -5


def test_score_win_formula_without_extra_penalty():
    # BUG FIX #11 TEST: Attempt 1 should award 90 points (100 - 10 * 1)
    assert update_score(0, "Win", 1) == 90
