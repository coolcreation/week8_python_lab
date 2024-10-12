#!/usr/bin/env python3
# Jeff Bohn
# 10/9/2024
# Chapter 14
# objects.py


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    def getStr(self):
        return (self.name, self.year )     
        
