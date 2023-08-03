from bs4 import BeautifulSoup
import requests
import json
import hashlib

cookie_value = 'visitor=14177777673173596450; _pbjs_userid_consent_data=3524755945110770; _lr_env_src_ats=false; _gcl_au=1.1.1729084667.1690122804; TREK_SESSION=db70a9f2-239f-4069-2222-c8f397792120; _tfpvi=ZGMwYzM3NjUtYzg3MC00ZTc5LWIwNDgtZDIzNmEwY2Q2NjhmIy03LTk%3D; ucf_uid=51d7ac7a-34f9-451a-a4e6-2db6693d94dd; _cc_id=ffac014ea85054ee13c8952f7c124da1; _fbp=fb.1.1690122804550.893930502; ad2udid=64bd39eaeb8821.490855561c10dbd77ee11f6520eabe360ca7e7f4; _im_vid=01H61N7S8E69R7J0P5D8DVRTF3; _ss_pp_id=4772d623ac8572e2c021690096661436; _td=29ff9907-709e-413b-8c66-457a18f1d5f3; _clck=1gdkc8t|2|fdl|0|1299; __gads=ID=2d5d63562d873ad1-224d78afb1e70016:T=1690122807:RT=1690299065:S=ALNI_MYD7RYxZWxLHvPZe8W9no7Xzy2epw; __gpi=UID=00000c237ed2ff29:T=1690122807:RT=1690299065:S=ALNI_MYvhYq9ihbBSL7jz_HkYWeaYluOTA; CF-IPCountry=HK; _lr_retry_request=true; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.673578729.1690299070; panoramaId_expiry=1690385469717; panoramaId=ecd8270fe723ad514b73e1a60d19a9fb927ace85080cd19a6a263ad1cf2cc8fd; ad2session=d8fc70d0-1d55-439a-a009-48e977cb2e70; _lr_geo_location_state=; _lr_geo_location=HK; cto_bundle=b7BvQV9MJTJGQXZHVzFOMTk0UlV2YzFnd1VNM1JnMW9yJTJCSTJQanhkTUI5Vk84bzZhMFQ2YzQySXJnSSUyQjNMYkk2eXJsQWVTUGNTT2txVXlhZU1DUTlCSkUxTTMwcTJqbUN1VDVtbE5IaXY1enJyamxkUmZVV3BnJTJCdHZPTmlyc2FwYmlYTjN2aERVcGFDNjUzME00ZEo3VWluciUyRkFBJTNEJTNE; sent-cid=1690299140; CSRF-TOKEN=wPVHnxngMgBpLz%2FD8zO%2Fc0CqIknwZcvUDQcQWZOdAHxwsaJQ4OGJKrCj5CRpChC4J8nOdV6wRlxjKqcKWmrk6Q%3D%3D; _icook_sess=Tm0wWG85cFQrVlBkaXdrZjV5R0U2cHhXZ0lDeENWdDRVQml6T2hwdU9VMHkrUkZoRlRNVHY1d0F6cU0vbGxiSDJ4RCt4blhjdXlpbHRSOXlIK1hxRHJmVi9ka0EvQTZPWGozWW1sNDVxanlZVjJQcjA2Ykx5TDhJL1FCejNlelBBREIrN2xGeUl1anRwK3FRUzJkRWwyd0pLMjZvd2Y1RklHT2RNVFBVY09leWhQNmNXdXZ5OTdmamhnTDRCVTFCcFJGSEQ0T2hXSVdBdGVsMjk3YnE2UmVDNkdUbDhwdXpBRlNxajRheWQ5akRhWDQ4ZnRtR3VsYzBKY0JNcFMwdjBKVG9uVnRYbkRlMWdGVElqZVNPRGtJSmNTSFRkRnF0dXpXVy9PdTJMRkR1U1FHelUxc1g3WGMyam1YU040UWI1SmNrc05ZQjRkTGNhVWFjYk9YQ2N6WjBVdTg3bGRwaE9KT3VzS3lVZmswPS0tVWswWUJ0ZE54ekI3dG5KUzlheU0rUT09--bfe5c397a0223b3c63c37ab7c4e1ddd6d505e211; _ga=GA1.1.233676984.1690122804; _ga_JGPGC2WD9R=GS1.1.1690299065.3.1.1690299185.0.0.0; _ga_1VWKN3HFXY=GS1.2.1690299072.3.1.1690299186.0.0.0; _ga_Q65WJCEHK3=GS1.1.1690299065.4.1.1690299803.60.0.0; _ga_ZKZX6M179R=GS1.1.1690299067.4.1.1690299803.60.0.0; _clsk=1q82vfk|1690299805862|4|1|u.clarity.ms/collect'
cookies = {'Cookie': cookie_value}

# Define the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

def fetchlinks( page ):
    url = "https://icook.tw/recipes/popular?page=%d" % (page)
    response = requests.get(url, cookies=cookies, headers=headers)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    all_paragraphs = soup.find_all(class_='browse-recipe-link')
    for paragraph in all_paragraphs:
        print(paragraph["href"])


def getAllLinks():
    for num in range(1,6):
        fetchlinks(num)


def getJson(url):
    hash_object = hashlib.md5(url.encode())
    hex_dig = hash_object.hexdigest()
    print(url)
    response = requests.get(url, cookies=cookies, headers=headers)
    html_content = response.content
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')
    script = soup.find(type='application/ld+json')
    if script is not None:
        result = {"code": 0,"msg":"success"}

        data = json.loads(script.string)
        data.pop('@context', None)
        recipeObj = data["@graph"][0]

        recipeObj.pop('image', None)
        recipeObj.pop('datePublished', None)
        recipeObj.pop('dateModified', None)
        steps = recipeObj["recipeInstructions"]
        for value in steps:
            value.pop('url', None)
        
        recipe_name = soup.find('h1', {'id': 'recipe-name', 'class': 'title'})
        preload_image = soup.find('link', {'rel': 'preload', 'as': 'image'})
        # print(recipe_name.text)
        # print(preload_image["href"])
        recipeObj["name"] = recipe_name.text.strip()
        recipeObj["cover"] = preload_image["href"]
        
        recipeObj["url"] = url
        recipeObj["digit"] = hex_dig
        recipeObj["author"] = official

        simple = recipeObj.copy()
        simple.pop('url', None)
        simple.pop('recipeIngredient', None)
        simple.pop('recipeInstructions', None)
        simple.pop('description', None)

        simple_list.append(simple)

        # 写入文件
        result["data"] = recipeObj
        with open(hex_dig, "w") as f:
            json.dump(result, f)
    else:
        print('No JSON-LD data found on the page.')

def getfn(page):
    filename = "page_" + str(page) + ".json"
    hash_object = hashlib.md5(filename.encode())
    return hash_object.hexdigest()

simple_list = []
official = {"@type": "Official", "name": "爱料理", "url": "https://woiads.com/img/chefathome.png"}
#0726
# "https://icook.tw/recipes/442681","https://icook.tw/recipes/442357","https://icook.tw/recipes/442303","https://icook.tw/recipes/441702","https://icook.tw/recipes/442103","https://icook.tw/recipes/441832","https://icook.tw/recipes/442606","https://icook.tw/recipes/442200","https://icook.tw/recipes/442190","https://icook.tw/recipes/442030","https://icook.tw/recipes/441942","https://icook.tw/recipes/442067","https://icook.tw/recipes/442744","https://icook.tw/recipes/442022","https://icook.tw/recipes/442329","https://icook.tw/recipes/442017","https://icook.tw/recipes/442486","https://icook.tw/recipes/441706","https://icook.tw/recipes/442044","https://icook.tw/recipes/441940","https://icook.tw/recipes/441861","https://icook.tw/recipes/441688","https://icook.tw/recipes/442258","https://icook.tw/recipes/442598","https://icook.tw/recipes/442483","https://icook.tw/recipes/442413","https://icook.tw/recipes/441480","https://icook.tw/recipes/409097","https://icook.tw/recipes/441926","https://icook.tw/recipes/441992","https://icook.tw/recipes/441996","https://icook.tw/recipes/442596","https://icook.tw/recipes/442410","https://icook.tw/recipes/442578","https://icook.tw/recipes/442610","https://icook.tw/recipes/442618","https://icook.tw/recipes/442505","https://icook.tw/recipes/442396","https://icook.tw/recipes/442209","https://icook.tw/recipes/442210","https://icook.tw/recipes/441510","https://icook.tw/recipes/442220","https://icook.tw/recipes/442638","https://icook.tw/recipes/442005","https://icook.tw/recipes/442278","https://icook.tw/recipes/442488","https://icook.tw/recipes/442282","https://icook.tw/recipes/442397","https://icook.tw/recipes/442756","https://icook.tw/recipes/439684","https://icook.tw/recipes/442309","https://icook.tw/recipes/442613","https://icook.tw/recipes/442395","https://icook.tw/recipes/442679","https://icook.tw/recipes/442307","https://icook.tw/recipes/442233","https://icook.tw/recipes/442683","https://icook.tw/recipes/441794","https://icook.tw/recipes/442806","https://icook.tw/recipes/442717","https://icook.tw/recipes/442631","https://icook.tw/recipes/442463","https://icook.tw/recipes/442591","https://icook.tw/recipes/441737","https://icook.tw/recipes/442720","https://icook.tw/recipes/442730","https://icook.tw/recipes/442696","https://icook.tw/recipes/441900","https://icook.tw/recipes/442587","https://icook.tw/recipes/442860","https://icook.tw/recipes/442561","https://icook.tw/recipes/442588","https://icook.tw/recipes/442437","https://icook.tw/recipes/441868","https://icook.tw/recipes/441950","https://icook.tw/recipes/442647","https://icook.tw/recipes/442414","https://icook.tw/recipes/441829","https://icook.tw/recipes/442218","https://icook.tw/recipes/441974",
recipe_list = ("https://icook.tw/recipes/441724","https://icook.tw/recipes/441859","https://icook.tw/recipes/442241","https://icook.tw/recipes/441953","https://icook.tw/recipes/442852","https://icook.tw/recipes/441466","https://icook.tw/recipes/442412","https://icook.tw/recipes/441764")
#"https://icook.tw/recipes/442570","https://icook.tw/recipes/442837",
page = 9
print("------" + str(page) + " > " + getfn(page) + "----------")
for recipe in recipe_list:
    getJson(recipe)
    if len(simple_list) == 10:
        filename = getfn(page)
        page = page + 1
        nextfn = getfn(page)
        result = {"code": 0,"msg":"success", "next_page": nextfn}
        result["data"] = simple_list
        with open(filename, "w") as f:
            json.dump(result, f)
        simple_list = []
        print("------" + str(page) + " > " + getfn(page) + "----------")

if len(simple_list) > 0:
    filename = getfn(page)
    result = {"code": 0,"msg":"success"}
    result["data"] = simple_list

    with open(filename, "w") as f:
        json.dump(result, f)
    simple_list = []

