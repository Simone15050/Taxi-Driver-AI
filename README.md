# 🚕 Taxi Driver AI Simulation

This project simulates an autonomous taxi navigating a city grid to pick up and drop off randomly spawning customers. Built using Python, it was originally developed in 2023 for an AI course at Fairleigh Dickinson University and updated in 2025 for improved functionality.

---

## 🧠 Features
- Grid-based map using 0s (roads) and 1s (sidewalks)
- Customers spawn on sidewalks
- The taxi searches for and picks up nearby customers
- Customers specify a destination (grid coordinates)
- The taxi calculates the distance and fare, and drops them off
- The shift ends after 300 movement units, and performance is evaluated

---

## 🛠️ Project History

This project was originally created in 2023 as part of my AI course. While preparing to upload it in 2025, I reviewed the code and found some issues that impacted the accuracy and behavior of the simulation. I’ve since corrected those issues and included both the original and updated versions for comparison.

### ✅ Key Fixes in the 2025 Version:
- **Expanded destination logic:**  
  In the original version, customers could only select from 4 coordinates due to the way random destinations were chosen. The updated version allows for a wider range of destinations, making the simulation more dynamic.

- **Proper shift termination:**  
  Previously, the simulation continued running even after the 300-move limit was reached, causing performance calculations to repeat. The new version correctly breaks out of the loop when the shift ends, and evaluates performance only once.

### 📂 Files Included:
- `Final Taxi Driver- Jordan Brown Fixed 23.py` – Original version submitted in 2023  
- `Final Taxi Driver- Jordan Brown Edited 2025.py` – Updated and fully functioning version

---

## 📊 Technologies Used
- Python
- Randomization and Grid Simulation
- Basic AI Logic / Decision-Making
- Jupyter Notebook and VS Code

---

## 🎓 Created For
AI Course Project (2023)  
Fairleigh Dickinson University  

---

👨‍💻 **Created by Jordan Brown**  
📍 [Visit My GitHub Profile](https://github.com/Simone15050)  
📫 [Connect with me on LinkedIn](https://www.linkedin.com/in/jordan-brown-413615233)
