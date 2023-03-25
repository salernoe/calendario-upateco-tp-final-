from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import tkinter as tk
from tkinter import ttk
import json
import os

class Evento:
    def __init__(self):
        self.nombre = ""
        self.fecha = ""
        self.hora = ""
        self.descripcion = ""
        self.importancia = ""
    
    # set attributes

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora(self,hora):
        self.hora = hora

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_importancia(self, importancia):
        self.importancia = importancia

    # get attributes

    def get_nombre(self):
        return self.nombre
    
    def get_fecha(self):
        return self.fecha
    
    def get_hora(self):
        return self.hora
    
    def get_descripcion(self):
        return self.descripcion
    
    def get_importancia(self):
        return self.importancia



    def get_elemento_tupla(self):
        evento = ()
        evento.append(self.nombre)
        evento.append(self.fecha)
        evento.append(self.hora)
        evento.append(self.descripcion)
        evento.append(self.importancia)
        return evento
    
    @staticmethod
    def eliminar(id_evento):
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                pass
        #print(eventos)
        aux = []
        for elem in eventos["eventos"]:
            if elem['id'] != id_evento:
                aux.append(elem)

        eventos["eventos"] = aux

        #recetas["cantidad"] = int(recetas["cantidad"])

        #print(recetas)

        with open("eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)
    
    def guardar(self):
        abs_path_json = os.path.dirname(os.path.abspath('eventos.json'))
        abs_path = os.path.dirname(abs_path_json)
        path_json = os.path.relpath(abs_path_json, abs_path)+'\eventos.json'
        print(path_json)
        with open(path_json, 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = {"cantidad": 0, "recetas": []}         
        
        evento = {}
        evento["id"] = int(eventos["cantidad"])+1
        evento["nombre"] = self.nombre
        evento["fecha"] = self.fecha
        evento["hora"] = self.hora
        evento["descripcion"] = self.descripcion
        evento["importancia"] = self.importancia
        print(evento)
        print('********************************')
        print(eventos)
        eventos["recetas"].append(evento)
        eventos["cantidad"] = int(eventos["cantidad"])+1
        print(eventos)
        with open("calendario-upateco-tp-final--main\eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)

    def guardarV1(self):
        with open("eventos.json", 'r') as archivo:
            try:
                eventos = json.load(archivo)
            except ValueError:
                eventos = []          
        evento = {}
        evento["nombre"] = self.nombre
        evento["fecha"] = self.fecha
        evento["hora"] = self.hora
        evento["descripcion"] = self.descripcion
        evento["importancia"] = self.importancia
        eventos.append(evento)
        
        with open("eventos.json", 'w') as archivo:
            json.dump(eventos, archivo)