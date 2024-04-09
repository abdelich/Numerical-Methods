import math

grav = 6.67259
grav_abs_err = 85 * math.pow(10, -5)
grav_rel_err = grav_abs_err/grav
print('Gravity constant relative error = ', grav_rel_err)

electron = 1.60217733
electron_abs_err = 49 * math.pow(10, -8)
electron_rel_ell = electron_abs_err/electron
print('Electron`s charge relative error = ', electron_rel_ell)
