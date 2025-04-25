# LISTA
lista = [1, 2, 3]
lista = lista + [4]             
print("Lista:", lista)
print("Elementos:", len(lista))
lista[len(lista):] = [10]        
print("Lista modificada:", lista)

# DICCIONARIO
dic = {"nombre": "Ana", "edad": 20}
dic["ciudad"] = "Bogotá"    
print("\nDiccionario:", dic)
print("Elementos:", len(dic))
dic["edad"] = 21           
print("Diccionario modificado:", dic)

# TUPLA
tupla = (1, 2, 3)
print("\nTupla:", tupla)
print("Elementos:", len(tupla))
# cambiar 
lista_temp = list(tupla)
lista_temp[0] = 10
tupla = tuple(lista_temp)
print("Tupla modificada:", tupla)
