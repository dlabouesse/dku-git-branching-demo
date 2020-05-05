# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
weather_partitioned_filtered_prepared_joined_prepared = dataiku.Dataset("weather_partitioned_filtered_prepared_joined_prepared")
weather_partitioned_filtered_prepared_joined_prepared_df = weather_partitioned_filtered_prepared_joined_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_tmp_df = weather_partitioned_filtered_prepared_joined_prepared_df # For this sample code, simply copy input to output

#test


# Write recipe outputs
test_tmp = dataiku.Dataset("test-tmp")
test_tmp.write_with_schema(test_tmp_df)
