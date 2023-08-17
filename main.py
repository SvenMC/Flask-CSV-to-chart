from chartgen import BuildChart, ParseCSV
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def readcsv():
    ParseCSV()

    return "<h1>hello</>"


# @app.route("/chartgen/build")
# def hello_world():
#     chart = BuildChart()

#     chart.build()
#     return send_from_directory(
#         directory=r'assets\charts', path=f'{chart.val}.png'
#     )
