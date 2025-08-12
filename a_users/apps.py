from django.apps import AppConfig


class AUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "a_users"

    def ready(self) -> None:
        import a_users.signals

        # This code snippet is needed here just to make Pyright and Ruff
        # happy, to force them to stop complaining about unused/unaccessed
        # module a_users.signals
        if a_users.signals.Profile.DoesNotExist:
            pass
