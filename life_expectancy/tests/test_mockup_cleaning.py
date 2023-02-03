"""Tests for the cleaning module"""
import pandas as pd
import pytest
from life_expectancy.cleaning import clean_data
from life_expectancy.tests.fixtures.tear_up import data_raw,data_expect


@pytest.fixture
def fixture_raw():
    """AI is creating summary for fixture_raw

    Returns:
        [type]: [description]
    """

    return pd.DataFrame(data_raw())

@pytest.fixture
def fixture_expect():
    """AI is creating summary for fixture_expect

    Returns:
        [type]: [description]
    """

    return pd.DataFrame(data_expect())

def clean_data_mockup(df_fixture_raw):
    """AI is creating summary for clean_data_mockup

    Args:
        df_fixture_raw ([type]): [description]

    Returns:
        [type]: [description]
    """

    pt_life_expectancy_mock = clean_data(
        data=df_fixture_raw,
        region='PT'
    )
    return pt_life_expectancy_mock

def test_clean_data(fixture_raw, fixture_expect):
    """Run the `clean_data` function and compare the output to the expected output"""

    result  = clean_data_mockup(fixture_raw)
    pd.testing.assert_frame_equal(
        result.reset_index(drop=True), fixture_expect.reset_index(drop=True)
    )
