from django.core.management.base import BaseCommand, CommandError
import random
from activityapi.models import Activity
from faker import Faker
# from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Activity database Creation.'

    def add_arguments(self, parser):

        parser.add_argument(
            'activities',
            type=int,
            default=20,
            help="Number of activities to generate and save to database"
        )
    
    # def gen_datetime(self, min_year=2010, max_year=datetime.now().year):
    # # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    #     start = datetime(min_year, 1, 1, 00, 00, 00)
    #     years = max_year - min_year + 1
    #     end = start + timedelta(days=365 * years)
    #     return start + (end - start) * random.random()

    def handle(self, *args, **options):
        try:
            # records = []
            fake = Faker()
            size = options['activities']

            if size < 0 or size > 10000:
                raise CommandError("You can only generate 1-10000 activity records at a go")

            for _ in range(size):
                startTime = fake.date_time_between(start_date='-20y', end_date='now')
                endTime = fake.date_time_between(start_date=startTime, end_date='now')

                Activity.objects.create(start_time=startTime, end_time=endTime)

            #     kwargs = {
            #         'start_time': startTime,
            #         'end_time': endTime
            #     }
            #     record = Activity(**kwargs)
            #     records.append(record)
            # Activity.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS('Activity records saved successfully.'))
            
        except Exception as e:
            raise CommandError(repr(e))