import logging

from django.core.management import BaseCommand
from django.utils import timezone

"""
※ Djangoのバッチプログラムを作成するためのテンプレート

[usage] python manage.py check -period 2021-03 -dir media/outdata -file abc.csv
・複数のバッチプログラムを作成しても、クラス名は「class Command(BaseCommand):」の部分は同じにする。
"""


class Command(BaseCommand):
    help = '[Usage] $ python manage.py check -period 2021-03 -dir media/outdata -file abc.csv'

    def add_arguments(self, parser):
        parser.add_argument('-period', nargs='+', type=str)  # registered -period 2-2306
        parser.add_argument('-dir', type=str)   # registered -dir media/outdata
        parser.add_argument('-file', type=str)  # registered -file abc.csv
        parser.add_argument('-id', type=int)    # registered -id 1

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        logger.debug("check--debug--Level")
        logger.error('check--error--Level')

        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)

        print('Period= ', options['period'])
        print('dir= ', options['dir'])
        print('file=', options['file'])
        print('id= ', options['id'])
