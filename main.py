import json

with open('data.json', 'r') as file:
    data = json.load(file)

#print(data)


#1-Gasto total por usuario
gasto_por_usuario = {}

for usuario, compras in data.items():
    total_gastado = 0.0
    for compra in compras:
        total_gastado = total_gastado + compra["precio"]
    
    gasto_por_usuario[usuario] = total_gastado
    print(f"El usuario {usuario} ha gastado {total_gastado:.2f} €.")


#2-Cliente VIP (Mayor gasto)
nombre_cliente_vip = ""
mayor_gasto = 0.0
for usuario, gasto in gasto_por_usuario.items():
    if gasto > mayor_gasto:
        mayor_gasto = gasto
        nombre_cliente_vip = usuario #se queda con el ultimo nombre que tenga mas gasto
print(f"El cliente con mayor gasto es: {nombre_cliente_vip} y su gasto total es de {mayor_gasto} €.")

#3-Cliente con más artículos y nº articulos
max_articulos=0
for usuario, compras in data.items():
    cantidad_productos = len(compras)
    if cantidad_productos > max_articulos:
        max_articulos = cantidad_productos
        cliente_mas_articulos = usuario
print(f"El cliente con más artículos es: {cliente_mas_articulos} y ha comprado {max_articulos} artículos.")

#4-Producto más caro y más barato

#NOTA IMPORTANTE: No se ha valorado que hayan varios productos con el mismo precio o varios compradores para el mismo producto

nombre_mas_caro = ""
precio_mas_caro = 0.0
usuario_mas_caro = ""

nombre_mas_barato = ""
precio_mas_barato = 999999.0   # Empezamos con un número muy alto para poder encontrar el menor
usuario_mas_barato = ""

for usuario, compras in data.items():
    for compra in compras:
        nombre = compra["producto"]
        precio = compra["precio"]
        
        # Comprobar si es el más caro
        if precio > precio_mas_caro:
            precio_mas_caro = precio
            nombre_mas_caro = nombre
            usuario_mas_caro = usuario
            
        # Comprobar si es el más barato
        if precio < precio_mas_barato:
            precio_mas_barato = precio
            nombre_mas_barato = nombre
            usuario_mas_barato = usuario

print(f"El producto más caro es: {nombre_mas_caro}, cuesta {precio_mas_caro} € y lo compró {usuario_mas_caro}.")
print(f"El producto más barato es: {nombre_mas_barato}, cuesta {precio_mas_barato} € y lo compró {usuario_mas_barato}.")
        

#5-Resumen por categorías
gasto_por_categoria = {}

for usuario, compras in data.items():
    for compra in compras:
        categoria = compra["categoria"]
        precio = compra["precio"]
        
        # Si la categoría ya está en el diccionario
        if categoria in gasto_por_categoria:
            gasto_por_categoria[categoria] = gasto_por_categoria[categoria] + precio
        # Si es la primera vez que aparece
        else:
            gasto_por_categoria[categoria] = precio

print("Resumen por categorías:")
print(gasto_por_categoria)

#6-Productos con IVA 
for usuario, compras in data.items():
    for compra in compras:
        # Añadimos columna a Data
        compra["precioIVA"] = compra["precio"] * 1.21

#7-Fichero CSV
import csv
with open('contabilidad_a.csv', 'w', newline='', encoding='utf-8') as archivo:
    writer = csv.writer(archivo)
    
    writer.writerow(["producto", "precioIVA"])
    
    for usuario, compras in data.items():
        for compra in compras:
            writer.writerow([compra["producto"], round(compra["precioIVA"], 2)])
        



