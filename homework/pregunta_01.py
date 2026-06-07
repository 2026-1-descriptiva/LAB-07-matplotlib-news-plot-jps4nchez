# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    colors = {
        "Television": "dimgray",
        "Newspaper": "gray",
        "Internet": "tab:blue",
        "Radio": "lightgray",
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    line_widths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2,
    }

    df = pd.read_csv(
        "files/input/news.csv",
        index_col=0,
    )

    plt.figure()

    for column in df.columns:
        plt.plot(
            df[column],
            color=colors[column],
            label=column,
            zorder=zorder[column],
            linewidth=line_widths[column],
        )

    plt.title(
        "How people get their news",
        fontsize=16,
    )

    ax = plt.gca()

    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    start_year = df.index[0]
    end_year = df.index[-1]

    for column in df.columns:

        plt.scatter(
            start_year,
            df[column][start_year],
            color=colors[column],
            zorder=zorder[column],
        )

        plt.text(
            start_year - 0.2,
            df[column][start_year],
            f"{column} {df[column][start_year]}%",
            ha="right",
            va="center",
            color=colors[column],
        )

        plt.scatter(
            end_year,
            df[column][end_year],
            color=colors[column],
            zorder=zorder[column],
        )

        plt.text(
            end_year + 0.2,
            df[column][end_year],
            f"{df[column][end_year]}%",
            ha="left",
            va="center",
            color=colors[column],
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha="center",
    )

    plt.tight_layout()

    output_directory = "files/plots"
    os.makedirs(output_directory, exist_ok=True)

    plt.savefig(
        os.path.join(
            output_directory,
            "news.png",
        )
    )
    