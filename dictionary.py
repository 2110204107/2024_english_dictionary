import requests
from bs4 import BeautifulSoup

def read(word):
#     word = input('請輸入要查詢的英文單字: ')
    url = f'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/{word}'

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    headers = {'User-Agent': user_agent}

#     print(word+'的查詢結果：')

    try:
        web_request = requests.get(url, headers=headers)
        bs = BeautifulSoup(web_request.text, "html.parser")

        means = bs.find_all("div", class_="entry-body__el")


        if means:
            for mean in means:
                posgram = mean.find('div', class_="posgram").text.strip()
                sen = f'{posgram}:'

                def_bodies = mean.find_all("div", class_="def-body")

                if def_bodies:
                    i = 1
                    for def_body in def_bodies:
                        translation = def_body.find('span').text.strip()
                        sen += f'{i}. {translation}'
                        i += 1
                    return sen
                else:
                    return('查無此字。')
        else:
            return('查無此字。')

    except error:
        return('查無此字')
