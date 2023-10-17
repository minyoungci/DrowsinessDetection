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
