#este diccionario es de mi

Dic = {

    "Nombre"   : "Manuel",
    "Apellido" : "Mateo" ,
    "Edad"     : 19,
    "Num mascotas" : 2,
    "Mascotas" : ["bicho","monito"]
}

print(Dic["Apellido"])

print(Dic)

print(f"""
    El nombre de esta persona es {Dic['Nombre']} {Dic['Apellido']}
    y su edad es de {Dic['Edad']}
    Tiene {Dic['Num mascotas']}
    La primera con nombre {Dic['Mascotas'][0]}
    La segunda con nombre {Dic['Mascotas'][1]}
""")

print("Este fue el diccionario")

Dic["Apellido"] = "Naruto"
Dic["age"] = Dic.pop("Edad")  

print(Dic)