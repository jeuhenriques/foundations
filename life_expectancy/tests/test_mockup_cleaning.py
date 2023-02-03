"""Tests for the cleaning module"""
import pandas as pd
import pytest
from life_expectancy.cleaning import load_data, clean_data, save_data
from . import OUTPUT_DIR


class DataRaw:
    data = {
        'unit,sex,age,geo\time': ['YR,F,Y1,AL','YR,F,Y1,AL','YR,F,Y1,PT'],
        '2021': ['79.4','79.6','79.6'],
        '2022': ['79.4','79.6','79.6'],
        '2023': ['83.2 ','79.6','79.6']
    }

class DataExpect:
    data = {
        'unit': ['YR','YR','YR'],
        'sex': ['F','F','F'],
        'age': ['Y1','Y1','Y1'],
        'region': ['PT','PT','PT'],
        'year': [2021,2022,2023],
        'value': [79.6,79.6,79.6]
    }

@pytest.fixture
def df_fixture_raw():
    df_raw = pd.DataFrame(DataRaw.data)
    return df_raw

@pytest.fixture
def df_fixture_expect():
    df_expect = pd.DataFrame(DataExpect.data)
    return df_expect
    
def clean_data_mockup(df):
    pt_life_expectancy_mock = clean_data(
        data=df,
        region='PT'
    )
    return pt_life_expectancy_mock

def test_clean_data(df_fixture_raw, df_fixture_expect):
    """Run the `clean_data` function and compare the output to the expected output"""

    result  = clean_data_mockup(df_fixture_raw)
    print(result.head())

    print(df_fixture_expect.head())
    pd.testing.assert_frame_equal(
        result.reset_index(drop=True), df_fixture_expect.reset_index(drop=True)
    )
