"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
# pylint: disable=import-outside-toplevel
import os
import pandas as pd
import matplotlib.pyplot as plt

# Constantes fuera de la funcion: mas facil de mantener y reutilizar
MEDIA_STYLES = {
    "Television": {"color": "dimgray",  "zorder": 1, "linewidth": 2},
    "Newspaper":  {"color": "gray",     "zorder": 1, "linewidth": 2},
    "Internet":   {"color": "tab:blue", "zorder": 2, "linewidth": 4},
    "Radio":      {"color": "lightgray","zorder": 1, "linewidth": 2},
}

INPUT_PATH  = "files/input/news.csv"
OUTPUT_PATH = "files/plots/news.png"


def _load_data(path: str) -> pd.DataFrame:
    """Carga y valida el CSV de noticias."""
    df = pd.read_csv(path, index_col=0)
    missing = set(MEDIA_STYLES) - set(df.columns)
    if missing:
        raise ValueError(f"Columnas faltantes en el CSV: {missing}")
    return df


def _style_axes(ax: plt.Axes) -> None:
    """Elimina los bordes y el eje Y del grafico."""
    for spine in ("top", "left", "right"):
        ax.spines[spine].set_visible(False)
    ax.yaxis.set_visible(False)


def _annotate_endpoints(ax: plt.Axes, df: pd.DataFrame) -> None:
    """Dibuja puntos y etiquetas en el inicio y fin de cada serie."""
    start, end = df.index[0], df.index[-1]

    for col in df.columns:
        style = MEDIA_STYLES[col]
        color  = style["color"]
        zorder = style["zorder"]

        for year, ha, x_offset, label_fmt in [
            (start, "right", -0.2, f"{col} {df[col][start]}%"),
            (end,   "left",  +0.2, f"{df[col][end]}%"),
        ]:
            ax.scatter(year, df[col][year], color=color, zorder=zorder)
            ax.text(
                year + x_offset,
                df[col][year],
                label_fmt,
                ha=ha,
                va="center",
                color=color,
            )


def pregunta_01() -> None:
    """
    Genera el grafico 'How people get their news' y lo guarda en disco.
    Referencia: https://youtu.be/qVdwpxG_JpE
    """
    df = _load_data(INPUT_PATH)

    fig, ax = plt.subplots()  # Mejor que plt.figure() + plt.gca()

    for col in df.columns:
        style = MEDIA_STYLES[col]
        ax.plot(
            df[col],
            color=style["color"],
            label=col,
            zorder=style["zorder"],
            linewidth=style["linewidth"],
        )

    ax.set_title("How people get their news", fontsize=16)
    _style_axes(ax)
    _annotate_endpoints(ax, df)

    ax.set_xticks(df.index)
    ax.set_xticklabels(df.index, ha="center")

    fig.tight_layout()

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    fig.savefig(OUTPUT_PATH)
    plt.close(fig)  # Libera memoria; importante en entornos de CI


