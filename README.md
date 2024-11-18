
# Homomorphic Encryption of Vehicular Data: Simulating Attack Models to Resist Data Modification

## Project Overview

This project demonstrates the application of **Homomorphic Encryption (HE)** using the **CKKS scheme** to secure vehicular data. The main focus is on simulating and resisting data modification attacks by encrypting data, introducing tampering, and evaluating the impact of such tampering on computations performed over encrypted data.

Homomorphic encryption allows computations to be performed directly on encrypted data without decryption, ensuring privacy and security for sensitive data. This project uses simulated vehicular data (e.g., speed, GPS coordinates) to showcase this functionality and measure the resilience of the system under attack.

---

## Features

1. **Simulate Vehicular Data**:
   - Generate synthetic data including vehicle speed and GPS coordinates.
   
2. **Homomorphic Encryption Using CKKS**:
   - Encrypt data using the **CKKS** scheme, which supports approximate arithmetic on encrypted data.

3. **Data Modification Attack Simulation**:
   - Simulate an attacker modifying encrypted data.
   - Introduce tampered noise to demonstrate potential risks.

4. **Decryption and Comparison**:
   - Decrypt both original and tampered data to highlight the effects of tampering.
   - Compare the decrypted values and observe discrepancies.

5. **Secure Computation**:
   - Perform secure computations (e.g., average speed) on encrypted data.
   - Measure the difference in results between original and tampered data.

6. **Error Rate Analysis**:
   - Calculate and visualize the error rate introduced by tampering.

7. **Performance Analysis**:
   - Compare computation times for unencrypted and encrypted data processing.

---

## Installation

### Prerequisites

- Python 3.x
- Required libraries:
  - `tenseal`
  - `numpy`
  - `matplotlib`

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/bhaveshkhatri81/homomorphic-encryption-vehicular-data.git
   cd homomorphic-encryption-vehicular-data
   ```

2. Install dependencies:
   ```bash
   pip install tenseal numpy matplotlib
   ```

3. Run the script:
   ```bash
   python homomorphic_encryption_simulation.py
   ```

---

## Project Structure

```
.
├── homomorphic_encryption_simulation.py  # Main script
├── README.md                             # Project documentation
└── requirements.txt                      # List of dependencies (optional)
```

---

## How It Works

### Step 1: Simulate Vehicular Data
Generate synthetic data representing:
- **Speed**: Vehicle speed in km/h.
- **GPS Coordinates**: Latitude and longitude values.

### Step 2: Encrypt Data
Encrypt the generated data using the **CKKS homomorphic encryption** scheme.

### Step 3: Simulate Data Tampering
Modify the encrypted data to simulate a potential attack. Tampering is done by adding noise vectors to encrypted data.

### Step 4: Decrypt and Compare Data
Decrypt both original and tampered data to highlight differences caused by the attack.

### Step 5: Secure Computation
Perform encrypted computations (e.g., average speed) and analyze the effect of tampering on results.

### Step 6: Visualize Results
- **Encrypted vs. Decrypted Data**: Compare data before and after tampering.
- **Error Rate**: Visualize the percentage error introduced by tampering.
- **Performance Overhead**: Measure and compare computation times for encrypted vs. unencrypted data.

---

## Results

- **Average Speed Calculation**: Shows the impact of tampering on calculated averages.
- **Error Rate Analysis**: Highlights the error introduced by tampered data.
- **Performance Comparison**: Demonstrates the overhead introduced by homomorphic encryption.

---

## Visualizations

1. **Ciphertext Representation**:
   - Visualizes encrypted data in its decrypted approximate form.
2. **Original vs. Tampered Data**:
   - Plots to compare the original and tampered data.
3. **Error Rate**:
   - A bar graph showing the error rate due to tampering.
4. **Performance Overhead**:
   - A comparison of computation times for encrypted and unencrypted data processing.

---

## Conclusion

This project highlights the robustness of **homomorphic encryption** in securing vehicular data and its ability to resist data modification attacks. By simulating an attack, decrypting the data, and analyzing performance, it provides a comprehensive overview of how homomorphic encryption can be applied in real-world scenarios to ensure data integrity and privacy.

---
