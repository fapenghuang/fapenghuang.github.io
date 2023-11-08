from ptarcade.models_utils import prior

parameters = {
            'log_A_star' : prior("Uniform", -14, -6),
            'log_f_star' : prior("Uniform", -10, -6)
            }

def S(x):
    return x / (1 + x**2)

def spectrum(f, log_A_star, log_f_star):
    A_star = 10**log_A_star
    f_star = 10**log_f_star

    return A_star * S(f/f_star)
