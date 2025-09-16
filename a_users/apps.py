from django.apps import AppConfig

from a_core.utils import maybe_unused


class AUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "a_users"

    def ready(self) -> None:
        import a_users.signals

        maybe_unused(a_users.signals)
