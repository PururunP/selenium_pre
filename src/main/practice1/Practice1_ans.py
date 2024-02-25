from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


''' 
【解答版】
インスタグラムにログインする
前提条件：
mainメソッドの入力値にログイン可能な「インスタログインID」と「インスタログインPW」を入力 
'''


# メイン
def main():
    '''入力値'''
    # インスタログインID
    login_id = "sample@~~~.~~"
    # インスタログインPW
    login_pw = "password"
    ''''''

    # ドライバ取得
    driver = get_selenium_driver()
    print("ドライバー生成成功")

    # スクレイピング開始
    scraiping(driver, login_id, login_pw)

    # ドライバークローズ(driverのみクローズするため、オプションでdetachをTrueにしているならchromeは開きっぱなしとなる)
    driver.service.stop()
    print("ドライバークローズ成功")


# seleniumのドライバーを生成し返却
def get_selenium_driver():

    # ドライバーのオプションを生成
    options = webdriver.ChromeOptions()
    # 画面を表示しない
    # options.add_argument("--headless")
    # 処理が終わってもchromeを閉じない
    # options.add_experimental_option("detach", True)

    # ドライバーを生成(Chrome)
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)

    return driver


# スクレイピング(インスタログイン)
def scraiping(driver: webdriver.Chrome, login_id: str, login_pw: str):
    '''インスタにログイン'''
    # ログイン画面URL
    url_login = "https://www.instagram.com/"

    # ログイン画面に接続
    driver.get(url_login)

    # 1秒待機
    sleep(1)

    # inputタグを全取得(そのうち0番目がログインID,1番目がログインPW)
    login_input_tags = driver.find_elements_by_tag_name("input")

    # ログインIDを入力
    login_input_tags[0].send_keys(login_id)

    # 1秒待機
    sleep(1)

    # ログインPWを入力
    login_input_tags[1].send_keys(login_pw)

    # 1秒待機
    sleep(1)

    # formタグをidで取得
    login_form_tag = driver.find_element_by_id("loginForm")

    # フォームをsubmit
    login_form_tag.submit()


# 実行時呼び出し
if __name__ == "__main__":
    main()
