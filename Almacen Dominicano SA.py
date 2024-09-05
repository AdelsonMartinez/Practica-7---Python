#Se agrega la clase Item y sus atributos 
import os
class Item: 
    def __init__(self, item_id, description, volumen):
        self.item_id = item_id
        self.description = description
        self.volumen = volumen
        
    def __str__(self): #se accede a los atributos de la instancia y se muestran en un formato legible
        return f"ID: {self.item_id}, Descripción: {self.description}, Volumen: {self.volumen} m³"
#Se agrega la clase Almacen y sus atributos         
class Almacen:
    def __init__(self, almacen_id, nombre, altura, anchura, longitud):
        self.almacen_id = almacen_id
        self.nombre = nombre
        self.altura = altura
        self.anchura = anchura
        self.longitud = longitud
        self.items = []
        self.capacidad_total = altura * anchura * longitud
        self.capacidad_disponible = self.capacidad_total * 0.8  
    #Se define el método de la clase que se encarga de agregar un ítem
    def agregar_item(self, item):
        if self.capacidad_disponible >= item.volumen:
            self.items.append(item)
            self.capacidad_disponible -= item.volumen
            print(f"Ítem {item.item_id} agregado al almacén {self.nombre}.")
        else:
            print(f"No hay suficiente espacio en el almacén {self.nombre} para el ítem {item.item_id}.")

def retirar_item(self, item_id): #se define una función llamada retirar_item 
        for item in self.items: #se inicia un bucle que itera sobre cada ítem en la lista llamada self.items,
            if item.item_id == item_id: #En cada iteración se verifica si el item.item_id del ítem actual coincide con el item_id proporcionado. 
                self.items.remove(item)
                self.capacidad_disponible += item.volumen
                print(f"Ítem {item.item_id} retirado del almacén {self.nombre}.")
                return
        print(f"Ítem {item_id} no encontrado en el almacén {self.nombre}.")