import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("modul_03_extract_and_transform/daten2.csv")
df["Umsatz"] = pd.to_numeric(df["Umsatz"], errors="coerce")

df.plot(kind="bar", x="Name",y="Umsatz", color="skyblue", rot=0)

plt.show()
