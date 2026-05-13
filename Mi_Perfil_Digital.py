#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Michell Alexandra Oviedo Vasquez"
edad = 14
estatura = 1.57
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("mxchell_777", "michell123-aura")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "musa", "artista": "carabin3", "duracion": "2:15"},
{"titulo": "Instagram", "artista": "blessd", "duracion": "2:46"},
{"titulo": "una noche en Medellín", "artista": "cris mj", "duracion": "2:34"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
