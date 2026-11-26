from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Очищает БД и заполняет её тестовыми данными из фикстуры'

    def handle(self, *args, **options):
        # Удаляем существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загружаем данные из фикстуры
        call_command('loaddata', 'catalog_data.json')

        self.stdout.write(self.style.SUCCESS('База данных успешно очищена и заполнена!'))
