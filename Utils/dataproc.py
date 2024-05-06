import os
import json
import numpy as np 
import pandas as pd
import polars as pl
import seaborn as sns 
import matplotlib as mpl
import scipy.stats as st
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def drop_col_null(df, percent_null):
    bad = []
    for col in df.columns:
        null_percentages = df[col].null_count() / df[col].len() 
        if null_percentages >= percent_null:
            bad.append(col)
    new_df = df.drop(bad)
    return new_df