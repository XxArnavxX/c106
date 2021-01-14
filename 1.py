import plotly.express as px
import csv

with open('./1.csv') as file1:
    df = csv.DictReader(file1)
    figure1 = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
    figure1.show()