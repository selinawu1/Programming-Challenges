import csv
from pathlib import Path

csv_file = Path("south.csv")


def read_csv(path):
    csv_contents = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents.append(row)
    return csv_contents


def read_html(path):
    fp = open(path)
    mystr = fp.read()
    fp.close()
    return mystr


def process(csv, html):
    x = 0
    csv_contents = {}
    for row in csv:
        x += 1
        link, initial, name = row[0], row[1], row[2]
        csv_contents[x] = ["", "", ""]
        csv_contents[x][0] = link
        csv_contents[x][1] = initial
        csv_contents[x][2] = name

    for i in range(1, 6):
        html = html.replace(f"link{i}", csv[i - 1][0])

    for j in range(1, 6):
        html = html.replace(f"initials{j}", csv[j - 1][1])

    for k in range(1, 6):
        html = html.replace(f"name{k}", csv[k - 1][2])

    return html


def write_html(path, html):
    with open(path, "w") as f:
        file = f.write(html)
        f.close()
    return file


if __name__ == "__main__":
    csv = read_csv(path="south.csv")
    html = read_html(path="south.html")
    html = process(csv=csv, html=html)
    write_html(path="south_final.html", html=html)
