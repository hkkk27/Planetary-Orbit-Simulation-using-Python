
```markdown
# 🌍 Planetary Orbit Simulation using Python

A computational physics project that simulates the orbital motion of **Earth and Jupiter around the Sun** using **Newtonian mechanics** and **numerical integration (Euler method)**.

This project aims to build both **physical intuition** and **computational understanding** of how gravity, velocity, and mass govern planetary motion.

---

## 🔭 Project Overview

This simulation models a simplified solar system where:

- Earth and Jupiter orbit a fixed Sun in **2D space**
- Gravitational interaction follows **Newton’s law of gravitation**
- Motion is updated using **Euler numerical integration**

### Key Concepts Demonstrated
- Circular and elliptical orbits  
- Escape velocity and collapse scenarios  
- Effect of changing velocity and mass  
- Numerical instability and limitations of Euler’s method  

---

## ⚙️ Physics & Mathematical Model

The simulation is based on:

- **Newton’s Universal Law of Gravitation**
- **Newton’s Second Law of Motion**
- **Euler Method for numerical integration**

### Acceleration of a Planet

```

a = G × M_sun / r²

````

Where:
- `G` is the gravitational constant  
- `M_sun` is the mass of the Sun  
- `r` is the distance from the Sun  

The Sun is fixed at the origin and exerts gravitational force on the planets.

---

## 🛠️ Technologies Used

- **Python 3**
- **NumPy** — vector and numerical computation
- **Matplotlib** — visualization and animation (`FuncAnimation`)

---

## ▶️ How to Run the Simulation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/planetary-orbit-simulation.git
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Simulation

```bash
python orbital_simulation.py
```

An animated visualization of planetary orbits will appear.

---

## 📊 Experiments & Observations

The following experiments were performed:

* Same mass, different velocities
* Reduced velocity → elliptical orbit
* Very low velocity → collapse into the Sun
* High velocity → escape trajectory
* Effect of changing the Sun’s mass
* Effect of changing planet mass
* Negative velocity → reversed orbital direction

📘 **All experiments, plots, and explanations are documented in the PDF report.**

---

## ⚠️ Limitations

* Euler integration introduces numerical drift over long simulations
* No planet–planet gravitational interaction
* Sun is assumed stationary
* Simulation is limited to **2D space**

---

## 🚀 Future Improvements

* Implement **Runge-Kutta (RK4)** integration
* Include planet–planet gravitational forces
* Add more planets (full solar system model)
* Extend simulation to **3D space**
* Allow the Sun to move dynamically

---

## 📘 Documentation

A detailed explanation of:

* Physical equations
* Model assumptions
* Experimental observations
* Visual results

is available in:

**📄 Planetary_Motion_Report.pdf**

---

## 👤 Author

**Harshit Singh**
Undergraduate Student

**Interest Areas:**

* Computational Simulation
* Data Analysis

---

