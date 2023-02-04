import requests
from bs4 import BeautifulSoup

url = 'https://jkt48.com/member/list?lang=id'

# get data
def get_data(url):
    r = requests.get(url)
    return r.text

# process data
def parse(data):
    result = []
    soup = BeautifulSoup(data, 'html.parser')
    contents = soup.find('div', attrs={'class': 'row row-all-10'})
    members = contents.find_all('a', href=True)
    print(members)
    # print(result)
    for member in members:
        # parsing data
        link = member['href']
        name = member.text.strip()
        # pic = member.find('img').text.strip()
        # print(pic)
        # pic = member.find('img')['src']
        # name = " ".join(name.split())
        # br = member.find_next_sibling('br')
        # if br:
        #     name = name + br.text.strip()
        # if member.find_next_sibling('br'):
        #     name = name + member.find_next_sibling().text.strip()
        # print(name) this is for debugging

        if name:
            dataDict = {
                'name': name,
                # 'pic': pic,
                'link': link,
            }
            result.append(dataDict)

        # append data
            result.append(dataDict)
    return result

def output(datas: list):
    for i in datas:
        print(i)

if __name__ == '__main__':
    data = get_data(url)
    finalData = parse(data)
    output(finalData)