import numpy as np
from scipy.special import erfc

# Boltzmann constant
k = 1.38e-23  

def fspl(distance_km, frequency_ghz):
    return 20*np.log10(distance_km) + 20*np.log10(frequency_ghz) + 92.45

def received_power(pt, gt, gr, fspl_db, other_losses):
    return pt + gt + gr - fspl_db - other_losses

def noise_power(bandwidth_hz, temperature_k):
    noise_watts = k * temperature_k * bandwidth_hz
    return 10*np.log10(noise_watts)

def carrier_to_noise(pr_dbw, noise_dbw):
    return pr_dbw - noise_dbw

def total_cn(cn_up, cn_down):
    cn_up_lin = 10**(cn_up/10)
    cn_down_lin = 10**(cn_down/10)
    total_lin = 1 / ((1/cn_up_lin) + (1/cn_down_lin))
    return 10*np.log10(total_lin)

def ber_qpsk(snr_db):
    snr_linear = 10**(snr_db/10)
    return 0.5 * erfc(np.sqrt(snr_linear))