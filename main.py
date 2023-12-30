import numpy as np

Cp_T = {
    "T": [
        0.01,
        5,
        10,
        15,
        20,
        25,
        30,
        35,
        40,
        45,
        50,
        55,
        60,
        65,
        70,
        75,
        80,
        85,
        90,
        95,
        100
    ],
    "Cp": [
        4217,
        4205,
        4194,
        4186,
        4182,
        4280,
        4178,
        4178,
        4179,
        4180,
        4181,
        4183,
        4185,
        4187,
        4190,
        4193,
        4197,
        4201,
        4206,
        4212,
        4217
    ]
}
M_oil = 0.1
M_water = 0.2
T_in_oil = 100
T_in_water = 30
T_out_oil = 60

Cp_oil = 2131


def get_Cp_water(T):
    right = find_next_greater_sorted(Cp_T["T"], T)
    left = right - 1
    t_list = Cp_T["T"][left:right]
    Cp_list = Cp_T["Cp"][left:right]
    return np.interp(T, t_list, Cp_list)


def find_next_greater_sorted(lst, x):
    left, right = 0, len(lst) - 1
    res = None
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] > x:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


def get_actual_T_out_water():
    T_out_water = 50
    while True:
        detla_t_water = M_oil * Cp_oil * (T_in_oil - T_out_oil) / (M_water * get_Cp_water(T_out_water - T_in_water))
        T_out_water_new = T_in_water + detla_t_water
        if abs(T_out_water_new - T_out_water) < 0.1:
            return T_out_water_new
        else:
            T_out_water = T_out_water_new


T_out_water_actual = get_actual_T_out_water()
print(T_out_water_actual, "T_out_water_actual")
