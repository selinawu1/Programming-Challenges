import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"


def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def tracks(html, top):
    i = 0
    dictionary = {}
    for x in range(int(top)):
        open_tr = html.find('<tr>', i)
        close_tr = html.find('</tr>', open_tr)

        newstring = html[open_tr:close_tr]
        lookingfor = '"position">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        pos = newstring[pos_start + len(lookingfor):pos_end]

        open_ta = html.find('<div class="title-artist">', i)
        close_ta = html.find('</td>', open_ta)

        title_artist = html[open_ta: close_ta]
        open_div = title_artist.find('<a href=', title_artist.find('<div class="title">'))
        close_div = title_artist.find('</div>', open_div)
        track_str = title_artist[open_div: close_div]
        track = track_str[track_str.find('>') + 1:track_str.find('</a>')]

        open_div2 = title_artist.find('<a href=', title_artist.find('<div class="artist">'))
        close_div2 = title_artist.find('</div>', open_div2)
        artist_str = title_artist[open_div2: close_div2]
        artist = artist_str[artist_str.find('>') + 1:artist_str.find('</a>')]

        if pos not in dictionary:
            dictionary[pos] = ['', '']

        dictionary[pos][0] = track
        dictionary[pos][1] = artist

        i = close_tr
    return dictionary


if __name__ == "__main__":
    html = scrape(url)
    list = tracks(html, 10)
    print(f"{'Position':<15}{'Title':<35}{'Artist':<35}")
    for key, value in list.items():
        title, artist = value
        print(f"{key:<15}{title:<35}{artist:<35}")
