from chartgen import BuildChart, ParseCSV
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def readcsv():
    support_df = ParseCSV().support_df
    # print(support_df)

    return "<h1>hello</>"


@app.route("/chartgen/build")
def chart_build():
    data = ParseCSV()

    for _series in data.get_series():

        chart = BuildChart()

        chart.build(
            dataframe=_series
        )
    return send_from_directory(
        directory=r'assets\charts', path=f'{chart.val}.png'
    )
