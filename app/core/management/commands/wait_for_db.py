"""DJANGO comm to wait for db to be avail"""
import time
from psycopg2 import OperationalError as Psycopg20pError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    " DJango comm to wait for db"

    def handle(self, *args, **options):
        "entrypoint for command"
        self.stdout.write('Wait for db')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20pError, OperationalError):
                self.stdout.write('db unavail, w 1s')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('db av'))
