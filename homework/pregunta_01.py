# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
from matplotlib import pyplot as plt

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    # Verificar si la carpeta 'docs' existe, si no, crearla
    if not os.path.exists("docs"):
        os.makedirs("docs", exist_ok=True)

    # Leer datos
    df = pd.read_csv("files/input/shipping-data.csv")

    # Crear figura
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("Shipping Dashboard Example", fontsize=16, fontweight="bold")

    # Gráfico 1: Shipping per Warehouse
    warehouse_counts = df["Warehouse_block"].value_counts().sort_index()
    axs[0, 0].bar(warehouse_counts.index, warehouse_counts.values, color="steelblue")
    axs[0, 0].set_title("Shipping per Warehouse")
    axs[0, 0].set_xlabel("Warehouse block")
    axs[0, 0].set_ylabel("Shipment Count")

    # Gráfico 2: Average Customer Rating por modo de envío
    avg_rating = df.groupby("Mode_of_Shipment")["Customer_rating"].mean().sort_values()
    axs[0, 1].barh(avg_rating.index, avg_rating.values, color="darkorange")
    axs[0, 1].set_title("Average Customer Rating")
    axs[0, 1].set_xlabel("Rating")
    axs[0, 1].set_xlim(1, 5)

    # Gráfico 3: Mode of shipment (donut)
    mode_counts = df["Mode_of_Shipment"].value_counts()
    wedges, texts = axs[1, 0].pie(mode_counts.values, labels=mode_counts.index, colors=["#1f77b4", "#ff7f0e", "#2ca02c"], startangle=90, wedgeprops=dict(width=0.4))
    axs[1, 0].set_title("Mode of shipment")

    # Gráfico 4: Shipped Weight Distribution
    axs[1, 1].hist(df["Weight_in_gms"], bins=10, color="darkorange", edgecolor="black")
    axs[1, 1].set_title("Shipped Weight Distribution")
    axs[1, 1].set_xlabel("Weight (gms)")
    axs[1, 1].set_ylabel("Frequency")

   
    # Guardar cada gráfico individualmente en la carpeta 'docs'
    plt.tight_layout()
    axs[0, 0].figure.set_size_inches(10, 8)
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.savefig("docs/mode_of_shipment.png")
    plt.savefig("docs/average_customer_rating.png")
    plt.savefig("docs/weight_distribution.png")
    plt.close(fig)  # Cerrar la figura para liberar memoria
    # Guardar el dashboard completo como una imagen
    fig.savefig("docs/shipping_dashboard.png", bbox_inches='tight')
   
    

    # Crear HTML simple para mostrar el dashboard
    html_content = """
    <html>
        <head>
            <title>Shipping Dashboard Example</title>
        </head>
        <body>
            <h1>Shipping Dashboard Example</h1>
            <img src="shipping_dashboard.png" alt="Dashboard">
        </body>
    </html>
    """
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)  

  
    print("Dashboard creado en la carpeta 'docs'.")
    return True

if __name__ == "__main__":
    pregunta_01()
      

