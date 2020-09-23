# -*- coding: utf-8 -*-
"""Importlib_metadata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r26yUHRbRB5j74gkoUicuxAWgLiLnaGw
"""

#https://docs.python.org/3/library/importlib.metadata.html

from importlib_metadata import version, requires, metadata

bibliotecas = ['pandas', 'numpy', 'naoexiste', 
                'seaborn','wheel','matplotlib']

#Versao bibiotecas
for lib in bibliotecas:
  try:
    print("Versão pacote " + lib + ": ",version(lib))
  except:
    print("ops! Biblioteca ausente:", lib)

#Metada bibliotecas - Requires-Python
for lib in bibliotecas:
  try:
    lib_metadata = metadata(lib)
    print("Distribution metadata (Requires-Python) for  " + lib + ": ",lib_metadata['Requires-Python'])
  except:
    print("ops! Biblioteca ausente:", lib)

#Requires bibliotecas
for lib in bibliotecas:
  try:
    print("\nRequires for " + lib + ":\n ",requires(lib))
  except:
    print("\nOps.... Biblioteca ausente:", lib)