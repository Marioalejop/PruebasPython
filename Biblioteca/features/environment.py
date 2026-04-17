def before_scenario(context, scenario):
    class Contexto:
        def __init__(self):
            self.dias_retraso = 0
            self.multa = 0
            self.mensaje = ""
            self.bloqueado = False

    context.data = Contexto()