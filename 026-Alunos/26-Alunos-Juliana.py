a=[input(),float(input()),float(input()),0]
m=(a[1]+a[2])/2
a[3]=m
if m>7:s="Aprovado"
else:s="Reprovado"
print("NOME: %s\nNOTA 1: %.1f\nNOTA 2: %.1f\nMEDIA: %.1f\nSTATUS: %s"%(a[0],a[1],a[2],a[3],s))
