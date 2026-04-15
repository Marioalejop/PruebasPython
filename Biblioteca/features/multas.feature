Feature: Sistema de multas por devolución tardía

  Como estudiante de la Universitaria de Colombia
  Quiero conocer mis multas
  Para poder gestionar mis reservas

  Scenario: Cálculo de multa por 3 días de retraso
    Given un estudiante con 3 días de retraso
    When consulta su multa
    Then el sistema muestra 1500 COP

  Scenario: Estudiante sin multa
    Given un estudiante sin retrasos
    When consulta su multa
    Then el sistema muestra "Sin multa pendiente"

  Scenario: Bloqueo por multa
    Given un estudiante con multa mayor a 0
    When intenta reservar un libro
    Then el sistema bloquea la reserva
    And muestra un mensaje de deuda