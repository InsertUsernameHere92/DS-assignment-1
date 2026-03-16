from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Min
from MyApp1.models import teacher
from MyApp1.models import courses

class Command(BaseCommand):
    help = "This is some help text"
    
    def add_arguments(self, parser):
        # Set up 2 arguments so we can have a bit more control over everything
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--del', action='store_true')
        parser.add_argument('--model', type=str)
    
    def handle(self, *args, **options):
        model = options['model']

        if model == 'teacher':
            duplicate_field = 'Name'
            keep_ids = teacher.objects.values(duplicate_field).annotate(
                min_id=Min('id')
            ).values_list('min_id', flat=True)
            to_delete = teacher.objects.exclude(id__in=keep_ids)
            count = to_delete.count()
            if options['list']:
                if to_delete:
                    for teach in to_delete:
                        print(teach.Name)
                else:
                    print('No duplicates found')
            if options['del']:
                with transaction.atomic():
                    to_delete.delete()
                    self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} duplicate items.'))
        if model == 'courses':
            duplicate_field = 'Title'
            keep_ids = courses.objects.values(duplicate_field).annotate(
                min_id=Min('id')
            ).values_list('min_id', flat=True)
            to_delete = courses.objects.exclude(id__in=keep_ids)
            count = to_delete.count()
            if options['list']:
                if to_delete:
                    for course in to_delete:
                        print(course.Title)
                else:
                    print('No duplicates found')
            if options['del']:
                with transaction.atomic():
                    to_delete.delete()
                    self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} duplicate items.'))