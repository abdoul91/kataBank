#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:42:05 2019

@author: abdoulaziz
"""
from client import Client
from time import gmtime, strftime

class Bank :

    
    
    def __init__(self, b_name) :
        self._clients   = dict()
        self._comptes   = dict()
        self._operation = dict()
        self._b_name    = b_name
        self._ids       = 0
        
        
        
#==============================================================================
# Important Note:
# This function allow to create a new client by his name and his lastname
#==============================================================================
    def create(self, nom, prenom) :
        self._ids += 1
        self._clients[self._ids]   = Client(nom, prenom)
        self._comptes[self._ids]   = 0
        self._operation[self._ids] = [] 
        return self._ids
        
        
#==============================================================================
# Important Note:
# This function allow to  obtain a customer by his id 
#==============================================================================
    def get_client(self, idd) :
        return self._clients[idd]
    


#==============================================================================
# Important Note:
# This function allow a customer to  make a deposit 
#==============================================================================
    def deposit(self, idd, amount) :
        self._comptes[idd] += amount
        t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self._operation[idd].append(['deposit', amount, self._comptes[idd], t])
        print("you have deposited", amount)
        
   
    
#==============================================================================
# Important Note:
# This function allow a customer to  make a withdrawal 
#==============================================================================
    def widthraw(self, idd, amount) :        
        try :
            assert self._comptes[idd] > 0
            if self._comptes[idd] - amount >= 0 :
               self._comptes[idd] -= amount
               t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
               self._operation[idd].append(['widthrawal', amount, self._comptes[idd],t])
               print("you have withdrawn ", amount)
            else :
                raise ValueError ("You can't windraw this amount \n\n")
        except AssertionError:
            print("You can't windraw, your balance is zero \n\n")
        except ValueError:
            print("You can only windraw ", self._comptes[idd])
            print("\n\n")
            


#==============================================================================
# Important Note:
# A customer can see the history of all his operations with this function
#==============================================================================
    def consulte(self, idd) :
        op = ''
        operations = self._operation[idd]
        if operations == [] :
           print("no operation performed\n\n")
        else :
           operations.reverse()
           for l in operations :
               s = 'Type : {} \n\t Amount : {} \n\t Balance : {} \n\t Date : {}'.format(l[0], 
                         l[1], l[2], l[3])
               op += s
               op += '\n\n'  
           print("Your balance now is :", self._comptes[idd])
           print("Your operations :")
           print(op)
            
     
        
        
#==============================================================================
# Important Note:
# Bank class getters and setters using decorators syntax
#==============================================================================   
    @property
    def clients(self) :
        return self._clients
    
    @property
    def comptes(self) :
        return self._comptes
    
    @property
    def operation(self) :
        return self._operation
    
    @property
    def ids(self) :
        return self._ids
    
    @ids.setter
    def ids(self,n):
        self._ids = n