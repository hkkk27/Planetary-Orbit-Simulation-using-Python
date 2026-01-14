```markdown
# Planetary Orbit Simulation using Python

This project simulates the orbital motion of Earth and Jupiter around the Sun
using Newton’s law of gravitation and numerical integration (Euler method).

The goal of this project is to visually and computationally understand how
gravitational force, velocity, and mass affect planetary motion.

---

## 🔭 Project Overview

- Simulates Earth and Jupiter orbiting the Sun in 2D space
- Uses real-world approximate astronomical values
- Demonstrates:
  - Circular and elliptical orbits
  - Escape velocity
  - Effect of changing velocity and mass
  - Limitations of Euler integration

The Sun is fixed at the origin, and gravitational force acts on the planets.

---

## ⚙️ Physics & Mathematics Used

- Newton’s Universal Law of Gravitation  
- Newton’s Second Law of Motion  
- Euler Numerical Integration  

Acceleration of a planet:
```

a = G * M_sun / r²

````

---

## 🛠️ Technologies Used

- Python 3
- NumPy
- Matplotlib (FuncAnimation)

---

## ▶️ How to Run the Simulation

1. Clone the repository:
```bash
git clone https://github.com/your-username/planetary-orbit-simulation.git
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the simulation:

```bash
python orbital_simulation.py
```

---

## 📊 Experiments Performed

* Same mass, different velocities
* Reduced velocity → elliptical orbit
* Very low velocity → collapse into the Sun
* High velocity → escape trajectory
* Effect of changing Sun’s mass
* Effect of changing planet mass
* Negative velocity → reversed orbit direction

All experiments and observations are explained in detail in the PDF report.

---

## ⚠️ Limitations

* Euler method introduces numerical drift
* No planet–planet interaction
* Sun is fixed (does not move)
* 2D simulation only

---

## 🚀 Future Improvements

* Use Runge-Kutta integration
* Include planet-planet gravitational forces
* Add more planets
* Extend simulation to 3D
* Allow Sun to move dynamically

---

## 📘 Documentation

Detailed explanation, equations, observations, and screenshots are available in:

**Planetary_Motion_Report.pdf**

---

## 👤 Author

Harshit Singh
Undergraduate Student
Interest Areas: Simulation, Data Analysis

```
