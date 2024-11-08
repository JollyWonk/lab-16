import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 9, 100)

y = 0.5 * x + 0.1 * x**4

plt.plot(x, y, 'k:', label='y = 0.5x + 0.1x^4') 
plt.xlabel('x')  
plt.ylabel('y')  
plt.title('Графік функції')  
plt.legend()  
plt.grid(True)  

plt.savefig('gr_file.tiff', dpi=300)
plt.show()
