import pandas as pd


class ParseCSV:

    def __init__(self, filename: str) -> None:
        file = pd.read_csv(fr'uploads\\{filename}')
        df = pd.DataFrame(file)

        # Set first column as index
        support_df = df.set_index(df.iloc[:, 0])

        # Strip non numerical columns
        self.support_df = support_df.select_dtypes('number')

    def get_series(self) -> dict:
        series_dict = {}

        for _column in self.support_df.columns:
            series_dict[_column] = self.support_df[_column]

        return series_dict
