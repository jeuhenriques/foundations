"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import load_data, clean_data, save_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    pt_life_expectancy_data = load_data(file_input_name='eu_life_expectancy_raw.tsv',path="data")

    eu_life_expectancy_raw = load_data(
        file_input_name='eu_life_expectancy_raw.tsv',
        path="data"
    )

    pt_life_expectancy = clean_data(
        data=eu_life_expectancy_raw,
        region='PT'
    )

    save_data(
        data=pt_life_expectancy,
        file_output_name='pt_life_expectancy.csv',
        path="data"
    )

    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
