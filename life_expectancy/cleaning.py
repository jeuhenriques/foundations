"""Module clean data"""
import argparse
import pathlib
import pandas as pd
from typing import Any

def load_data(file_input_name: str, path: str ) -> pd.DataFrame:
    """load_data from file_input_name and path

    Args:
        file_input_name (str): name naming
        path (str): path

    Returns:
        pd.DataFrame: dataframe return
    """
    path = pathlib.Path(__file__).parent / path
    # read data
    data = pd.read_csv(path / file_input_name, sep='\t')

    return data


def clean_data(data: pd.DataFrame, region: str = 'PT' ) -> pd.DataFrame:
    """AI is creating summary for clean_data

    Args:
        data (pd.DataFrame): [description]
        region (str, optional): [description]. Defaults to 'PT'.

    Returns:
        pd.DataFrame: [description]
    """
    # slice data frame column to split
    split_column = data.columns[0]
    # slip column by comma
    new_columns = split_column.split(",")
    # slip one column in new column
    data[new_columns] = data[split_column].str.split(',', expand=True)
    # drop unused column
    data = data.drop(columns=split_column)
    # unpivot data by new_column
    data = data.melt(id_vars=new_columns, var_name='year', value_name="value")
    # Convert the column to float
    data["value"] = data['value'].str.extract(r'(\d+.\d+)').astype('float')
    # Convert the column to int
    data["year"] = data['year'].astype('int')
    # Filter is not na in column value
    data = data[~data["value"].isna()]
    # Rename column to region
    data = data.rename(columns={data.columns[3]: "region"})
    # Filter region column by region parameter
    data_cleaned = data[data["region"] == region]

    return data_cleaned

def save_data(data: pd.DataFrame, file_output_name: str, path: Any) ->  None:
    """AI is creating summary for save_data

    Args:
        data (pd.DataFrame): [description]
        path (str): [description]
        file_output_name (str): [description]

    Returns:
        [type]: [description]
    """
    # save data
    data.to_csv(path / file_output_name, index=False)

if __name__=='__main__': # pragma: no cover

    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()

    eu_life_expectancy_raw = load_data(
        file_input_name='eu_life_expectancy_raw.tsv',
        path="data"
    )

    pt_life_expectancy = clean_data(
        data=eu_life_expectancy_raw,
        region=args.region
    )

    save_data(
        data=pt_life_expectancy,
        file_output_name='pt_life_expectancy.csv',
        path="data"
    )
