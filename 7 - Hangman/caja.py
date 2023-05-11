def crear_caja(MAX_HORIZONTAL, MAX_VERTICAL, texto):
    tam_texto = len(texto)
    espacios_disp = (MAX_HORIZONTAL-tam_texto) // 2
    espacios_derecha = " " * espacios_disp
    espacios_izquierda = " " * espacios_disp

    arriba = " " + "_" * MAX_HORIZONTAL
    espacios = "|" + " " * MAX_HORIZONTAL + "|"
    base = "|" + "_" * MAX_HORIZONTAL + "|"

    linea_texto = f"|{espacios_izquierda}{texto}{espacios_derecha}|"

    if (MAX_HORIZONTAL-tam_texto) % 2 == 1:
        linea_texto = f"|{espacios_izquierda}{texto}{espacios_derecha} |"

    print(f"{arriba}")
    for i in range(MAX_VERTICAL-1):
        if i == MAX_VERTICAL // 2:
            print(f"{linea_texto}")
        else:
            print(f"{espacios}")
    print(f"{base}")
