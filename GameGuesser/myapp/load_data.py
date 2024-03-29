import csv
from myapp.models import MyModel

with open('vgsales.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        _, created = MyModel.objects.get_or_create(
            Rank=row[0],
            Name=row[1],
            Platform=row[2],
            Year=row[3],
            Genre=row[4],
            Publisher=row[5],
            NA_Sales=row[6],
            EU_Sales=row[7],
            JP_Sales=row[8],
            Other_Sales=row[9],
            Total_Sales=row[10],
           
        )
