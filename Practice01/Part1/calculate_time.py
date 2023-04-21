import math

FOOT_IN_YARD = 3  # число футов в ярде
FOOT_PER_SECOND = 5280 / 3600  # сколько футов/секунду в 1 миле/час


def calculate(dist1, dist2, offset, v_sand, ratio, theta1):
    dist1 *= FOOT_IN_YARD  # перевод в футы
    offset *= FOOT_IN_YARD  # перевод в футы
    v_sand *= FOOT_PER_SECOND  # перевод в футы в секунду
    variable = math.tan(math.radians(theta1)) * dist1
    length1 = math.sqrt(variable ** 2 + dist1 ** 2)
    length2 = math.sqrt((offset - variable) ** 2 + dist2 ** 2)
    time = (length1 + ratio * length2) / v_sand
    return time