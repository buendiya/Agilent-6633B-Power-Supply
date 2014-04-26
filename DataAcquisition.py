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
#        self.Reset()
#        self.clear()
        
    def Reset(self):
    
        """ Reset """
        
        self.write("*RST")
        logging.info("Reset succeed")
        
    def QueryConfigure(self, channel = None):
    
        """  Query the present configuration on the specified channels  """
        if channel:
            configure = self.ask_for_values("CONFigure? (@%s)" % channel)
            logging.info("Configure%s: %s", channel, configure)
        else:
            configure = self.ask_for_values("CONFigure?")
            logging.info("Configure: %s", configure)
        return configure
         
    def ConfigureCurrentAC(self, currentRange = None, resolution = None, channels = None):
    
        """  Configure the channels for AC or DC current measurements but do not initiate the scan.

        Args:
            currentRange: can be 1, 0.1, 0.01(amps) or AUTO, MIN(0.01), MAX(1), DEF.
            resolution: Numeric. Desired resolution in amps. Can be MIN, MAX or DEF.
            channels: list.
        """
        for channel in channels:
            if currentRange and resolution:
                self.write("CONFigure:CURRent:AC %s,%s,(@%s)" % (currentRange, resolution, channel))
            else:
                self.write("CONFigure:CURRent:AC (@%s)" % channel)

        logging.info("Configure %s succeed", channels)

if __name__ == '__main__':
    try:
        dc = DataAcquisition("GPIB0::2")
        dc.ConfigureCurrentAC("MIN", 0.001, [121])
        dc.QueryConfigure(121)
        dc.ConfigureCurrentAC("MAX", 0.001, [121])
        dc.QueryConfigure(121)

        
    except Exception, e:
        logging.error(e)

