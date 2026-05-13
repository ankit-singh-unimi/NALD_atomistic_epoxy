# Atomistic NALD

Code for computing frequency-dependent viscoelastic storage and loss moduli using the Non-Affine Lattice Dynamics (NALD) framework.

The methodology combines molecular simulations, Hessian matrix analysis, affine force-field correlations, and non-affine lattice dynamics theory to calculate viscoelastic properties of atomistic and polymeric glassy materials.

---

## Overview

The NALD calculation requires three main quantities:

* Vibrational density of states (DOS)
* Affine force-field correlator
* Friction kernel

Starting from an equilibrated atomistic configuration, the workflow proceeds through Hessian construction, eigenmode analysis, DOS evaluation, and finally the calculation of the storage modulus (G'(\omega)) and loss modulus (G''(\omega)).

---

## Workflow

### 1. Generate Hessian Matrix

```bash id="wlhbso"
mpirun -np 12 lmp_mpi -in in.hessian
```

### 2. Generate Affine Force Field

```bash id="4z3jhz"
mpirun -np 12 lmp_mpi -in in.AF
```

### 3. Diagonalize Hessian

```bash id="jmy08p"
python diagonalization.py
```

### 4. Compute DOS and Affine Correlator

```bash id="jlwm9d"
python cal_DOS_Gamma.py
```

### 5. Compute Viscoelastic Moduli

Compile:

```bash id="r3z3gf"
gfortran G_p.f90 -o Gp.out
gfortran G_dp.f90 -o Gdp.out
```

Run:

```bash id="lbfmuj"
./Gp.out
./Gdp.out
```

---

## Repository Contents

| File                 | Description                             |
| -------------------- | --------------------------------------- |
| `in.hessian`         | Hessian matrix generation               |
| `in.AF`              | Affine force-field calculation          |
| `in.GA`              | Affine modulus calculation              |
| `diagonalization.py` | Hessian diagonalization                 |
| `cal_DOS_Gamma.py`   | DOS and affine correlator               |
| `G_p.f90`            | Storage modulus (G'(\omega))            |
| `G_dp.f90`           | Loss modulus (G''(\omega))              |
| `average_Gdp.py`     | Averaging over independent trajectories |

---

## Requirements

* LAMMPS
* Python 3
* NumPy
* SciPy
* gfortran

---

## Applications

* Polymer glasses
* Amorphous solids
* Atomistic viscoelasticity
* Frequency-dependent mechanical response

---

## Developed By

**Zaccone Group**
University of Milan, Italy

---

## Citation

If you use this code, please cite:

V. Vaibhav, T. W. Sirk, and A. Zaccone,
*Time-Scale Bridging in Atomistic Simulations of Epoxy Polymer Mechanics Using Nonaffine Deformation Theory*,
Macromolecules **57**, 10885 (2024).

---

## License

This code is intended for academic and research purposes only.
Users are free to use and modify the code with appropriate citation.
