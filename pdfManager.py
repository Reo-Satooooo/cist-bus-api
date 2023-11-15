import requests
import os
import shutil
from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup

class PdfManager:
  
  def __init__(self):
    self.load_url = "http://www.chitose.ac.jp/info/access"
    self.html = requests.get(self.load_url, verify=False)
    self.soup = BeautifulSoup(self.html.content, "html.parser")
    self.tag_list = self.soup.select('a[href*="/uploads/files/"]')
    self.file_name = self.tag_list[0].get('href')
    self.file_dir = "download"    
    self.file_path = os.path.join(self.file_dir, self.get_file_name())
                                  
  def get_file_name(self):
    JST = timezone(timedelta(hours=+9), 'JST')
    now = datetime.now(JST).strftime("%Y_%m_%d")
    return now + ".pdf"
  
  def file_exists(self):
    print("ファイルの存在確認")
    return os.path.isfile(self.file_path)

  def download_file(self):
    file_url = "https://www.chitose.ac.jp" + self.file_name
    response = requests.get(file_url, verify=False)
    with open(self.file_path, "wb") as file:
        for chunk in response.iter_content(100000):
            file.write(chunk)
    print("ダウンロード・ファイル保存完了")
    
  def get_pdf_from_web(self):  
    if not os.path.exists(self.file_dir):
        os.makedirs(self.file_dir)
    
    if self.file_exists():
        print("ファイルが既に存在します")
        current_file_name = os.listdir(self.file_dir)[0]
        expected_file_name = self.get_file_name()
        if current_file_name != expected_file_name:
            print("ファイル名が異なるため、ファイルを更新します")
            shutil.rmtree(self.file_dir)
            os.makedirs(self.file_dir)
            self.download_file()    
    else:
        print("ファイルが一つも存在しません")
        self.download_file()
    # if  self.file_exists():
    #     print("ファイルが既に存在します")
    #     # file_dir直下にあるファイル名を取得
    #     current_file_name = os.listdir(self.file_dir)[0]
    #     expected_file_name = self.get_file_name()
    #     if current_file_name != expected_file_name:
    #         print("ファイル名が異なるため、ファイルを更新します")
    #         shutil.rmtree(self.file_dir)
    #         os.makedirs(self.file_dir)
    #         self.file_path = os.path.join(self.file_dir, expected_file_name)
    #         self.download_file()    
    # else:
    #     print("ファイルが一つも存在しません")
    #     shutil.rmtree(self.file_dir)
    #     os.makedirs(self.file_dir)
    #     self.download_file()
        
    