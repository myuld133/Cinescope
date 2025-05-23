from api.api_manager import ApiManager

class User:
    def __init__(self, email: str, password: str, roles: list, api: ApiManager):
        self.email = email
        self.password = password
        self.roles = roles
        self.api = api  # Сюда будем передавать экземпляр API Manager для запросов

    @property
    def creds(self):
        """Возвращает словарь (email, password)"""
        return {'email': self.email, 'password': self.password}