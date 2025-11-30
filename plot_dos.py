import matplotlib.pyplot as plt
import numpy as np


E_fermi = -1.9986 


data = np.loadtxt('SiGe.dos')
energy = data[:, 0] - E_fermi
dos = data[:, 1]

plt.figure(figsize=(8, 6))
plt.plot(energy, dos, 'r-', linewidth=1, label='Total DOS')
plt.fill_between(energy, 0, dos, where=(energy < 0), color='red', alpha=0.1)

plt.axvline(0, color='k', linestyle='--', label="Fermi Level")
plt.xlabel('Energy (eV) - $E_F$')
plt.ylabel('Density of States (states/eV)')
plt.title('Density of States of SiGe')
plt.xlim(-6, 6)
plt.ylim(bottom=0)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('SiGe_DOS.png', dpi=300)
print("DOS Graph saved as SiGe_DOS.png")
