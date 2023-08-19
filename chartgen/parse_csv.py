import pandas as pd


class ParseCSV:

    def __init__(self) -> None:
        file = pd.read_csv(r'playground\nvchart.csv')
        df = pd.DataFrame(file)

        # Set first column as index
        support_df = df.set_index(df.iloc[:, 0])

        # Strip non numerical columns
        self.support_df = support_df.select_dtypes('number')
