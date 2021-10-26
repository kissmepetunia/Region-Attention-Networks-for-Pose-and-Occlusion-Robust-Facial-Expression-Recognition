# RAN

This is an reimplement of the work [Region Attention Networks for Pose and Occlusion Robust Facial Expression Recognition](https://arxiv.org/pdf/1905.04075.pdf).
This code is based on [the original author's code](https://github.com/kaiwang960112/Challenge-condition-FER-dataset/) with the following changes. Thanks, Kai Wang.


## Changes

- Pytorch code

Since part of the original pytorch code does not work in the new version of pytorch code, I made some minor changes to accommodate the versioning issue.

- Code to generate intermediate files

Some of the files in the original repository did not have uniform code to generate intermediate files (e.g. cropping, txt of the corresponding folder corresponding to each image)

- The path tree is rather confusing

The original files and script paths were rather messy, so I made some changes here to better organize these scripts.

## Results

```
accuracy 0.8701964133219471
correct 1019
video_num 1171

```

## Usage
After all the pre-generated files is done.

```
python train_attention_rank_loss.py

python test_rank_loss_attention.py
```
## To Do

- [ ]  Change variable names that are inconsistent and obscure

- [x]  Removal of unnecessary intermediate files
 
- [x]  Removal of unnecessary script files and functions

- [ ]  Implemetation on Affectnet and RAF-DB

- [ ]  Swich the Backbone. [VGG16 is the caffe model from vggface officially published by vgg to pytorch (with soft label)]
