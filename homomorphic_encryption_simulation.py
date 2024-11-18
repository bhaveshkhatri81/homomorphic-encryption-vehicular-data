import tenseal as ts
import numpy as np
import matplotlib.pyplot as plt
import time

# Step 1: Generate Simulated Vehicular Data
def generate_vehicular_data(n=100):
    np.random.seed(42)
    speed = np.random.uniform(30, 100, n)  # Speed in km/h
    gps_lat = np.random.uniform(35.0, 40.0, n)  # Latitude
    gps_long = np.random.uniform(-120.0, -115.0, n)  # Longitude
    return speed, gps_lat, gps_long

speed, gps_lat, gps_long = generate_vehicular_data()

# Step 2: Create CKKS Context for Homomorphic Encryption
def create_context():
    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[40, 21, 21, 40]
    )
    context.global_scale = 2**21
    context.generate_galois_keys()
    return context

context = create_context()

# Step 3: Encrypt the Data
def encrypt_data(context, data):
    return [ts.ckks_vector(context, data[i:i+10]) for i in range(0, len(data), 10)]

encrypted_speed = encrypt_data(context, speed)
encrypted_lat = encrypt_data(context, gps_lat)
encrypted_long = encrypt_data(context, gps_long)

# Step 4: Simulate an Attack by Modifying Encrypted Data
def modify_encrypted_data(encrypted_data):
    tampered_data = []
    for vector in encrypted_data:
        noise = ts.ckks_vector(context, [5] * vector.size())
        tampered_vector = vector + noise
        tampered_data.append(tampered_vector)
    return tampered_data

tampered_speed = modify_encrypted_data(encrypted_speed)

# Step 5: Decrypt Data
def decrypt_data(encrypted_data):
    decrypted_data = []
    for vector in encrypted_data:
        decrypted_data.extend(vector.decrypt())
    return decrypted_data

original_speed_decrypted = decrypt_data(encrypted_speed)
tampered_speed_decrypted = decrypt_data(tampered_speed)

# Visualization 1 - Encrypted and Decrypted Data
def plot_encrypted_data(encrypted_data):
    plt.figure(figsize=(10, 6))
    for vector in encrypted_data:
        plt.plot(range(len(vector.decrypt())), vector.decrypt(), label="Encrypted Data Chunk", linestyle='--', marker='o')
    plt.title("Ciphertext Representation (Encrypted Speed Data)")
    plt.xlabel("Index")
    plt.ylabel("Decrypted Values (Approximation)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_decrypted_data(original, tampered):
    plt.figure(figsize=(10, 6))
    plt.plot(original, label="Original Data", linestyle='--', marker='o')
    plt.plot(tampered, label="Tampered Data", linestyle='-', marker='x')
    plt.title("Original vs Tampered Speed Data (Decrypted)")
    plt.xlabel("Sample Index")
    plt.ylabel("Speed (km/h)")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_encrypted_data(encrypted_speed)
plot_decrypted_data(original_speed_decrypted, tampered_speed_decrypted)

# Step 7: Perform Secure Computation
def compute_average_speed(encrypted_speed_data):
    result = ts.ckks_vector(context, [0])
    total_elements = 0
    for vector in encrypted_speed_data:
        result += vector.sum()
        total_elements += vector.size()
    decrypted_sum = result.decrypt()[0]
    avg_speed = decrypted_sum / total_elements
    return avg_speed

original_avg_speed = compute_average_speed(encrypted_speed)
tampered_avg_speed = compute_average_speed(tampered_speed)

# Visualization 2 - Error Rate
def calculate_error(original, tampered):
    return abs(original - tampered) / original * 100

error_rate = calculate_error(original_avg_speed, tampered_avg_speed)

def plot_error_rate(error_rate):
    plt.figure(figsize=(10, 6))
    plt.bar(["Error Rate"], [error_rate], color='orange')
    plt.title("Error Rate in Tampered Data")
    plt.ylabel("Error Rate (%)")
    plt.grid(True)
    plt.show()

plot_error_rate(error_rate)

# Visualization 3 - Performance Overhead
def measure_computation_time(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time

unencrypted_time = measure_computation_time(np.mean, speed)
encrypted_time = measure_computation_time(compute_average_speed, encrypted_speed)

def plot_performance(unencrypted, encrypted):
    plt.figure(figsize=(10, 6))
    plt.bar(["Unencrypted Data", "Encrypted Data"], [unencrypted, encrypted], color=['blue', 'orange'])
    plt.title("Computation Time: Unencrypted vs Encrypted Data")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.show()

plot_performance(unencrypted_time, encrypted_time)

# Output Results
print(f"Original Average Speed: {original_avg_speed:.2f} km/h")
print(f"Tampered Average Speed: {tampered_avg_speed:.2f} km/h")
print(f"Percentage Error Due to Tampering: {error_rate:.2f}%")
