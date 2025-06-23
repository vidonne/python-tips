### Module 1 project

# Create 5 charts using the provided datasets

# load packages
import pandas as pd
import matplotlib.pyplot as plt
from pyodide.http import open_url

# data
url_storms = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/storms/storms.csv"
df_storms = pd.read_csv(open_url(url_storms))

url_footprint = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/footprint/footprint.csv"
df_footprint = pd.read_csv(open_url(url_footprint))

url_mario = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/mariokart/mariokart.csv"
df_mario = pd.read_csv(open_url(url_mario))