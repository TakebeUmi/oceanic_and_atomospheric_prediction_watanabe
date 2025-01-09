import numpy as np

class four_box:
    def __init__(self,T_1,T_2,T_3):
        self.m_1 = 6.8*10**3 #km^3
        self.m_2 = 6.8*10**5 
        self.m_3 = 5.2*10**6
        self.m_4 = 5.2*10**6

        self.A_W = 10*6 #m^3s^-1K-1
        self.A_H = 4*10**6

        self.H_1 = 50 #m
        self.H_2 = 50
        self.H_3 = 200

        self.C_p = 4.186 #JK^-1g^-1
        self.rho = 10**6 #gm^-3
        self.S_W = 240 #Wm^-2
        self.S_W_ex = 140 #Wm^-2
        self.E = 0.18
        self.sigma = 5.67*10**(-8) #Wm^-2K^-4
        self.rho_air = 1225 #gm^-3

        self.V_ar1 = 5 #ms-1
        self.V_ar2 = 5 #ms-1
        self.V_ar3 = 8

        self.L_d = 1.5*10**(-3)
        self.L = 2260 #Jg-1

        self.RH = 0.8
        self.T_1 = T_1
        self.T_2 = T_2
        self.T_3 = T_3
    
    def calculation_q(self):
        T_eq = (self.T_1 + self.T_2) / 2
        return self.A_H * (T_eq - self.T_3) + self.A_W  * (self.T_1 - self.T_2)
    