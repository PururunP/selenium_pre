from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import datetime
import os
import urllib


''' 
【解答版】
インスタグラムの特定のユーザの上から6枚のトップ画像をダウンロードする
前提条件：
mainメソッドの入力値に検索対象の「インスタユーザ名」を入力 
'''


def main():
    '''入力値'''
    # 検索対象ユーザ名のホームリンク("https://www.instagram.com/〇〇◯"の◯部分)
    target_user_name = ""
    ''''''

    # ドライバ取得
    driver = get_selenium_driver()
    print("ドライバー生成成功")

    # スクレイピング開始
    # ダウンロードする画像リンクリストを返却
    img_link_list = scraiping(driver, target_user_name)

    # ドライバークローズ
    driver.quit()
    print("ドライバークローズ成功")

    # 取得した画像リンクリストをダウンロード
    download_image(img_link_list, target_user_name)


# seleniumのドライバーを生成し返却
def get_selenium_driver():

    # ドライバーのオプションを生成
    options = webdriver.ChromeOptions()
    # 画面を表示しない
    options.add_argument("--headless")
    # 処理が終わってもchromeを閉じない
    options.add_experimental_option("detach", True)

    # ドライバーを生成(Chrome)
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)

    return driver


# スクレイピング(特定のインスタユーザのホーム画面に遷移し、表示されている投稿画像リンクをすべて取得)
def scraiping(driver: webdriver.Chrome, target_user_name: str):
    '''ホーム画面操作'''
    # 操作するユーザのトップ画面に遷移
    driver.get("https://www.instagram.com/" + target_user_name)

    # 処理が終わるまで最大30秒待機(前処理に時間を要するため)
    driver.implicitly_wait(30)

    # ダウンロードする画像リンクリストを宣言
    img_link_list = []

    # 投稿ごとのdivタグをclass名で全取得
    home_div_tags = driver.find_elements_by_class_name("_aagv")

    # 処理が終わるまで最大10秒待機(前処理に時間を要するため)
    driver.implicitly_wait(10)

    # 投稿の数繰り返し
    for home_div_tag in home_div_tags:
        # 投稿の中のimgタグを取得
        home_img_tag = home_div_tag.find_element_by_tag_name("img")

        # imgタグ内のsrc属性の値(画像リンク)を抽出
        src = home_img_tag.get_attribute("src")

        # 取得した画像リンクをリストに追加
        img_link_list.append(src)

    print(f"{len(img_link_list)} 件の画像リンク取得成功")

    # 画像リンクリストを返却
    return img_link_list


# 引数の画像リンクリストの画像をドライブにダウンロード
def download_image(img_link_list: list, target_user_name: str):
    # 実行時の現在時間を「yyyyMMdd」で取得
    now_date = datetime.datetime.now()
    now_date_formatted = now_date.strftime("%Y%m%d_%H%M%S")

    # 保存先フォルダパス
    folder_path = "./output/homeImg/" + target_user_name + "_" + now_date_formatted + "/"

    '''フォルダ作成'''
    try:
        # 画像の取得元のユーザIDをフォルダ名として作成
        os.makedirs(folder_path)
    except:
        print(f"\n{folder_path} フォルダは既に存在するため作成されませんでした")

    '''画像ダウンロード'''
    # 連番
    i = 0

    # 画像リンクリストの数だけ繰り返し
    for img_link in img_link_list:
        '''画像を1件ずつダウンロード(ファイル名は連番)'''
        # 連番をインクリメント
        i = i + 1

        # 画像データ変数宣言
        img_data = None

        # urllibで画像URLからバイナリ読み込み
        with urllib.request.urlopen(img_link) as rf:
            img_data = rf.read()

        # 画像データをpng形式で書き出し
        with open(folder_path + str(i) + ".png", mode="wb") as wf:
            wf.write(img_data)
    print(f"{folder_path} に {i} 件保存しました")


# 実行時呼び出し
if __name__ == "__main__":
    main()
