import pandas as pd

file = "cities.csv"
df = pd.read_csv(file)
html = df.to_html(classes='utf8')