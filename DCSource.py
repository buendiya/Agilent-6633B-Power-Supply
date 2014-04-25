# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:14:13 2014

@author: jingsz
"""

import visa
import logging


logging.basicConfig(level=logging.DEBUG)

class DCSource(visa.GpibInstrument):

    """ This class exists to handle the requirements of the
        Agilent 6633B System DC power supply 
        
   """

    err = 1e-6
        
    def __init__(self, gpib_identifier, **keyw):

        super(DCSource, self).__init__(gpib_identifier, **keyw)
        
        self.write("*RST")
        logging.info("Reset succeed")
        
    def OutputOn(self):
    
        """ Enable the output """
        
        self.write("OUTPut ON")
        logging.info("Output On")
        
    def OutputOff(self):
    
        """ Enable the output """
        
        self.write("OUTPut OFF")
        logging.info("Output Off")
        

if __name__ == '__main__':
    dc = DCSource("GPIB0::7")
    dc.OutputOn()


