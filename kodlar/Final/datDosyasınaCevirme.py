import pickle

data = {
    "Turkey": {"Region": "Asia", "Population (Millions)": 81.6, "Area (Square Kilometers)": 302535},
    "United States": {"Region": "North America", "Population (Millions)": 331.0, "Area (Square Kilometers)": 9833517},
    "Brazil": {"Region": "South America", "Population (Millions)": 209.3, "Area (Square Kilometers)": 8515767},
    "India": {"Region": "Asia", "Population (Millions)": 1380.0, "Area (Square Kilometers)": 3287263},
    "South Africa": {"Region": "Africa", "Population (Millions)": 59.3, "Area (Square Kilometers)": 1220817},
    "Australia": {"Region": "Australia/Oceania", "Population (Millions)": 25.5, "Area (Square Kilometers)": 7692024},
    "France": {"Region": "Europe", "Population (Millions)": 67.1, "Area (Square Kilometers)": 551695},
    "Canada": {"Region": "North America", "Population (Millions)": 38.0, "Area (Square Kilometers)": 9976140},
    "China": {"Region": "Asia", "Population (Millions)": 1444.0, "Area (Square Kilometers)": 9596961},
    "Russia": {"Region": "Europe", "Population (Millions)": 146.6, "Area (Square Kilometers)": 17098242},
    "Mexico": {"Region": "North America", "Population (Millions)": 126.2, "Area (Square Kilometers)": 1964375},
    "Argentina": {"Region": "South America", "Population (Millions)": 44.0, "Area (Square Kilometers)": 1068302},
    "Germany": {"Region": "Europe", "Population (Millions)": 83.2, "Area (Square Kilometers)": 357022},
    "Japan": {"Region": "Asia", "Population (Millions)": 125.5, "Area (Square Kilometers)": 377975},
    "Nigeria": {"Region": "Africa", "Population (Millions)": 206.1, "Area (Square Kilometers)": 923768},
    "Saudi Arabia": {"Region": "Asia", "Population (Millions)": 34.2, "Area (Square Kilometers)": 2149690},
    "United Kingdom": {"Region": "Europe", "Population (Millions)": 67.0, "Area (Square Kilometers)": 243610},
    "Indonesia": {"Region": "Asia", "Population (Millions)": 273.5, "Area (Square Kilometers)": 1904569},
    "Egypt": {"Region": "Africa", "Population (Millions)": 104.4, "Area (Square Kilometers)": 1002450},
    "Italy": {"Region": "Europe", "Population (Millions)": 60.4, "Area (Square Kilometers)": 301340},
    "South Korea": {"Region": "Asia", "Population (Millions)": 51.8, "Area (Square Kilometers)": 100210},
    "Pakistan": {"Region": "Asia", "Population (Millions)": 225.2, "Area (Square Kilometers)": 881913},
    "Colombia": {"Region": "South America", "Population (Millions)": 51.1, "Area (Square Kilometers)": 1141748},
    "Spain": {"Region": "Europe", "Population (Millions)": 46.8, "Area (Square Kilometers)": 505990},
    "Iran": {"Region": "Asia", "Population (Millions)": 83.9, "Area (Square Kilometers)": 1648195},
    "Vietnam": {"Region": "Asia", "Population (Millions)": 97.3, "Area (Square Kilometers)": 331212},
    "Thailand": {"Region": "Asia", "Population (Millions)": 69.8, "Area (Square Kilometers)": 513120},
    "Algeria": {"Region": "Africa", "Population (Millions)": 40.4, "Area (Square Kilometers)": 2381741},
    "Poland": {"Region": "Europe", "Population (Millions)": 38.3, "Area (Square Kilometers)": 312696}
}

UNDict={}

for country, data in data.items():
    region = data["Region"]
    population = data["Population (Millions)"]
    area = data["Area (Square Kilometers)"]

    UNDict[country] = {"cont": region, "popl": population, "area": area}

# Veriyi .dat dosyasına yazma
with open('UNdict2.dat', 'wb') as file:
    pickle.dump(UNDict, file)

print("Veriler başarıyla 'veriler.dat' dosyasına yazıldı.")
