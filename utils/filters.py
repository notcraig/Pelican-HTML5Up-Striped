#!/usr/local/bin/python
import inflect
o = inflect.engine()

def ordinal(self):
  
  return o.ordinal(self)  #  '1st' '2nd' '11th' '23rd' et al
  


