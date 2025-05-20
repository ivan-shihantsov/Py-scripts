import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

storage_f = "data.json"
url_base = "https://www.mymarket.ge/ka/search/?UserID="
min_user = 0
max_usrs = 9999999 # 9999999
skip_users = 0
users_done = 0


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

find_name = ".//div[contains(@class, 'shop-name')]/span"


def get_app_num():
    card_num = driver.find_element(By.ID, "searchProducts").find_element(By.CLASS_NAME,"mr-8px").text
    if card_num == "":
        return 0
    return card_num


def write_data(user_ID, username, card_num):
    print(f"page UserID: {user_ID}")
    print(f"username: {username}")
    print(f"cards num: {card_num}")
    print()

    with open(storage_f, 'r') as storage_file:
        data = json.load(storage_file)

    val = [username, card_num]
    data.update({user_ID: val})

    with open(storage_f, 'w') as storage_file:
        json.dump(data, storage_file)



def parse_link(link, user_ID):
    global skip_users, users_done
    try:
        username = driver.find_elements(By.XPATH, find_name)[0].text
    except:
        print(f"issue on user_ID: {user_ID}. repeat")
        return -1
    
    if username == "null null":
        skip_users += 1
        pass
    else:
        card_num = get_app_num()
        if card_num == 0:
            skip_users += 1
            pass
        else:
            users_done += 1
            write_data(user_ID, username, card_num)


def prep_links():
    for i in range(min_user, max_usrs + 1):
        user_ID = "%07d" % i
        url = url_base + user_ID
        #url = "https://www.mymarket.ge/ka/search/?UserID=752770"

        # make get request here and then only parse the results
        driver.get(url)
        time.sleep(3)
        #wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        #wait.until(EC.presence_of_element_located((By.XPATH, find_name)))

        successful = False
        while not successful:        
            res = parse_link(url, user_ID)
            if res == -1:
                pass
            else:
                successful = True
    
    print("total users parsed:", max_usrs + 1 - min_user)
    print("users skipped:", skip_users)
    print("users OK:", users_done)


def main():
    prep_links()


if __name__ == "__main__":
    main()
