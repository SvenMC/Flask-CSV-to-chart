from flask import Flask, send_from_directory, request, abort
import os

from chartgen import BuildChart, ParseCSV
from utils import UniqueFileValidator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'uploads/'
ALLOWED_EXTENSIONS = ['.csv']


@app.route("/chartgen/build", methods=['POST'])
def chart_build():
    if 'chart' not in request.files:
        abort(400)

    file = request.files['chart']
    unique_filename = UniqueFileValidator().validate_upload()
    file.name = unique_filename
    file.save(
        os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    )

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

# TODO Add endpoint that parses pre-build series
