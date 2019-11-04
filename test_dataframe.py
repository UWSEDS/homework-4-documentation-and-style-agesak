"""
This module implements a class that tests various attributes of a dataframe
The tests are as follows:
1. Do all of the columns have values of the correct type?
2. Are there NaNs in any of the columns?
3. Does the dataframe have at least one row?
"""
import sys
import importlib
import warnings
sys.path.append("C:/Users/agesak/Documents/MPH/MPH Courses/CSE 583")

# set globals
HW2 = importlib.import_module(
    "homework-2-python-functions-and-modules-agesak.pronto_checks")


class TestDataframe():
    """
    A class to test various attributes of a dataframe
    ...

    Methods
    -----------
    test_col_types(): Checks that all columns have
                    values of the corect type.
    test_nans(): Checks for NaN values
    test_row(): Verify that the dataframe has at least one row.

    """

    def __init__(self):
        """
        Sets the attributes of the class

        Attributes
        -----------------
        df : pd.Dataframe
            pandas dataframe read in from a csv
        type_dict: dictionary
                  dictionary that maps df column to the expected type
        """
        self.df = HW2.read_in_data(
            "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD")
        self.type_dict = {"trip_id": "int64",
                          "starttime": "object",
                          "stoptime": "object",
                          "bikeid": "object",
                          "tripduration": "float64",
                          "from_station_name": "object",
                          "to_station_name": "object",
                          "from_station_id": "object",
                          "to_station_id": "object",
                          "usertype": "object",
                          "gender": "object",
                          "birthyear": "int64"}

    def test_col_types(self):
        """
        * Warns the user if column is of incorrect type
        """
        for col in self.type_dict:
            expected = self.df[f"{col}"].dtype == self.type_dict[f"{col}"]
            if not expected:
                warnings.warn("Column {} is not of the expected type. "
                              "It is {}".format(col, self.df[col].dtype))

    def test_nans(self):
        """
        * Warns the user if there are any NA's in a column
        """
        for col in list(self.df):
            if self.df[col].isnull().any():
                warnings.warn(f"There are NAs in the {col} column")

    def test_row(self):
        """
        * Will break (give an AssertionError) if this condition is not met
        """
        assert len(self.df) >= 1, "DataFrame does not have at least one row"
