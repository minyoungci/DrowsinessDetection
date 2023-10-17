### 데이터셋 

`100k / train`의 경로에 몇 이미지들은 testA, testB, trainA, trainB로 나눠져있음. 

``` bash
$ mv bdd100k/bdd100k/image bdd100k/
$ mv bdd100k/images/100k/train/testA/* bdd100k/images/100k/train/
$ mv bdd100k/images/100k/train/testB/* bdd100k/images/100k/train/
$ mv bdd100k/images/100k/train/trainA/* bdd100k/images/100k/train/
$ mv bdd100k/images/100k/train/trainB/* bdd100k/images/100k/train/

$ cp -r bdd100k_labels_release/bdd100k/labels/ ./bdd100k/
```

### bdd2voc.py - 이 코드는 주어진 BDD100K 데이터셋을 처리하여 PASCAL VOC 형식으로 변환하며, 이를 통해 객체 탐지 모델을 훈련시키기 위한 준비 작업을 수행할 수 있습니다.

전역 변수 설정:
DEBUG, BDD_FOLDER, XML_PATH와 같은 전역 변수를 설정하여 파일 경로와 디버깅 옵션을 정의합니다.

bdd_to_voc 함수:
bdd_to_voc 함수는 BDD100K 데이터셋의 JSON 파일을 PASCAL VOC 스타일의 XML 파일로 변환합니다.
이 함수는 두 개의 인자를 받습니다: bdd_folder (BDD100K 데이터셋의 경로)와 xml_folder (XML 파일을 저장할 경로).
이 함수 내에서, 코드는 train 및 val 데이터셋에 대해 반복하며, 각 이미지에 대한 XML 파일을 생성합니다.

XML 파일 생성:
각 이미지에 대해, 코드는 XML 요소와 속성을 생성하며, 해당 이미지의 바운딩 박스와 클래스 레이블을 포함합니다.
get_size, get_bbox, prettify 함수는 XML 파일 생성을 돕습니다. get_size는 이미지의 크기를 반환하며, get_bbox는 바운딩 박스의 좌표를 반환하고, prettify는 XML 문자열을 예쁘게 포맷팅합니다.

XML 파일 저장:
각 이미지에 대한 XML 파일은 지정된 xml_folder 디렉토리에 저장됩니다.

메인 실행 블록:
코드가 메인으로 실행되면 bdd_to_voc 함수가 호출되어 지정된 BDD100K 폴더에서 XML 파일을 생성하고 저장합니다.
