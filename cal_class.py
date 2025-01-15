import numpy as np

class four_box:
    def __init__(self,T_1,T_2,T_3,T_4,decreasing_rate):
        self.epsilon = 0.48

        self.m_1 = 6.8*10**(6+9) #m^3
        self.m_2 = 6.8*10**(5+9) 
        self.m_3 = 5.2*10**(6+9)
        self.m_4 = 5.2*10**(6+9)

        self.A_W = 10**6 #m^3s^-1K-1
        self.A_H = 4*10**6

        self.H_1 = 50 #m
        self.H_2 = 50
        self.H_3 = 200
        self.H_set = self.H_1, self.H_2, self.H_3

        self.C_p = 4.186*10**3 #JK^-1g^-1
        self.rho = 10**6 #gm^-3
        self.S_W = 240*10**3 #Wm^-2
        self.S_W_ex = 140*10**3 #Wm^-2

        self.sigma = 5.67*10**(-8+3) #Wm^-2K^-4
        self.rho_air = 1225 #gm^-3

        self.V_ar1 = 5 #ms-1
        self.V_ar2 = 5 #ms-1
        self.V_et = 8

        self.L_d = 1.5*10**(-3)
        self.L = 2260*10**3 #Jg-1

        self.RH = 0.8
        self.T_1 = T_1
        self.T_2 = T_2
        self.T_3 = T_3
        self.T_4 = T_4
        self.H_SW = 0
        self.H_sensible = 0                                 

        self.decreasing_rate = decreasing_rate
        self.H_iOLR = 0
        self.H_iLatent = 0
        self.H_i = 0
        self.q = 0

        self.E = 0.18*(1 - decreasing_rate)

        self.delta_T = 31536000 / 2
        self.T1_array = []
        self.T2_array = []
        self.T3_array = []
        self.T4_array = []
        self.T1_T_2_array = []
        self.T1_array.append(self.T_1)
        self.T2_array.append(self.T_2)
        self.T3_array.append(self.T_3)
        self.T4_array.append(self.T_4)
        self.T1_T_2_array.append(self.T_1-self.T_2)
    
    def calculation_q(self):
        T_eq = (self.T_1 + self.T_2) / 2
        return self.A_H * (T_eq - self.T_3) + self.A_W  * (self.T_1 - self.T_2)
    
    def calculation_H_iOLR(self,i):
        if i == 1:
            T_i = self.T_1
        elif i == 2:
            T_i = self.T_2
        elif i == 3:
            T_i = self.T_3
        # print((T_i**4))
        a = (self.E*self.sigma)*(T_i**4)
        # print("H_iO: "+str(a))
        return a
    
    def calculation_H_iLatent(self,i):
        if i == 1:
            T_i = self.T_1
        elif i == 2:
            T_i = self.T_2
        elif i == 3:
            T_i = self.T_3
        if i == 1:
            V_i = self.V_ar1
        elif i == 2:
            V_i = self.V_ar2
        elif i == 3:
            V_i = self.V_et
        C_L = 10**(-2)
        e_s = 6.1078*100*10**(7.5*T_i/(T_i+237.3))
        a = self.L*V_i*C_L*(0.622/self.rho_air)*e_s*(1-self.RH)
        # print("H_iL: "+str(a))
        return a


    def calculation_H_i(self,i,H_iLatent,H_iOLR):

        a = (self.H_SW - (H_iLatent + self.H_sensible + H_iOLR)) / (self.C_p*self.rho*self.H_set[i-1]*10**5) 
        # print("H_i: "+str(a))
        return a
    
    def step(self):
        H_1Latent = self.calculation_H_iLatent(1)
        H_1OLR = self.calculation_H_iOLR(1)
        H_1 = self.calculation_H_i(1,H_1Latent,H_1OLR)

        H_2Latent = self.calculation_H_iLatent(2)
        H_2OLR = self.calculation_H_iOLR(2)
        H_2 = self.calculation_H_i(2,H_2Latent,H_2OLR)

        H_3Latent = self.calculation_H_iLatent(3)
        H_3OLR = self.calculation_H_iOLR(3)
        H_3 = self.calculation_H_i(3,H_3Latent,H_3OLR)

        q = self.calculation_q()
        
        T1 = self.T_1
        T2 = self.T_2
        T3 = self.T_3
        T4 = self.T_4
        
        self.T_1 = T1 + self.delta_T*(H_1 + (q/self.m_1)*(1-self.epsilon)*(T2-T1))
        self.T_2 = T2 + self.delta_T*(H_2 + (q/self.m_2)*(T4-T2))
        self.T_3 = T3 + self.delta_T*(H_3 + (q/self.m_3)*self.epsilon*(T2-T3) + (q/self.m_3)*(1-self.epsilon)*(T1-T3))
        self.T_4 = T4 + self.delta_T*(q/self.m_4)*(T3-T4)
        print("delta_T1: "+str(self.T_1-T1))
        print("delta_T2: "+str(self.T_2-T2))
        print("delta_T3: "+str(self.T_3-T3))
        print("delta_T4: "+str(self.T_4-T4))
        # print("T1-T2: "+str(self.T_1-self.T_2))

        self.T1_array.append(self.T_1)
        self.T2_array.append(self.T_2)
        self.T3_array.append(self.T_3)
        self.T4_array.append(self.T_4)
        self.T1_T_2_array.append(self.T_1-self.T_2)
        
