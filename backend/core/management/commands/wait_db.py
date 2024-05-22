import time

from django.core.management import BaseCommand
from django.db import OperationalError, connection, connections
from django.db.backends.mysql.base import DatabaseWrapper

connection: DatabaseWrapper = connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_con = False

        while not db_con:
            try:
                db_conn = connections['default']
                db_conn.ensure_connection()
                # connections['default'].cursor()
                # connection.ensure_connection()
                db_con = True
            except OperationalError:
                self.stdout.write('Database unavailable, wait 3 seconds')
                time.sleep(3)
        self.stdout.write('Database is available!!!')
