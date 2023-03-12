import pandas as pd

data = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        'Ventas': [30500, 35600, 28300, 33900, 45000, 18600, 38740, 35000, 28950, 17505, 36540, 44444],
        'Gastos': [22000, 23400, 18100, 20700, 42500, 12000, 21450, 18900, 17850, 8500, 21500, 25600]}

df = pd.DataFrame(data)
# Escribir un programa que genere un DataFreme con los datos de la siguiente tabla:
print(df)

# Escribir una función que reciba un DataFrame con el formato del ejercicio anterior y devuelva el balance total en los meses indicados.


def get_balances(df, months):
    balances = []
    for month in months:
        month_df = df[df['Mes'] == month]
        balance = month_df['Ventas'].iloc[0] - month_df['Gastos'].iloc[0]
        balances.append(balance)
    return balances


print('Los balances son ')
print(get_balances(df, ['Mayo', 'Agosto']))

# Escribir una función que exporte el DataFrame y el resultado de lo solicitado en este item.


def export_df(df):
    months = df['Mes'].tolist()
    balances = get_balances(df, months)
    new_data = {'Mes': months, 'Ventas': df['Ventas'].tolist(
    ), 'Gastos': df['Gastos'].tolist(), 'Balance': balances}
    new_df = pd.DataFrame(new_data)
    new_df.to_csv('reporte_con_balance.csv', index=False)


export_df(df)
