def extract(prod_soup):
    months = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avqust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
    questions = []
    username = []
    time = []
    result2 = []
    i=0
    result = dict()
    times = prod_soup.find_all("time")
    user_name = prod_soup.find_all("div", class_="user_name")
    Body = prod_soup.find_all("div", class_="body")
    conversation = prod_soup.find_all("div", class_="conversation")
    if conversation != None:
        for question in Body:
            questions.append(question.text)
        for person in user_name:
            username.append(person.string)
        for date in times:

            time.append(date.text)
        while i < len(questions):
            result2.append(time[i])
            result2.append(username[i])
            result2.append(questions[i])
            i+=1
    return result2



