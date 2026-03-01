import tkinter as tk
from tkinter import messagebox
from link_budget import *
from graphs import *

def calculate():
    try:
        frequency = float(freq_entry.get())
        distance = float(dist_entry.get())
        pt = float(pt_entry.get())
        gt = float(gt_entry.get())
        gr = float(gr_entry.get())
        bandwidth = float(bw_entry.get()) * 1e6
        temperature = float(temp_entry.get())
        rain_loss = float(rain_entry.get())

        path_loss = fspl(distance, frequency)
        pr = received_power(pt, gt, gr, path_loss, rain_loss)
        noise = noise_power(bandwidth, temperature)
        cn = carrier_to_noise(pr, noise)
        ber = ber_qpsk(cn)

        result_text.set(
            f"FSPL: {path_loss:.2f} dB\n"
            f"Received Power: {pr:.2f} dBW\n"
            f"Noise Power: {noise:.2f} dBW\n"
            f"C/N: {cn:.2f} dB\n"
            f"BER (QPSK): {ber:.2e}"
        )

    except:
        messagebox.showerror("Error", "Invalid Input")

def plot_ber_graph():
    plot_ber()

def plot_distance_graph():
    frequency = float(freq_entry.get())
    pt = float(pt_entry.get())
    gt = float(gt_entry.get())
    gr = float(gr_entry.get())
    rain_loss = float(rain_entry.get())
    plot_received_power_vs_distance(pt, gt, gr, frequency, rain_loss)

# GUI
root = tk.Tk()
root.title("Satellite Link Budget Simulator")

tk.Label(root, text="Frequency (GHz)").grid(row=0)
tk.Label(root, text="Distance (km)").grid(row=1)
tk.Label(root, text="Transmit Power (dBW)").grid(row=2)
tk.Label(root, text="Tx Gain (dBi)").grid(row=3)
tk.Label(root, text="Rx Gain (dBi)").grid(row=4)
tk.Label(root, text="Bandwidth (MHz)").grid(row=5)
tk.Label(root, text="Noise Temp (K)").grid(row=6)
tk.Label(root, text="Rain Loss (dB)").grid(row=7)

freq_entry = tk.Entry(root)
dist_entry = tk.Entry(root)
pt_entry = tk.Entry(root)
gt_entry = tk.Entry(root)
gr_entry = tk.Entry(root)
bw_entry = tk.Entry(root)
temp_entry = tk.Entry(root)
rain_entry = tk.Entry(root)

freq_entry.grid(row=0, column=1)
dist_entry.grid(row=1, column=1)
pt_entry.grid(row=2, column=1)
gt_entry.grid(row=3, column=1)
gr_entry.grid(row=4, column=1)
bw_entry.grid(row=5, column=1)
temp_entry.grid(row=6, column=1)
rain_entry.grid(row=7, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=8, column=0)
tk.Button(root, text="Plot BER", command=plot_ber_graph).grid(row=8, column=1)
tk.Button(root, text="Power vs Distance", command=plot_distance_graph).grid(row=9, column=0)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left").grid(row=10, columnspan=2)

root.mainloop()