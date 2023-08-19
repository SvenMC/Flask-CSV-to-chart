import matplotlib.pyplot as plt
import mplcyberpunk  # noqa: F401 # used in plt.style
import random
import os
import pandas as pd


class BuildChart:

    asset_path = "assets/charts/"

    def __init__(self) -> None:
        self.val = random.randint(111111111111, 999999999999)
        self.chart_type = None
        self.full_path = None

    def build(self, series: pd.Series):
        # TODO add some logic here to pull out 0 values and
        # -  return if no positive values.

        series = series.sort_values()

        self.generate_chart(series, self.chart_type)

    def generate_chart(self, series: pd.Series, title):

        # Title font dict
        title_dict = {
            'fontsize': 18,
            'fontweight': 'bold',
            'color': 'white',
            'verticalalignment': 'baseline'
        }

        names = series.index
        values = series.values

        # Styling
        plt.style.use('cyberpunk')
        colors = ["C0", "C1", "C2", "C3", "C4"]

        # Figure Size
        fig, ax = plt.subplots(figsize=(21, 9))

        # Horizontal Bar Plot
        ax.barh(names, values, color=colors, ec='black', lw=0.4)

        # Add x, y gridlines
        ax.grid(
            color='grey',
            linestyle='-',
            linewidth=0.5,
            alpha=0.9,
            axis='x'
        )

        # Add Plot Title
        ax.set_title(
            f'{series.name}',
            loc='center',
            fontdict=title_dict,
            pad=40
        )
        ax.set_xlabel(f'{series.name}', fontdict=title_dict, labelpad=40)
        ax.set_yticklabels(names, fontsize=12, fontweight='bold')

        self.full_path = rf'{self.asset_path}{self.val}.png'
        plt.savefig(self.full_path)

    def delete_chart(self):
        os.remove(self.full_path)
