from django.core.management.base import BaseCommand, CommandError
import random
from faker import Faker
from activityapi.models import User, Timezone, Activity

class Command(BaseCommand):
    help = 'Users database Creation.'

    def add_arguments(self, parser):

         parser.add_argument(
            'users',
            type=int,
            default=20,
            help="Number of users to generate and save to database."
        )

    def get_timezone(self, timezone = Timezone):
        tzo = random.choice(timezone.objects.all())
        return tzo
    
    def get_activity(self, activity = Activity):
        acti_peri= list(set(random.choices(activity.objects.all(), k=random.randint(1, 10))))
        return acti_peri

    def handle(self, *args, **options):
        try:
            fake = Faker()
            size = options['users']

            if size < 0 or size > 10000:
                raise CommandError("You can only generate 1-10000 user records at a go")

            for _ in range(size):
                instance = User.objects.create(tz=self.get_timezone(), real_name=fake.name())
                instance.activity_periods.set(self.get_activity())
            self.stdout.write(self.style.SUCCESS('User records saved successfully.'))
            
        except Exception as e:
            raise CommandError(repr(e))