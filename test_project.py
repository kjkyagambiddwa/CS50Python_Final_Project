import pytest
import pandas as pd
from unittest.mock import patch
import project


@pytest.fixture
def sample_csv(tmp_path):
    path = tmp_path / "project.csv"
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob'],
        'Students_no': ['2300710001', '2300710002'],
        'Math': [80, 60],
        'English': [75, 65],
        'Math_lec_att': [90, 70],
        'Eng_lec_att': [85, 75],
    })
    df.to_csv(path, index=False)
    return path


@pytest.fixture(autouse=True)
def override_filename(monkeypatch, sample_csv):
    # Patch the FILENAME variable in project to point to the temp CSV file for all tests
    monkeypatch.setattr(project, "FILENAME", str(sample_csv))


@patch('builtins.input', side_effect=[
    '2',  # number of students to add
    'Alice', '2300710001', '80', '75', '90', '85',
    'Bob', '2300710002', '60', '65', '70', '75',
])

def test_add_students(mock_input, sample_csv):
    project.add_students()
    df = pd.read_csv(sample_csv)
    # Check if both Alice and Bob exist after addition
    assert 'Alice' in df['Name'].values
    assert 'Bob' in df['Name'].values
    # Check that there are at least 2 records
    assert len(df) >= 2


@patch('builtins.input', side_effect=[
    'Alice', '2300710001', 'y',  # delete student called Alice confirmation
])
def test_delete_student(mock_input, sample_csv):
    # Run delete_student functions which should delete Alice
    project.delete_student()
    df = pd.read_csv(sample_csv)
    # Alice should be gone, Bob should remain
    assert 'Alice' not in df['Name'].values
    assert 'Bob' in df['Name'].values


@patch('builtins.input', side_effect=[
    '1',  # sort by Name
    'a',  # in ascending
    '1',  # descending order
    'b',  # in descending
    '5',  # back from view_students menu
])
def test_view_students(mock_input):
    # No exceptions and expected flow
    project.view_students()


@patch('builtins.input', side_effect=[
    '1',  # mean
    '3',  # for both
    '9',  # immediately exit analyze_statistics
])
def test_analyze_statistics_exit(mock_input):
    # The function runs and exits without errors
    project.analyze_statistics()
