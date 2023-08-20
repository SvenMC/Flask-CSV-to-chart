import random
import os


class UniqueFileValidator:

    assets_path = r'assets'
    assets_chart_path = r'assets\charts'
    uploads_path = r'uploads'

    def validate_uploads(self):
        count = 0
        while True:
            val = random.randint(100000000000, 999999999999)
            file_name = f'{val}.csv'

            if file_name not in os.listdir(self.uploads_path):
                return file_name

            if count > 100:
                return None

            count += 1
