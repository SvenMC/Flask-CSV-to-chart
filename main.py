from flask import Flask, send_from_directory

from chartgen import BuildChart, ParseCSV
from utils import UniqueFileValidator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'uploads'
ALLOWED_EXTENSIONS = ['.csv']


@app.route("/")
def readcsv():
    return "<h1>hello</>"


@app.route("/chartgen/build")
def chart_build():
    unique_filename = UniqueFileValidator.validate_uploads()
    data = ParseCSV(
        filename=unique_filename
    )

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
