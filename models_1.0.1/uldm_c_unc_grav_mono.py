import numpy as np
import ptarcade.models_utils as aux

name = 'uldm_c_unc_grav_mono'

smbhb = True

parameters ={
    "log10_rho_dm" : aux.prior("Uniform", -1, 2),
    "log10_m_dm" : aux.prior("Uniform", -23.2, -22.9),
    "gamma_p" : aux.prior("Uniform", 0, 2 * np.pi, common=False),
    "gamma_e" : aux.prior("Uniform", 0, 2 * np.pi),
    "phi_hat_sq_p" : aux.prior("Gamma", 1,0,1, common=False),
    "phi_hat_sq_e" : aux.prior("Gamma", 1,0,1)
}

group = ['log10_rho_dm', 'log10_m_dm']

scale_factor = aux.gev_to_hz**-1 * 0.5*np.pi * aux.G    #conversion to hz is actually to s^-1

def signal(toas, log10_rho_dm, log10_m_dm, gamma_e, phi_hat_sq_e, gamma_p, phi_hat_sq_p):
    """
    Function that calculates the pulsar term signal generated by
    ultralight dark matter 
    :param toas: Time-of-arrival measurements [s]
    :param log10_rho_dm: log10 of dm density [GeV/cm3]
    :param log10_m_dm: log10 of dm mass [eV]
    :param gamma_e(p): The Earth(Pulsar)-term phase of the GW
    :param phi_hat_sq_e(p): dm fluctuation at the Earth (Pulsar) position
    :return: the waveform as induced timing residuals [s]
    """
    
    rho = 10**log10_rho_dm * 1e6 * aux.gev_to_hz**-3 * 299792458.0**3   #dm density in Gev^4
    m = 10**log10_m_dm * 1e-9                                           #dm mass in Gev
    omega = 2 * m * aux.gev_to_hz                                       #dm gravitational freq in s^-1 (not Hz)

    e_s =  scale_factor * rho * m**-3 * phi_hat_sq_e * np.sin(omega * toas + gamma_e)
    p_s =  scale_factor * rho * m**-3 * phi_hat_sq_p * np.sin(omega * toas + gamma_p)    

    return e_s + p_s