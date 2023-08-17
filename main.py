from chartgen import BuildChart
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/chartgen/build")
def hello_world():
    chart = BuildChart()

    chart.build()
    return send_from_directory(
        directory=r'assets\charts', path=f'{chart.val}.png'
    )
