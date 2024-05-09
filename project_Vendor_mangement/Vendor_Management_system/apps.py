from django.apps import AppConfig


class VendorManagementSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Vendor_Management_system'

    def ready(self):
        import Vendor_Management_system.signals

