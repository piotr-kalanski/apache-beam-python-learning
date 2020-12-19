import csv

import apache_beam as beam


def print_row(element):
    print(element)


def parse_file(element):
  for line in csv.reader([element], quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    return line


with beam.Pipeline() as p:
    parsed_csv = (
        p 
        | 'Read input file' >> beam.io.ReadFromText("data/people.csv")
        | 'Parse file' >> beam.Map(parse_file)
        | 'Print output' >> beam.Map(print_row)
    )
