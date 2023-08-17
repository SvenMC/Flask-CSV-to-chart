import pandas as pd


class ParseCSV:

    def __init__(self) -> None:
        file = pd.read_csv(r'playground\nvchart.csv')
        df = pd.DataFrame(file)

