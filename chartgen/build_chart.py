import matplotlib.pyplot as plt
import mplcyberpunk  # noqa: F401 # used in plt.style
import random
import os


class BuildChart:

    asset_path = "assets/charts/"

    def __init__(self) -> None:
        self.val = random.randint(111111111111, 999999999999)
        self.chart_type = None
        self.full_path = None

    def build(self):

        duration_dict = {
            "example1": 50,
            "example2": 400,
            "example3": 150
        }

        self.generate_chart(duration_dict, self.chart_type)

    def generate_chart(self, duration_dict, title):

        # Title font dict
        title_dict = {
            'fontsize': 18,
            'fontweight': 'bold',
            'color': 'white',
            'verticalalignment': 'baseline'
        }

        names = list(duration_dict.keys())
        values = list(duration_dict.values())

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
            f'{title}',
            loc='center',
            fontdict=title_dict,
            pad=40
        )
        ax.set_xlabel('Time (Hours)', fontdict=title_dict, labelpad=40)
        ax.set_yticklabels(names, fontsize=12, fontweight='bold')

        self.full_path = rf'{self.asset_path}{self.val}.png'
        plt.savefig(self.full_path)

    def delete_chart(self):
        os.remove(self.full_path)
