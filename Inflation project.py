import matplotlib.pyplot as plt
import numpy as np
y=np.array([6.19, 5.51, 5.70, 5.54, 5.59, 5.69, 5.55, 7.70, 9.88, 10.89])
mylabels=["2015: 6.19%", "2016: 5.51%", "2017: 5.70%", "2018: 5.54%","2019: 5.59%","2020:5.69%","2021:5.55%","2022:7.70%","2023:9.88%","2024:10.89%"]
myexplode=[0,0,0,0,0,0,0,.1,.2,.3]
plt.pie(y,labels=mylabels,explode=myexplode,shadow=True)
plt.legend(title="The Inflation rate of Bangladesh over the last ten years:")
plt.show()