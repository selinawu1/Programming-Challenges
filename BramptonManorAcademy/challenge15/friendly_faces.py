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

    i = 0
    links = []
    for _ in range(len(csv_contents)):
        open = html.find('link', i)
        close = html.find('");', open)
        links.append(html[open: close])
        i = close

    j = 0
    initials = []
    for _ in range(len(csv_contents)):
        open = html.find('initial', j)
        close = html.find('</h2>', open)
        initials.append(html[open: close])
        j = close

    k = 0
    names = []
    for _ in range(len(csv_contents)):
        open = html.find('name', k)
        close = html.find('</div>', open)
        names.append(html[open: close])
        k = close

    z = 0
    for y in range(1, len(csv_contents)+1):
        html = html.replace(links[z], csv_contents[y][0])
        html = html.replace(initials[z], csv_contents[y][1])
        html = html.replace(names[z], csv_contents[y][2])
        z += 1

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
