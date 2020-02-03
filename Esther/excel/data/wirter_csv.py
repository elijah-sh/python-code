import csv


def writer():
    with open('D:/tmp/data/data.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['HELLO', 'WORLD'])


if __name__ == '__main__':
    writer()