from src.generator import generate_synthetic_signal
from src.processor import bandpass_filter, extract_features
from src.visualizer import plot_results

def main():
    print("[INFO] Initializing Time-Series Processing Pipeline...")
    
    #Generate Synthetic Data (Sampling frequency 1000 Hz)
    fs = 1000.0
    t, noisy_signal = generate_synthetic_signal(duration=5.0, fs=fs, noise_level=0.7)
    
    #Apply Bandpass Filter (Keeping frequencies between 2 Hz and 10 Hz)
    print("[INFO] Applying Butterworth bandpass filter...")
    filtered_signal = bandpass_filter(noisy_signal, lowcut=2.0, highcut=10.0, fs=fs, order=4)
    
    #Extract Statistical Features
    print("[INFO] Extracting features (rolling statistics & energy)...")
    features_df = extract_features(t, filtered_signal)
    print(features_df.head())
    
    #Visualize Output
    plot_results(t, noisy_signal, filtered_signal, output_path="assets/signal_processing_output.png")
    print("[INFO] Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()