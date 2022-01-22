def extract(prod_soup):
    advertisement = []
    container = prod_soup.find("div", class_="lot-expired")
    if container != None:
       advertisement.append(container.text)
    else:
        advertisement.append("Elan aktivdir")
    return advertisement
