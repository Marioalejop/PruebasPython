class DashboardPage:
    def __init__(self, page):
        self.page = page

        self.task_input = "#taskInput"
        self.add_btn = "#addTask"
        self.tasks = ".task-item"
        self.filter = "#filter"
        self.logout_btn = "#logout"

    def esta_en_dashboard(self):
        return "/dashboard" in self.page.url

    def crear_tarea(self, texto):
        self.page.fill(self.task_input, texto)
        self.page.click(self.add_btn)

    def obtener_tareas(self):
        return self.page.locator(self.tasks).all_text_contents()

    def filtrar(self, valor):
        self.page.select_option(self.filter, valor)

    def logout(self):
        self.page.click(self.logout_btn)