import pandas as pd
data_frame = pd.read_csv("nombres.csv")

# ¿Hay mujeres llamados Jules, Nery?
jules_data = data_frame[
    (data_frame["name"] == "Jules")
    &
    (data_frame["sex"] == "F")
]

nery_data = data_frame[(data_frame["name"] == "Nery")
                       & (data_frame["sex"] == "F")]

if len(jules_data) > 0:
    print("Hay mujeres llamadas Jules")
else:
    print("No hay mujeres llamadas Jules")

if len(nery_data) > 0:
    print("Hay mujeres llamadas Nery")
else:
    print("No hay mujeres llamadas Nery")

# ¿Cuál es la cantidad de mujeres llamadas Nery en el estado de CA y NJ nacidas después de 1950?
nery_specific_data = data_frame[
    (data_frame['name'] == 'Nery') & (data_frame['state'].isin(['NJ', 'CA'])) & (
        data_frame['sex'] == 'F') & (data_frame['year'] > 1950)
]

nery_specific_total = nery_specific_data['quantity'].sum()

print("La cantidad de mujeres llamadas Nery en el estado de CA y NJ nacidas después de 1950 es " +
      str(nery_specific_total))

# ¿Cuál es la cantidad promedio de hombres llamados Mary nacidos después de 1989?
mary_m = data_frame[(data_frame['name'] == 'Mary') & (
    data_frame['sex'] == 'M') & (data_frame['year'] > 1989)]

average = mary_m['quantity'].mean()

print("La cantidad promedio de hombres llamados Mary nacidos después de 1989 es " +
      str(average))

# ¿Cuáles son los tres estados donde hay más mujeres llamados Nery y Alex?
nery_or_alex = data_frame[(data_frame['name'].isin(
    ['Nery', 'Alex'])) & (data_frame['sex'] == 'F')]

state_totals = nery_or_alex.groupby('state')['quantity'].sum()

top_states = state_totals.sort_values(ascending=False).head(3)

print("Los tres estados donde hay más mujeres llamados Nery y Alex son")

print(top_states)
