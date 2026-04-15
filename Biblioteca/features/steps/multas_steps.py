from behave import given, when, then

# Simulación simple en memoria
class Contexto:
    def __init__(self):
        self.dias_retraso = 0
        self.multa = 0
        self.mensaje = ""
        self.bloqueado = False

def before_scenario(context, scenario):
    context.data = Contexto()


@given('un estudiante con 3 días de retraso')
def step_given_3_dias(context):
    context.data.dias_retraso = 3


@when('consulta su multa')
def step_when_consulta_multa(context):
    tarifa = 500
    context.data.multa = context.data.dias_retraso * tarifa

    if context.data.multa == 0:
        context.data.mensaje = "Sin multa pendiente"


@then('el sistema muestra 1500 COP')
def step_then_multa(context):
    assert context.data.multa == 1500


@given('un estudiante sin retrasos')
def step_given_sin_retraso(context):
    context.data.dias_retraso = 0


@then('el sistema muestra "Sin multa pendiente"')
def step_then_sin_multa(context):
    assert context.data.mensaje == "Sin multa pendiente"


@given('un estudiante con multa mayor a 0')
def step_given_con_multa(context):
    context.data.multa = 1000


@when('intenta reservar un libro')
def step_when_reserva(context):
    if context.data.multa > 0:
        context.data.bloqueado = True
        context.data.mensaje = "Tiene deuda pendiente"


@then('el sistema bloquea la reserva')
def step_then_bloqueo(context):
    assert context.data.bloqueado is True


@then('muestra un mensaje de deuda')
def step_then_mensaje(context):
    assert context.data.mensaje == "Tiene deuda pendiente"