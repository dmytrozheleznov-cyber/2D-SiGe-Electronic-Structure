#!/bin/bash

cores=$(nproc)
echo "Using $cores CPU cores for calculation"


rm -f ecut_data.dat

echo "Ecut(Ry)   Total Energy(Ry)"


for ecut in 30 35 40 45 50 55 60 65 70 75 80
do
    
    rho=$((ecut * 8))

    
    cat > scf_$ecut.in << EOF
&CONTROL
  calculation = 'scf'
  pseudo_dir = '../pseudo/'
  outdir = './tmp/'
  prefix = 'SiGe'
  tprnfor = .true.
  tstress = .true.
/
&SYSTEM
  ibrav = 4
  a = 3.95
  c = 15.0
  nat = 2
  ntyp = 2
  ecutwfc = $ecut
  ecutrho = $rho
  occupations = 'smearing'
  smearing = 'mv'
  degauss = 0.01
/
&ELECTRONS
  mixing_beta = 0.7
  conv_thr = 1.0d-8
/
ATOMIC_SPECIES
 Si  28.0855  Si.upf
 Ge  72.6300  Ge.upf
ATOMIC_POSITIONS (crystal)
 Si  0.333333333  0.666666666  0.48
 Ge  0.666666666  0.333333333  0.52
K_POINTS (automatic)
 2 2 1 0 0 0
EOF

    
    mpirun --allow-run-as-root -np $cores pw.x < scf_$ecut.in > scf_$ecut.out

    
    energy=$(grep ! scf_$ecut.out | awk '{print $5}')
    
    
    echo "$ecut        $energy"
    echo "$ecut $energy" >> ecut_data.dat
done

echo "Calculation finished. Results in ecut_data.dat"
