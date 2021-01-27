#!/bin/env python3

class state:
    """small class to hold gas properties in a
    compact way"""
    
    def __init__(self, gasname, temperature, pressure):
        from CoolProp.CoolProp import PropsSI
        self.gasname = gasname
        self.temperature = temperature
        self.pressure = pressure
        
        self.density = PropsSI('D', 'T', self.temperature, 'P', self.pressure, self.gasname)
        self.dynamic_viscosity = PropsSI('viscosity', 'T', self.temperature, 'P', self.pressure, self.gasname)
        self.kinematic_viscosity = self.dynamic_viscosity / self.density

    def __str__(self):
        return "{:s}\nT= {:.1f}K, P= {:.0f}Pa\nrho= {:.3f}kg/m3, mu= {:.3e}Pa*s, nu= {:.3e}m2/s".format(self.gasname,
                                                                                                        self.temperature,
                                                                                                        self.pressure,
                                                                                                        self.density,
                                                                                                        self.dynamic_viscosity,
                                                                                                        self.kinematic_viscosity)
    
if __name__ == '__main__':
    pass