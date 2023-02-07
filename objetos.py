#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import random as rd
import matplotlib.pyplot as plt
# Por ahora esto es un prototipo para los objetos.
# Hay definidos objetos para los obstáculos, el jugador y la meta. Falta definir un objeto para el campo.
# Los obstáculos pueden ser dinámicos.

class InitialConditions():
    def __init__(self, pos_in, vel_in, spin_in, ener_in):
        self.pos_in = pos_in
        self.vel_in = vel_in
        self.spin_in = spin_in
        self.ener_in = ener_in
    def getPos_in(self):
        return self.pos_in
    def getVel_in(self):
        return self.vel_in
    def getSpin_in(self):
        return self.spin_in
    def getEner_in(self):
        return self.ener_in

lvl1 = InitialConditions(np.array([0.0,0.0]), np.array([0.0,0.0]), 1, 100.0)


class Player():
    def __init__(self, name):
        self.name = name
        self.color = "b"
        self.pos = lvl1.getPos_in()
        self.vel = lvl1.getVel_in()
        self.spin = lvl1.getSpin_in()
        self.ener = lvl1.getEner_in()
    def getPos(self):
        return self.pos
    def getVel(self):
        return self.vel
    def getName(self):
        return self.name
    def getEner(self):
        return self.ener
    def getSpin(self):
        return self.spin
    def getColor(self):
        return self.color
    
    def setPos(self, n_pos):
        self.pos = n_pos
    def setVel(self, n_vel):
        self.vel = n_vel
    def setEner(self, n_ener):
        self.ener = n_ener
    def setSpin(self, n_spin):
        self.spin = n_spin


class Obst():
    def __init__(self):
        self.pos = np.array([(0.2 + rd.random())*10.0, (0.2 + rd.random())*10.0])
        self.din = rd.choice([True, False])
        self.color = "r"
    def getPos(self):
        return self.pos
    def getDin(self):
        return self.din



plyr1 = Player("Guille")


class Goal():
    def __init__(self):
        self.pos = np.array([15.0, 0.0])
        self.color = "g"
    def getPos(self):
        return self.pos
    def getColor(self):
        return self.color

goal = Goal()

obsts = []
for i in range(10):
    obsts.append(Obst())




x = []
y = []
z = []
for i in range(len(obsts)):
    x.append(obsts[i].getPos()[0])
    y.append(obsts[i].getPos()[1])
