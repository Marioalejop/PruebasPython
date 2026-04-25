def calcular_bonificacion(
    promedio: float,
    asistencia_pct: float,
    participa_semillero: bool
) -> float:
    """
    Calcula la bonificación académica.
    """

    if promedio < 0 or promedio > 5:
        raise ValueError("Promedio inválido")

    if asistencia_pct < 0 or asistencia_pct > 100:
        raise ValueError("Asistencia inválida")

    if asistencia_pct < 70:
        return 0.0

    bonif = 0.0

    if promedio >= 4.5 and asistencia_pct >= 95:
        bonif = 0.5
    elif promedio >= 4.0 and asistencia_pct >= 85:
        bonif = 0.3
    elif promedio >= 3.5 and asistencia_pct >= 75:
        bonif = 0.15

    if bonif > 0 and participa_semillero:
        bonif += 0.1

    return bonif