import csv
from django.core.management import BaseCommand
from MyApp1.models import teacher
from MyApp1.models import courses

class Command(BaseCommand):
    help = "Help text not found... Sorry!"

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
        parser.add_argument('--model', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        model = kwargs['model']
        with open(path, 'rt', encoding='utf-8-sig') as f:
            reader = csv.reader(f, dialect='excel')
            count = 0
            if model:
                for row in reader:
                    model.objects.create(Name=row[0],Area=row[1])
                    count=+1
                print('Successfully imported ' + str(count) + ' new entries!')
            else:
                print('No model specified! Import failed')