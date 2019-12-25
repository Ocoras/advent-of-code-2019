def fuel_required(mass):
    return (mass // 3) - 2


def total(module):
    tot_for_module = 0
    fuel = fuel_required(module)
    while fuel > 0:
        tot_for_module += fuel
        fuel = fuel_required(fuel)
    return tot_for_module


modules = [
    108404,
    142663,
    113953,
    89187,
    134971,
    93901,
    79832,
    142582,
    145387,
    104530,
    87533,
    75312,
    139459,
    141201,
    68801,
    61163,
    96040,
    110287,
    97738,
    138959,
    122690,
    110331,
    107930,
    105938,
    134097,
    63599,
    56781,
    60741,
    85313,
    74432,
    112114,
    108556,
    99115,
    142180,
    86957,
    68882,
    53394,
    84383,
    75073,
    94942,
    89506,
    65782,
    85816,
    109814,
    79113,
    146432,
    55951,
    138827,
    140796,
    149851,
    137353,
    110513,
    132480,
    53724,
    52292,
    63473,
    97705,
    141506,
    147125,
    126996,
    107361,
    145397,
    105546,
    96261,
    90682,
    108029,
    144607,
    144603,
    74959,
    92000,
    70920,
    66026,
    70196,
    149729,
    126996,
    120026,
    118383,
    109199,
    84628,
    121412,
    135413,
    138807,
    115286,
    132455,
    73051,
    83131,
    78528,
    140029,
    117782,
    143779,
    55642,
    141798,
    79406,
    50167,
    124606,
    92822,
    144622,
    85043,
    126924,
    135624,
]


# print(fuel_required(12))
# print(fuel_required(14))
# print(fuel_required(1969))
# print(fuel_required(100756))
#
# print(total(14))
# print(total(1969))
# print(total(100756))

total_without_fuel = 0
total_inc_fuel = 0
for module in modules:
    total_without_fuel += fuel_required(module)
    total_inc_fuel += total(module)
# print(total_without_fuel)
print(total_inc_fuel)

# fuel_to_transport_fuel = fuel_required(total)
