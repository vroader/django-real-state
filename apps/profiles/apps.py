from django.apps import AppConfig

'''Configura a aplicação profiles garantindo que os sinais definidos
   em signals.py sejam carregados quando a aplicação for carregada,
   Permitindo que o Django execute automaticamente a criação de um
   perfil quando um usuário for criado
'''


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.profiles'

    def ready(self):
        from apps.profiles import signals
