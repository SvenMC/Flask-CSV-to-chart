from chartgen import BuildChart, ParseCSV
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def readcsv():
    return "<h1>hello</>"


@app.route("/chartgen/build")
def chart_build():
    data = ParseCSV()

    paths = []
    for _series in data.get_series().values():
        chart = BuildChart()

        path = chart.build(
            series=_series
        )
        if path:
            paths.append(path)

    return send_from_directory(
        directory=r'assets\charts', path=f'{paths[0]}.png'
    )
