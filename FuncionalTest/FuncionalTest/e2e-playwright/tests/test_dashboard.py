from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_crear_tarea(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.abrir()
    login.login("admin", "1234")

    dashboard.crear_tarea("tarea alta")

    tareas = dashboard.obtener_tareas()

    assert "tarea alta" in tareas

def test_filtrar_tareas(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.abrir()
    login.login("admin", "1234")

    dashboard.crear_tarea("tarea alta")
    dashboard.crear_tarea("tarea baja")

    dashboard.filtrar("alta")

    tareas = dashboard.obtener_tareas()

    assert len(tareas) == 1
    assert "alta" in tareas[0]

def test_logout(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.abrir()
    login.login("admin", "1234")

    dashboard.logout()

    assert "index.html" in page.url