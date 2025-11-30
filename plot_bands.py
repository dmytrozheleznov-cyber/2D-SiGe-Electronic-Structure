import matplotlib.pyplot as plt
import numpy as np
import sys


data_file = 'SiGe_bands.dat.gnu'


E_fermi = 0.0
try:
    with open('scf_final.out', 'r') as f:
        for line in f:
            if "Fermi energy" in line:
                
                E_fermi = float(line.split()[-2])
                print(f"Found Fermi energy: {E_fermi} eV")
except:
    print("Warning: Could not read Fermi energy from file. Using 0.0")
    print("Check if 'scf_final.out' exists or set E_fermi manually in the script.")


try:
    data = np.loadtxt(data_file)
except OSError:
    print(f"Error: File {data_file} not found. Did you run bands.x?")
    sys.exit(1)

k = data[:, 0]
energy = data[:, 1] - E_fermi  


plt.figure(figsize=(10, 6))
plt.plot(k, energy, 'b-', linewidth=1, alpha=0.8) 


plt.axhline(0, color='k', linestyle='--', linewidth=1, label="Fermi Level")
plt.ylabel('Energy (eV) - $E_F$')
plt.xlabel('Wave Vector (k)')
plt.title('Electronic Band Structure of 2D SiGe')
plt.ylim(-6, 6)  
plt.xlim(min(k), max(k))
plt.grid(True, alpha=0.3)
plt.legend()


output_file = 'SiGe_bands.png'
plt.savefig(output_file, dpi=300)
print(f"Success! Graph saved as {output_file}")
