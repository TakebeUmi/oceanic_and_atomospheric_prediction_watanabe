import numpy as np
from cal_class import four_box
import matplotlib.pyplot as plt
DURATION = 30
T1 = 300.0
T2 = T1 - 3.1
T3 = T1
T4 = T1
fb_1 = four_box(
    T_1 = T1,
    T_2 = T2,
    T_3 = T3,
    T_4 = T4,
    decreasing_rate=0.15
)
fb_2 = four_box(
    T_1 = T1,
    T_2 = T2,
    T_3 = T3,
    T_4 = T4,
    decreasing_rate=0.4
)
fb_3 = four_box(
    T_1 = T1,
    T_2 = T2,
    T_3 = T3,
    T_4 = T4,
    decreasing_rate=0.6
)
fb_4 = four_box(
    T_1 = T1,
    T_2 = T2,
    T_3 = T3,
    T_4 = T4,
    decreasing_rate=0.8
)

for i in range(DURATION):
    fb_1.step()
    fb_2.step()
    fb_3.step()
    fb_4.step()

# year = np.arange(DURATION)
# plt.figure(figsize=(8,5))
# plt.plot(year, fb_1.T1_T_2_array,label="0.15",color="blue")
# plt.plot(year, fb_2.T1_T_2_array,label="0.4",color="green")
# plt.plot(year, fb_3.T1_T_2_array,label="0.6",color="red")
# plt.plot(year, fb_4.T1_T_2_array,label="0.8",color="purple")
# plt.xlabel("half year")
# plt.ylable("T1 - T2")
# plt.title("Temperature Change Over years")
# plt.legend()
# plt.grid()
# plt.show()