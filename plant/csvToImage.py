from fastai.vision import *

# 현재 참조하는 디렉토리의 리스트 불러오기
import os

csv_path = input("Input your csv file path : ")
unit = input("Input your split unit : ")

path = csv_path # csv 파일이 들어있는 경로 설정
file_list = os.listdir(path)

print ("file_list: {}".format(file_list))

# 파일 이름 추출 확인을 위한 함수
def file_name_verify(name, file_name):
  print('식물 이름: '+ name)
  print('파일명: ' + file_name)


def download_files(name, file_name):
  # 폴더 만들기
  dest = path/folder
  dest.mkdir(parents=True, exist_ok=True)
  #이미지 다운로드
  download_images(path/file, dest, max_pics=1000)

# 파일 이름 추출하기
for i in file_list:
  fl_ = i.split(unit)
  del(fl_[1:])
  print(fl_)
  fl_name = ''.join(fl_)
  print(fl_name)
  # 파일 이름 추출 확인을 위한 함수
  fd(fl_name, i)
  # 파일 및 폴더 설정
  folder = fl_name
  file = i
  
  download_files(fl_name, i)
  # 정상적인 파일인지 확인
  for c in range(1000):
    print(c)
    verify_images(path/c, delete=True, max_size=1000)