import numpy as np
import ptarcade.models_utils as aux

name = 'uldm_c_cor' 

smbhb = True 

parameters ={
    "log10_A_dm" : aux.prior("Uniform", -9, -4),
    "log10_f_dm" : aux.prior("Uniform", -10, -5.5),
    "gamma_p" : aux.prior("Uniform", 0, 2 * np.pi, common=False),
    "gamma_e" : aux.prior("Uniform", 0, 2 * np.pi),
    "phi_hat_sq" : aux.prior("Gamma", 1,0,1)
}

group = ['log10_A_dm', 'log10_f_dm']

def pulsar_signal(toas, log10_A_dm, log10_f_dm, gamma_p, phi_hat_sq):
    
    A = 10**log10_A_dm
    f = 10**log10_f_dm

    # return timing residual in seconds
    return A * np.sqrt(phi_hat_sq) * np.sin(2 * np.pi * f * toas + gamma_p)

def earth_signal(toas, log10_A_dm, log10_f_dm, gamma_e, phi_hat_sq):
    
    A = 10**log10_A_dm
    f = 10**log10_f_dm

    # return timing residual in seconds
    return A * np.sqrt(phi_hat_sq) * np.sin(2 * np.pi * f * toas + gamma_e)

def signal(toas, log10_A_dm, log10_f_dm, gamma_p, gamma_e, phi_hat_sq):
    """
    Function that calculates the pulsar + earth signal generated by
    ultralight dark matter in the correlated limit 
    :param toas: Time-of-arrival measurements [s]
    :param log10_A_dm: log10 of signal amplitude
    :param log10_f_dm: log10 of signal frequency
    :param phase_p: Pulsar-term phase
    :param phase_p: Earth-term phase
    :param phi_hat_sq: dm density fluctuation
    :return: the waveform as induced timing residuals (seconds)
    """

    p_s = pulsar_signal(toas, log10_A_dm, log10_f_dm, gamma_p, phi_hat_sq)
    e_s = earth_signal(toas, log10_A_dm, log10_f_dm, gamma_e, phi_hat_sq)

    return p_s + e_s