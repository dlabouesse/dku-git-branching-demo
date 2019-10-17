# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
westnileToScore_partitioned_filtered_prepared_joined_scored = dataiku.Dataset("westnileToScore_partitioned_filtered_prepared_joined_scored")
westnileToScore_partitioned_filtered_prepared_joined_scored_df = westnileToScore_partitioned_filtered_prepared_joined_scored.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

rfegetge_df = westnileToScore_partitioned_filtered_prepared_joined_scored_df # For this sample code, simply copy input to output

print hello

# Write recipe outputs
rfegetge = dataiku.Dataset("rfegetge")
rfegetge.write_with_schema(rfegetge_df)
