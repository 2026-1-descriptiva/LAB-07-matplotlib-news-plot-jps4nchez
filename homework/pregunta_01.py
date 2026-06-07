"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import matplotlib.pyplot as plt
import numpy as np


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    # Crear el directorio si no existe
    output_dir = "files/plots"
    os.makedirs(output_dir, exist_ok=True)

    # Generar datos ficticios
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Crear la gráfica
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="Seno", color="blue")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.title("Gráfica de onda senoidal")
    plt.legend()
    plt.grid()

    # Guardar la imagen
    output_path = os.path.join(output_dir, "news.png")
    plt.savefig(output_path)
    plt.close()

    print(f"Gráfico guardado en: {output_path}")