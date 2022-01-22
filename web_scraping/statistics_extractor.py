def extract(prod_soup):
    statistics = []

    container = prod_soup.find("div", class_="lot-info")

    texts = container.find_all("p")
    if container != None:
        st = texts[1].text
        deyer = st.split(': ')[1]
        statistics.append(deyer)


    return statistics