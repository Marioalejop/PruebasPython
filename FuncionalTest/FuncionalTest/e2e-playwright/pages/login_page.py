class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "http://localhost:3000/index.html"

        self.username = "#username"
        self.password = "#password"
        self.login_btn = "#loginBtn"
        self.error_msg = ".error"

    def abrir(self):
        self.page.goto(self.url)

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)

    def obtener_error(self):
        return self.page.text_content(self.error_msg)