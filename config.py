import os


class Config:
    def __init__(self):
        self.debug = self._bool('DEBUG', False)
        self.port = self._int('PORT', 8080)
        self.db_url = os.environ.get('DATABASE_URL', 'sqlite:///app.db')

    def _bool(self, key, default=False):
        return os.environ.get(key, str(default)).lower() in ('1', 'true', 'yes')

    def _int(self, key, default=0):
        try:
            return int(os.environ.get(key, default))
        except ValueError:
            return default
