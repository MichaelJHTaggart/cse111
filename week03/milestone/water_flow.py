WATER_DENSITY = 998.2
GRAVITY = 9.80665
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    
    t = tower_height
    w = tank_height

    h = t + ((3 * w) / 4)

    return h


def pressure_gain_from_water_height(height):

    p = WATER_DENSITY
    g = GRAVITY
    h = height

    P = (p * g * h) / 1000

    return P


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

    f = friction_factor
    L = pipe_length
    p = WATER_DENSITY
    v = fluid_velocity
    d = pipe_diameter

    if L <= 0 or f <= 0 or v <= 0:
        return 0

    numerator = f * L * p * (v * v)
    denominator = 2000 * d

    P = -numerator / denominator

    return P


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):

    p = WATER_DENSITY
    v = fluid_velocity
    n = quantity_fittings

    if n <= 0 or v <= 0:
        return 0

    numerator = 0.04 * p * (v * v) * n
    denominator = 2000

    P = -numerator / denominator

    return P


def reynolds_number(hydraulic_diameter, fluid_velocity):

    p = WATER_DENSITY
    d = hydraulic_diameter
    v = fluid_velocity
    μ = WATER_DYNAMIC_VISCOSITY

    R = (p * d * v) / μ

    return R
