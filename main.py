#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 01:58:56 2019

@author: abdoulaziz
"""
from bank import Bank


#==============================================================================
# Important Note:
# Create a Bank object call myBank
#==============================================================================
myBank = Bank("myBank")


#==============================================================================
# Important Note:
# Ask customer to create a Bank account
#==============================================================================
print("Enter your name and create an account")
prenom    = input("First name :")
nom       = input("Name :")
idc       = myBank.create(nom, prenom)
print("Your customer number is :", idc)

        
#==============================================================================
# Important Note:
# display of a menu to allow the customer to perform operations
#==============================================================================
c = True
while c :
   try : 
     print("Welcome to your Bank :")
     print("\t 1.Consute my operations")
     print("\t 2.Withdraw from my account")
     print("\t 3.Deposit to my account")
     print("\t 4.Close")
     choix = input("Write your choice number : ")   
     choix = int(choix)
     if choix == 1:
        myBank.consulte(idc)
     elif choix == 2:
        amount = input("Write your amount :")
        print("\n\n")
        amount = int(amount)
        myBank.widthraw(idc, amount)
     elif choix == 3:
        amount = input("Write your amount :")
        print("\n\n")
        amount = int(amount)
        myBank.deposit(idc, amount)
     else :
        c = False
   except ValueError :
     print("You need to choose a number\n\n")  
   
    