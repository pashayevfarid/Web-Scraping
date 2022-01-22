def extract(prod_soup):
    photos = []

    container = prod_soup.find("div", class_="photos")

    images = container.find_all("a")
    url = 'https://tap.azstatic.com/uploads/full/'
    for image in images:
        photos.append(image["href"].split("full/")[1])

    return photos