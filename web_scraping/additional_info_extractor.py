def extract(prod_soup):
    attributes = []

    container = prod_soup.find("div", class_="lot-text")

    prod_texts = container.find_all("p")

    if container != None:
        for prod_text in prod_texts:
            attributes.append(prod_text.text.replace("\n", ". "))

    return attributes