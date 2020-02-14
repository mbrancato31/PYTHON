import csv

# with open("python\\course\\7\\data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transacion_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])

with open("python\\course\\7\\data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
