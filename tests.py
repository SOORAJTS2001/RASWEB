from django.test import TestCase

# Create your tests here.
import csv
with open("./tester.csv", 'r') as file:
  csvreader = csv.DictReader(file)
  for row in csvreader:
    print(row)