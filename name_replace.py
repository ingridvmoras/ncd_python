# Change nameplaces for Phylip with species Real Name 
# Last modified by: 
# Romulo Antao
# 4 January 2018

import sys

f = open('outtree','r')

data = f.read()
data_mod = data.replace('A'*9,"ASM1156v2")
data_mod = data_mod.replace('B'*9,"ASM9278v1")
data_mod = data_mod.replace('C'*9,"ASM20425v1")
data_mod = data_mod.replace('D'*9,"ASM23720v1")
data_mod = data_mod.replace('E'*9,"ASM25303v1")
ata_mod = data_mod.replace('F'*9,"ASM584v2")
data_mod = data_mod.replace('G'*9,"ASM886v2")

f = open('outtree','w')
f.write(data_mod)
f.close()
