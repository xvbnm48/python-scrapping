import requests
from bs4 import BeautifulSoup

url = 'https://jkt48.com/member/list?lang=id'

# get data
def get_data(url):
    r = requests.get(url)
    print(r)
    return r.text

# process data
def parse(data):
    result = []
    soup = BeautifulSoup(data, 'html.parser')
    contents = soup.find('div', attrs={'class': 'row row-all-10'})
    img_tags = contents.find_all('img')
    link_member = contents.find_all('a', href=True)
    for img_tag, link_member in zip(img_tags, link_member):
        name = img_tag['alt']
        link = "jkt48.com" + img_tag['src']
        link_profile = "jkt48.com" + link_member['href']
        dataDict = {
            'name': name,
            'link foto': link,
            'link-profile': link_profile,
        }
        result.append(dataDict)
    return result

def output(datas: list):
    for i in datas:
        print(i)
        # print("Name", i['name'])
        # print("Link Foto", "https://jkt48.com", i['link foto'])
        # print("Link Profile", "https://jkt48.com",i['link-profile'])
        # print("\n")
if __name__ == '__main__':
    data = get_data(url)
    finalData = parse(data)
    output(finalData)
