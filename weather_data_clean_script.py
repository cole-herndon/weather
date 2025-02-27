#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import argparse
import sys

def clean_data(df):
    """Function to clean the weather data."""
    # columns we want to keep
    columns_to_keep = ['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'DATE', 'PRCP', 'PRCP_ATTRIBUTES', 'SNWD', 'SNWD_ATTRIBUTES',
                   'SNOW','SNOW_ATTRIBUTES','TAVG', 'TAVG_ATTRIBUTES','TMAX', 'TMAX_ATTRIBUTES', 'TMIN', 'TMIN_ATTRIBUTES', 'TOBS','TOBS_ATTRIBUTES', 'WESD', 
                   'WESD_ATTRIBUTES']
    df = df[columns_to_keep]

    # Separate year, month, and day from the DATE column
    df[['Year', 'Month', 'Day']] = df['DATE'].str.split('-', expand=True)

    # Convert year, month, and day to integers
    df['Year'] = df['Year'].astype(int)
    df['Month'] = df['Month'].astype(int)
    df['Day'] = df['Day'].astype(int)

    # Convert DATE column to datetime
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Convert elevation from meters to feet and round to the nearest foot
    df['ELEVATION'] = (df['ELEVATION'] * 3.28084).round()

    return df

def main():
    parser = argparse.ArgumentParser(description="Clean weather data from a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("-o", "--output", default="historical_data/cleaned_data.csv",
                        help="Path to the output cleaned CSV file (default: historical_data/cleaned_data.csv)")
    args = parser.parse_args()

    try:
        # Read the CSV file
        df = pd.read_csv(args.input_file)

        # Clean the data
        cleaned_df = clean_data(df)

        # Save the cleaned data
        cleaned_df.to_csv(args.output, index=False)
        print(f"Cleaned data saved to {args.output}")

    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
