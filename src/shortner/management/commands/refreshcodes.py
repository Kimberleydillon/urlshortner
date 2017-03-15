from django.core.management.base import BaseCommand, CommandError
from shortner.models import UrlApp

class Command(BaseCommand):
    help = 'Refreshes all UrlApp shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)


    def handle(self, *args, **options):
        return UrlApp.objects.refresh_shortcodes(items=options['items'])
