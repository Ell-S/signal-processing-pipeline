import numpy as np
import pandas as pd
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def extract_features(t, signal, window_size=100):
    """
    Extracts statistical rolling features (mean, std) and signal energy.
    """
    df = pd.DataFrame({'time': t, 'signal': signal})
    df['rolling_mean'] = df['signal'].rolling(window=window_size, min_periods=1).mean()
    df['rolling_std'] = df['signal'].rolling(window=window_size, min_periods=1).std()
    df['energy'] = df['signal'] ** 2
    return df