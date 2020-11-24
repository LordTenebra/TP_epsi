# -*- coding: utf-8 -*-
#!/usr/bin/python
def prix(prix, quant):
    return float(prix) * quant

def ttc(prix_HT):
    return round(prix_HT + ((prix_HT * 20) / 100), 2)
