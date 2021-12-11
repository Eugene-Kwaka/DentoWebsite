from django.apps import AppConfig


class DentistConfig(AppConfig):
    name = 'dentist'

    def ready(self):
        import dentist.signals
