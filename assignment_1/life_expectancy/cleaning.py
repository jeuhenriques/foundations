"""Module clean data"""
import pandas as pd
import argparse
import pathlib

def clean_data(region="PT") -> None:
    """
    :param region:
    """
    path = pathlib.Path(__file__).parent / 'data'
    file_input_name="eu_life_expectancy_raw.tsv"
    file_output_name="pt_life_expectancy.csv"
    # read data
    data = pd.read_csv(path/file_input_name, sep='\t')
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
    data = data[data["region"] == region]
    # save data
    data.to_csv(path/file_output_name, index=False)

    return None

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()
    clean_data(region=args.region)
