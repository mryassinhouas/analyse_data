'''import pandas as pd
import matplotlib.pyplot as plt


# Lire le fichier CSV
try:
    data = pd.read_csv("ventes.csv")

except:
    print("Erreur : le fichier ventes.csv est introuvable")
    exit()


# Afficher les données
print("===== DONNEES =====")
print(data)


# Ajouter une colonne Total
data["Total"] = data["Quantite"] * data["Prix"]


print("\n===== VENTES =====")
print(data)


# Calcul du chiffre d'affaire total
chiffre_affaire = data["Total"].sum()

print("\nChiffre d'affaire total :", chiffre_affaire)


# Calcul des quantités vendues par produit
resultat = data.groupby("Produit")["Quantite"].sum()


print("\n===== PRODUITS VENDUS =====")
print(resultat)


# Trouver le produit le plus vendu
produit_max = resultat.idxmax()

print("\nProduit le plus vendu :", produit_max)


# Afficher un graphique
resultat.plot(kind="bar")

plt.title("Quantité vendue par produit")
plt.xlabel("Produit")
plt.ylabel("Quantité")

plt.show()'''
'''import pandas as pd
import matplotlib.pyplot as plt


# Lire le fichier CSV
try:
    data = pd.read_csv("ventes.csv")

except:
    print("Erreur : le fichier ventes.csv est introuvable")
    exit()


# Ajouter le total des ventes
data["Total"] = data["Quantite"] * data["Prix"]


# Afficher les données
print("===== DONNEES =====")
print(data)


# Regrouper les ventes par produit
produits = data.groupby("Produit")["Quantite"].sum()

print("\n===== QUANTITE PAR PRODUIT =====")
print(produits)


# Produit le plus vendu
print("\nProduit le plus vendu :", produits.idxmax())


# ===== FENETRE GRAPHIQUE =====

plt.figure(figsize=(8, 5))

# Créer une courbe pour chaque produit
for produit in data["Produit"].unique():

    produit_data = data[data["Produit"] == produit]

    plt.plot(
        produit_data.index,
        produit_data["Quantite"],
        marker="o",
        label=produit
    )


# Titre et informations
plt.title("Evolution des ventes par produit")
plt.xlabel("Numéro de vente")
plt.ylabel("Quantité vendue")

# Afficher le nom de chaque courbe
plt.legend()

# Afficher la grille
plt.grid(True)

# Ouvrir la fenêtre
plt.show()'''
--------------------------------------------------------------------------------------------------version 2 with courbe and charts------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt


# Lire le fichier CSV
try:
    data = pd.read_csv("ventes.csv")

except:
    print("Erreur : le fichier ventes.csv est introuvable")
    exit()


# Afficher les données
print("===== DONNEES =====")
print(data)


# ==========================
# FENETRE 1 : DIAGRAMME
# ==========================

quantite_produit = data.groupby("Produit")["Quantite"].sum()

plt.figure("Diagramme des ventes", figsize=(7,5))

quantite_produit.plot(kind="bar")

plt.title("Quantité vendue par produit")
plt.xlabel("Produit")
plt.ylabel("Quantité")

plt.grid(True)

plt.show()


# ==========================
# FENETRE 2 : COURBE
# ==========================

plt.figure("Courbe des ventes", figsize=(7,5))


for produit in data["Produit"].unique():

    produit_data = data[data["Produit"] == produit]

    plt.plot(
        produit_data.index,
        produit_data["Quantite"],
        marker="o",
        label=produit
    )


plt.title("Evolution des ventes par produit")
plt.xlabel("Numéro de vente")
plt.ylabel("Quantité")

plt.legend()

plt.grid(True)

plt.show()
