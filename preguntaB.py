lista_diccionarios = [{'curso': 'Matemáticas', 'inscritos': 50, 'aprobados': 40},
                      {'curso': 'Historia', 'inscritos': 30, 'aprobados': 25},
                      {'curso': 'Inglés', 'inscritos': 70, 'aprobados': 60}]

print('La cantidad de inscritos en el tercer registro es ' +
      str(lista_diccionarios[2]['inscritos']))
print('La cantidad de aprobados en el último registro es ' +
      str(lista_diccionarios[2]['aprobados']))

segundo_registro_aprobados = lista_diccionarios[1]['aprobados']

segundo_registro_inscritos = lista_diccionarios[1]['inscritos']

porcentaje_segundo_registro = (segundo_registro_aprobados /
                               segundo_registro_inscritos) * 100


print('Porcentaje de aprobados en el segundo registro ' +
      str(porcentaje_segundo_registro))
