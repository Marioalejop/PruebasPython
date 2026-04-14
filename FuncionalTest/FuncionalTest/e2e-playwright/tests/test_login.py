from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_exitoso(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.abrir()
    login.login("admin", "1234")

    assert dashboard.esta_en_dashboard()

def test_login_invalido(page):
    login = LoginPage(page)

    login.abrir()
    login.login("admin", "wrong")

    assert "incorrectas" in login.obtener_error().lower()