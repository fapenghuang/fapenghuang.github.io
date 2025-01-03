import numpy as np
import ptarcade.models_utils as aux

name = 'uldm_c_unc' 

smbhb = True 

parameters ={
    "log10_A_dm" : aux.prior("Uniform", -9, -4),
    "log10_f_dm" : aux.prior("Uniform", -10, -5.5),
    "gamma_p" : aux.prior("Uniform", 0, 2 * np.pi, common=False),
    "gamma_e" : aux.prior("Uniform", 0, 2 * np.pi),
    "phi_hat_sq_p" : aux.prior("Gamma", 1,0,1, common=False),
    "phi_hat_sq_e" : aux.prior("Gamma", 1,0,1)
}

group = ['log10_A_dm', 'log10_f_dm']

def pulsar_signal(toas, log10_A_dm, log10_f_dm, gamma_p, phi_hat_sq_p):
    
    A = 10**log10_A_dm
    f = 10**log10_f_dm

    # return timing residual in seconds
    return A * np.sqrt(phi_hat_sq_p) * np.sin(2 * np.pi * f * toas + gamma_p)

def earth_signal(toas, log10_A_dm, log10_f_dm, gamma_e, phi_hat_sq_e):
    
    A = 10**log10_A_dm
    f = 10**log10_f_dm

    # return timing residual in seconds
    return A * np.sqrt(phi_hat_sq_e) * np.sin(2 * np.pi * f * toas + gamma_e)

def signal(toas, log10_A_dm, log10_f_dm, gamma_p, gamma_e, phi_hat_sq_p, phi_hat_sq_e):
    """
    Function that calculates the pulsar + earth signal generated by
    ultralight dark matter in the uncorrelated limit 
    :param toas: Time-of-arrival measurements [s]
    :param log10_A_dm: log10 of signal amplitude
    :param log10_f_dm: log10 of signal frequency
    :param phase_p: Pulsar-term phase
    :param phase_p: Earth-term phase
    :param phi_hat_sq_p: dm density fluctuation at the pulsar position
    :param phi_hat_sq_e: dm density fluctuation at the Earth position
    :return: the waveform as induced timing residuals (seconds)
    """

    p_s = pulsar_signal(toas, log10_A_dm, log10_f_dm, gamma_p, phi_hat_sq_p)
    e_s = earth_signal(toas, log10_A_dm, log10_f_dm, gamma_e, phi_hat_sq_e)

    return p_s + e_s
