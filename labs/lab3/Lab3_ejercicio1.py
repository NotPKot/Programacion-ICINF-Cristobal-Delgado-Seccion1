#Los_rios = [14, 18429, 404432 ] 
#Magallanes = [12, 1382291, 66533 ]


Censo = { 'ID Región': 14,
                    'Nombre': 'Los Rios',
                    'Superficie (Km2)' : 18429,
                     'Habitantes (2017)' : 404432}

Censo2 = { 'ID Región2': 12,
                    'Nombre2': 'Magallanes',
                    'Superficie (Km2)2' : 1382291,
                     'Habitantes (2017)2' : 166533}


Censo.update(Censo2)


print(Censo)

densidad = Censo['Habitantes (2017)']/Censo['Superficie (Km2)']
densidad2= Censo2['Habitantes (2017)2']/Censo2['Superficie (Km2)2']


densidadFloat= round(densidad, 1)
densidadFloat2 = round(densidad2,1)

Censo.update({'Densidad' : densidadFloat})
Censo.update({'Densidad2': densidadFloat2})


Censo.update({'Capital': 'Valdivia'})
Censo.update({'Capital2': 'Punta Arenas'})

comunas = ['Río Bueno', 'La Unión', 'Paillaco']
Comunas2 = ['Cabo de Hornos', 'Puerto Williams', 'Porvenir']
print(type(comunas))
print(type(Comunas2))

Censo.update({'Comunas': comunas})
Censo.update({'Comunas2': Comunas2})

provincias = ('Ranco', 'Valdivia' )
provincias2 = ( 'Antártica Chilena', 'Magallanes', 'Tierra del Fuego', 'Última Esperanza')

print(type(provincias))
print(type(provincias2))

Censo.update({'Provincias': provincias})
Censo.update({'Provincias': provincias2})

print(Censo)
