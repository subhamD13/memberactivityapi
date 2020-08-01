from django.core.management.base import BaseCommand, CommandError
import pytz
from activityapi.models import Timezone



class Command(BaseCommand):
    help = 'Timezones database Creation.'

    def handle(self, *args, **options):
        try:
            Timezone.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing timezones records are deleted.'))
            for tzo in pytz.all_timezones:
                Timezone.objects.create(tz=tzo)
            self.stdout.write(self.style.SUCCESS('{} Timezones records created!!'.format(len(pytz.all_timezones))))
            
        except Exception as e:
            raise CommandError(repr(e))