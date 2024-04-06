import numpy as np
import matplotlib.pyplot as plt

#PV Ertrag 12 Werte in kWh fuer 12 h pro Tag: 2 0 3 7 3 8 4 6 5 0 1 2 als 1 x 12 Matrix
Ertrag = np.array([2,0,3,7, 3, 8, 4, 6, 5,0,1,2])
Ertrag_ges = np.sum(Ertrag)

#Strom Verbrauch des Verbrauchers in kWh, 12 Werte fuer 12 Stunden 
#Erstellen von 3 Segmenten mit zuf�lligen Werten in den angegebenen Bereichen, mit morgens niedrigem, mittags und Abends etwas h�herem Verbrauch 
segment1 = np.random.randint(0, 7, size=3)  # 3 Werte zwischen 0 und 6
segment2 = np.random.randint(2, 16, size=6) # 6 Werte zwischen 2 und 15
segment3 = np.random.randint(0, 11, size=3) # 3 Werte zwischen 4 und 15

# Kombinieren der zuf�lligen Segmente zu einer einzigen einzeiligen Matrix
Stromverbrauch = np.concatenate([segment1, segment2, segment3])
Stromverbrauch_ges = np.sum(Stromverbrauch)

#Eigenverbrauch berechnen
Eigenverbrauch = np.minimum (Ertrag,Stromverbrauch)
Eigenverbrauch_ges = np.sum(Eigenverbrauch)

#Autarkiegrad berechnen
Autarkie = Eigenverbrauch_ges / Stromverbrauch_ges

# Erstellen eines Arrays mit den Positionen der Werte f�r die X-Achse
x_positionen = np.arange(len(Ertrag))

# Plotten der Matrizen
plt.plot(x_positionen, Ertrag, label='Ertrag', marker='o')
plt.plot(x_positionen, Stromverbrauch, label='Stromverbrauch', marker='x')
plt.plot(x_positionen, Eigenverbrauch, label='Eigenverbrauch', marker='^')

# Hinzuf�gen von Titel und Legende
plt.legend()

# Anzeigen des Plots und des Autrakiegrads
plt.show()
print(Autarkie)
