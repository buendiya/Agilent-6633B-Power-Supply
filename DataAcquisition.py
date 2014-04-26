# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 17:14:13 2014

@author: jingsz
"""

import visa
import logging


logging.basicConfig(level=logging.DEBUG)

class DataAcquisition(visa.GpibInstrument):

    """ This class exists to handle the requirements of the
        34970A data acquisition/switch units.
        
   """
   
    def __init__(self, gpib_identifier, **keyw):
        super(DataAcquisition, self).__init__(gpib_identifier, **keyw)
        self.Reset()
        self.clear()
        
    def Reset(self):
    
        """ Reset """
        
        self.write("*RST")
        logging.info("Reset succeed")
        
    def QueryConfigure(self, channel = None):
    
        """  Query the present configuration on the specified channels  """
        if channel:
            configure = self.ask_for_values("CONFigure? (@%s)" % channel)
        else:
            configure = self.ask_for_values("CONFigure?")
        logging.info("Configure: %s", configure)
        return configure
        
 

if __name__ == '__main__':
    try:
        dc = DataAcquisition("GPIB0::2")
        dc.QueryConfigure()
        dc.QueryConfigure(101)

        
    except Exception, e:
        logging.error(e)

