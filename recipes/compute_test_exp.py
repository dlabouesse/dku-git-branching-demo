# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
westnileToScore_partitioned_filtered_prepared_joined = dataiku.Dataset("westnileToScore_partitioned_filtered_prepared_joined")
westnileToScore_partitioned_filtered_prepared_joined_df = westnileToScore_partitioned_filtered_prepared_joined.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_exp_df = westnileToScore_partitioned_filtered_prepared_joined_df # For this sample code, simply copy input to output


# Write recipe outputs
test_exp = dataiku.Dataset("test_exp")
test_exp.write_with_schema(test_exp_df)
