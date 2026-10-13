import numpy as np

def generate_synthetic_signal(duration=5.0, fs=1000.0, noise_level=0.8):
    """
    Generates a synthetic time-series signal combining low and high frequency components 
    with Gaussian noise, mimicking biological or physical sensor data streams.
    """
    t = np.linspace(0, duration, int(duration * fs), endpoint=False)
    # Combine low-frequency oscillation and high-frequency bursts
    signal = np.sin(2 * np.pi * 4 * t) + 0.5 * np.sin(2 * np.pi * 35 * t)
    noise = noise_level * np.random.normal(size=t.shape)
    noisy_signal = signal + noise
    return t, noisy_signal