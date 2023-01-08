def pasos_robot(pasos):
    if pasos == 1 or pasos == 2:
        return pasos
    return pasos_robot(pasos-1) + pasos_robot(pasos-2)

print(pasos_robot(5))
