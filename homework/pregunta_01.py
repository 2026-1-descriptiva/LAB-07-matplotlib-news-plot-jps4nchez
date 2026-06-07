# pylint: disable=import-outside-toplevel
import os

import matplotlib.pyplot as plt
import pandas as pd

INPUT_FILE = "files/input/news.csv"
OUTPUT_PATH = "files/plots/news.png"

MEDIA_COLUMNS = ["Television", "Newspaper", "Internet", "Radio"]

COLORS = {
    "Television": "dimgray",
    "Newspaper":  "steelblue",
    "Internet":   "tomato",
    "Radio":      "mediumseagreen",
}
MARKERS = {
    "Television": "o",
    "Newspaper":  "s",
    "Internet":   "^",
    "Radio":      "D",
}


def pregunta_01() -> None:
    """
    Genera una grafica de lineas mostrando el porcentaje de personas
    que obtienen noticias por cada medio (Television, Newspaper, Internet, Radio)
    entre 2001 y 2010, y la guarda en files/plots/news.png.
    """
    df = pd.read_csv(INPUT_FILE, index_col=0)

    fig, ax = plt.subplots(figsize=(9, 5))

    for col in MEDIA_COLUMNS:
        ax.plot(
            df.index,
            df[col],
            color=COLORS[col],
            marker=MARKERS[col],
            linewidth=2,
            markersize=7,
            label=col,
        )

    ax.set_title(
        "Porcentaje de personas que obtienen noticias\npor medio de comunicacion",
        fontsize=13,
        pad=14,
    )
    ax.set_xlabel("Anio", fontsize=11)
    ax.set_ylabel("Porcentaje (%)", fontsize=11)
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.index, rotation=45)
    ax.set_ylim(0, 100)
    ax.legend(title="Medio", fontsize=10, title_fontsize=10)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    plt.savefig(OUTPUT_PATH, dpi=150)
    plt.close(fig)