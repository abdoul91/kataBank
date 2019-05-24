#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:21:27 2019

@author: abdoulaziz
"""

#==============================================================================
# Important Note:
# Client class with his getters and setters using decorators syntax 
#==============================================================================
class Client :
    
    
    def __init__(self, nom, prenom) :
        self._nom    = nom
        self._prenom = prenom
        
        
    @property
    def nom(self) :
        return self._nom
    
    @nom.setter
    def nom(self,n):
        self._nom = n
        
    @property    
    def prenom(self) :
        return self._prenom
    
    @prenom.setter
    def prenom(self,p):
        self._prenom = p