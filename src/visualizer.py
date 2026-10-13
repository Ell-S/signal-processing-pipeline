import matplotlib.pyplot as plt
import os

def plot_results(t, original, filtered, output_path="assets/signal_processing_output.png"):
    plt.figure(figsize=(10, 5))
    plt.plot(t[:1000], original[:1000], label='Noisy Raw Signal', color='gray', alpha=0.6)
    plt.plot(t[:1000], filtered[:1000], label='Filtered Signal (Bandpass)', color='#1f77b4', linewidth=1.5)
    plt.title('Time-Series Signal Preprocessing & Filtering Pipeline', fontsize=12, fontweight='bold')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[INFO] Plot successfully generated and saved to {output_path}")