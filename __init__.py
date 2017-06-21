from django.apps import AppConfig
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from pretix import __version__ as version


class TicketOutputPdfApp(AppConfig):
    name = 'pretix.plugins.ticketoutputpdf'
    verbose_name = _("SHA PDF ticket output")

    class PretixPluginMeta:
        name = _("SHA PDF ticket output")
        author = _("Martin Gross, the pretix team")
        version = version
        description = _("This plugin allows you to print out tickets as PDF files - with the addition of SHA-related tax-stuff")

    def ready(self):
        from . import signals  # NOQA

    @cached_property
    def compatibility_errors(self):
        errs = []
        try:
            import reportlab  # NOQA
        except ImportError:
            errs.append("Python package 'reportlab' is not installed.")
        return errs


default_app_config = 'pretix.plugins.ticketoutputpdf.TicketOutputPdfApp'
