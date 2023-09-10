# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd


def main():
    # WebDriverのパスを指定（必要に応じて変更してください）
    webdriver_path = '/usr/local/Caskroom/chromedriver/116.0.5845.96/chromedriver-mac-x64/chromedriver'

    # WebDriverを起動
    driver = webdriver.Chrome(service=Service(webdriver_path))
    sessions = []
    titles = []
    abstracts = []

    for session_num in range(1, 19):
        # 指定されたURLを開く
        driver.get(f'https://recsys.acm.org/recsys23/session-{session_num}/')

        # ページが完全にロードされるのを待つ
        time.sleep(5)

        session_element = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/h3')
        session = session_element.text

        for i in range(1, 7):
            print(f'try: {i}')
            try:
                title_element = driver.find_element(By.XPATH, f'//*[@id="accordion-1"]/li[{i}]/a')
                title = title_element.text.split('\n')[1]

                abstract_element = driver.find_element(By.XPATH, f'//*[@id="accordion-1"]/li[{i}]/div')
                plus = driver.find_element(By.XPATH, f'//*[@id="accordion-1"]/li[{i}]')
                driver.execute_script("arguments[0].setAttribute('class', 'current')", plus)
                driver.execute_script("arguments[0].setAttribute('style', 'display: block')", abstract_element)
                abstract = abstract_element.text.replace('\n', ' ')

                print('\t'.join([session, title, abstract]))
                sessions.append(session)
                titles.append(title)
                abstracts.append(abstract)
            except:
                pass

    # dataframeに変換
    result_df = pd.DataFrame({'session': sessions, 'title': titles, 'abstract': abstracts})
    result_df.to_csv('../data/recsys23_data.tsv', index=False, sep='\t')

    # WebDriverを終了
    driver.quit()


if __name__ == '__main__':
    main()
