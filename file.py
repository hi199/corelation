from re import X
from _plotly_utils.basevalidators import ColorlistValidator
import plotly.express as px
import csv
with open("cups of coffee vs hours of sleep.csv", newline='')as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "Coffee in ml",y="sleep in hours",color="week")
    fig.show()
    def getDataSource(data_path):
    coffe_in_ml=[]
    sleep_in_hours=[]
    with open(data_path)as csv_file:
        df = csv.DictReader(csv_file)
        for row in df: