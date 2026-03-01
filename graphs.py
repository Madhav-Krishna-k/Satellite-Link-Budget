import numpy as np
import matplotlib.pyplot as plt
from link_budget import ber_qpsk, fspl

def plot_ber():
    snr_db = np.linspace(0, 15, 100)
    ber = ber_qpsk(snr_db)

    plt.figure()
    plt.semilogy(snr_db, ber)
    plt.title("BER vs SNR (QPSK)")
    plt.xlabel("SNR (dB)")
    plt.ylabel("Bit Error Rate")
    plt.grid(True)
    plt.show()

def plot_received_power_vs_distance(pt, gt, gr, frequency, other_losses):
    distances = np.linspace(500, 40000, 100)
    pr_list = []

    for d in distances:
        loss = fspl(d, frequency)
        pr = pt + gt + gr - loss - other_losses
        pr_list.append(pr)

    plt.figure()
    plt.plot(distances, pr_list)
    plt.title("Received Power vs Distance")
    plt.xlabel("Distance (km)")
    plt.ylabel("Received Power (dBW)")
    plt.grid(True)
    plt.show()