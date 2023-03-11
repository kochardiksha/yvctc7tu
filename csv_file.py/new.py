import csv
header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']
with open('name.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('newfile.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
      for line in csv_reader:
          csv_writer.writerow(line)
