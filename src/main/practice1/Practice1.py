from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


''' 
インスタグラムにログインする
前提条件：
mainメソッドの入力値にログイン可能な「インスタログインID」と「インスタログインPW」を入力 
'''


# メイン
def main():
    '''入力値'''
    # インスタログインID # TODO
    login_id = ""
    # インスタログインPW # TODO
    login_pw = ""
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
    options.add_experimental_option("detach", True)

    # ドライバーを生成(Chrome) # TODO
    driver = None

    return driver


# スクレイピング(インスタログイン)
def scraiping(driver: webdriver.Chrome, login_id: str, login_pw: str):
    '''インスタにログイン'''
    # ログイン画面URL
    url_login = "https://www.instagram.com/"

    # ログイン画面に接続 # TODO (コメントを外して~~~を正しく記載)
    # driver.~~~(~~~)

    # 1秒待機
    sleep(1)

    # inputタグをタグ名で全取得(そのうち0番目がログインID,1番目がログインPW) # TODO 後続の処理に合わせて記載。
    login_input_tags = None

    # ログインIDを入力
    login_input_tags[0].send_keys(login_id)

    # 1秒待機
    sleep(1)

    # ログインPWを入力
    login_input_tags[1].send_keys(login_pw)

    # 1秒待機
    sleep(1)

    # formタグをidで取得 # TODO
    login_form_tag = None

    # フォームをsubmit # TODO (コメントを外して~~~を正しく記載)
    # login_form_tag.~~~(~~~)


# 実行時呼び出し
if __name__ == "__main__":
    main()
