# seleniumをインポート
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


# メインメソッド
def main():

    # 操作するサイトURL(絶対パスに変換)
    url = "C:/programming/Python/scraping/selenium_pre/src/resources/template/index.html"

    # ドライバーのオプションを生成
    options = webdriver.ChromeOptions()
    # 画面を表示しない
    # options.add_argument('--headless')
    # 処理が終わってもchromeを閉じない
    options.add_experimental_option("detach", True)

    # ドライバーを生成(Chrome)
    # chromeのバージョンに合わせる(第一引数)
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)

    # スクレイピング操作
    scraiping(driver, url)

    # ドライバーをクローズ
    driver.service.stop()


# スクレイピング操作メソッド
def scraiping(driver: webdriver.Chrome, url: str):

    # サイトを取得
    driver.get(url)

    # 処理を1秒中断
    sleep(1)

    '''取得したサイトの情報を表示'''
    # サイトのURL
    print(f"URL:\n{driver.current_url}")
    # サイトのタイトル
    print(f"タイトル:\n{driver.title}")

    ''' menu画面に遷移する '''
    # aタグを取得(タグ名取得)
    a_tag = driver.find_element_by_tag_name("a")

    # aタグをクリック(画面遷移)
    a_tag.click()

    # 処理を1秒中断
    sleep(1)

    '''inputに文字を入れる'''
    # inputタグを取得(XPath取得)
    input_tag = driver.find_element_by_xpath("/html/body/div[1]/input[1]")

    # inputタグに値を入れる
    input_tag.send_keys("HelloWorld")

    # 処理を1秒中断
    sleep(1)

    # buttonタグを取得(id名取得)
    button_tag = driver.find_element_by_id("button1")

    # buttonを起動
    button_tag.click()

    '''表の値をすべてコンソール出力'''
    # 表の値であるtdタグを全取得(class名全取得)
    td_tags = driver.find_elements_by_class_name("favoriteHuman")

    # 取得したtdタグの数繰り返し
    for i in range(len(td_tags)):
        print(str(i + 1) + ":" + td_tags[i].text)


# 実行時呼び出し
if __name__ == "__main__":
    main()
