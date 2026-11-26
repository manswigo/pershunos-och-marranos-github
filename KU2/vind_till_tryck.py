import numpy as np


def wind_to_thrust(wind, turbine_diameter, max_generator_power):
    """
    Converts wind speed to thrust force on the wind turbine rotor.

    Parameters
    ----------
    wind : array
        Wind speed [m/s]

    turbine_diameter : float
        Rotor diameter [m]

    max_generator_power : float
        Maximum generator power [W]
        3.4, 10, 15 MW

    Returns
    -------
    thrust : array
        Thrust force [N]
    """

    # Constants
    rho = 1.225              # Air density [kg/m^3]
    Cp_turbine_max = 0.45    # Maximum turbine power coefficient [-]
    Ct_max = 0.8             # Maximum thrust coefficient [-]
    k = 1                    # Thrust decline exponent above rated wind speed

    wind = np.asarray(wind, dtype=float)

    # Swept rotor area
    swept_area = np.pi * turbine_diameter**2 / 4

    # Rated wind speed
    rated_wind_speed = (max_generator_power / (0.5 * rho * swept_area * Cp_turbine_max))**(1 / 3)

    # Thrust force at rated wind speed
    rated_thrust = (0.5 * rho * swept_area * Ct_max * rated_wind_speed**2)

    # Create thrust array
    thrust = np.zeros_like(wind)

    # Calculate thrust force for each wind speed
    for i, v in enumerate(wind):

        if v <= rated_wind_speed:

            thrust[i] = (0.5 * rho * swept_area * Ct_max * v**2)

        else:

            thrust[i] = (rated_thrust * (rated_wind_speed / v)**k)

    return thrust