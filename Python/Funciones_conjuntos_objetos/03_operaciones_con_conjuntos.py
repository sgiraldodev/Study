#Unir varios conjuntos
set_countries_a = {'Bra', 'Pe', 'Arg'}
set_countries_b = {'Chi', 'Mex', 'Bra'}
print(set_countries_a)
print('\n')
print(set_countries_b)


print('\n')
print('Unir varios conjuntos')
set_countries_c= set_countries_a.union(set_countries_b)
print(set_countries_c)

print('\n')
print('Unir varios conjuntos con un operador')
set_countries_d = set_countries_a | set_countries_b
print(set_countries_d) 

print('\n')
print('Identificar los valores en comun de conjuntos')
set_countries_e = set_countries_a.intersection(set_countries_b)
print(set_countries_e)

print('\n')
print('Identificar los valores en comun de conjuntos con operador')
set_countries_f = (set_countries_a & set_countries_b)
print(set_countries_f)

print('\n')
print('Identificar los valores diferentes en un conjunto')
set_countries_g = set_countries_a.difference(set_countries_b)
print(set_countries_g)

print('\n')
print('Diferencia simetrica de conjuntos: Crear conjunto con los elementos que no se repiten en los conjuntos')
set_countries_h = set_countries_a.symmetric_difference(set_countries_b)
print(set_countries_h)