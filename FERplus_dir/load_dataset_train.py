import os, sys, shutil
import random as rd
from os import listdir
from PIL import Image
import numpy as np
import random
import torch
import torch.nn.functional as F
import torch.utils.data as data
import pdb
from torch.autograd import Variable
from torch.nn.modules.loss import _WeightedLoss

def load_imgs(img_dir, image_list_file, label_file):
    imgs_first = list()
    imgs_second = list()
    imgs_third = list()
    imgs_forth = list()
    imgs_fifth = list()
    imgs_sixth = list()
    #imgs_seventh = list()
    #imgs_eigth = list()
    max_label = 0
    with open(image_list_file, 'r') as imf:
        with open(label_file, 'r') as laf:
            
            
            for line in imf:
                
                space_index = line.find(' ')
                
                video_name = line[0:space_index]  # name of video
                img_count = line[space_index+1:]  # number of frames in video
                
                video_path = os.path.join(img_dir, video_name)# video_path is the path of each video
                ###  for sampling triple imgs in the single video_path  ####

                if not os.path.exists(video_path):
                    continue
                
                img_lists = listdir(video_path)
                # pdb.set_trace()
                record = laf.readline().strip().split()
                img_lists.sort()  #  sort files by ascending
                img_path_first =    video_path+'/'+img_lists[0]
                img_path_second = video_path + '/'+img_lists[1]
                img_path_third = video_path + '/'+img_lists[2]
                img_path_forth = video_path + '/'+img_lists[3]
                img_path_fifth = video_path + '/' + img_lists[4]
                img_path_sixth = video_path + '/' + img_lists[5]
                #img_path_seventh = video_path + '/' + img_lists[6]
                #img_path_eigth = video_path + '/' + img_lists[7]
                #pdb.set_trace()
                label = int(record[0])            
                imgs_first.append((img_path_first,label))
                imgs_second.append((img_path_second,label))
                imgs_third.append((img_path_third,label))
                imgs_forth.append((img_path_forth,label))
                imgs_fifth.append((img_path_fifth,label))
                imgs_sixth.append((img_path_sixth,label))
                #imgs_seventh.append((img_path_seventh,label))
                #imgs_eigth.append((img_path_eigth,label))

                ###  return multi paths in a single video  #####

           
                #print 'record[0],record[1],record[2]',record[0],record[1],record[2]
                
    return imgs_first,imgs_second,imgs_third, imgs_forth, imgs_fifth, imgs_sixth

class MsCelebDataset(data.Dataset):
    def __init__(self, img_dir, image_list_file, label_file, transform=None):
        self.imgs_first, self.imgs_second, self.imgs_third, self.imgs_forth, self.imgs_fifth, self.imgs_sixth = load_imgs(img_dir, image_list_file, label_file)
        self.transform = transform

    def __getitem__(self, index):
        path_firt, target_first = self.imgs_first[index]
        img_first = Image.open(path_firt).convert("RGB")
        if self.transform is not None:
            img_first = self.transform(img_first)
        
        path_second, target_second = self.imgs_second[index]
        img_second = Image.open(path_second).convert("RGB")
        if self.transform is not None:
            img_second = self.transform(img_second)

        path_third, target_third = self.imgs_third[index]
        img_third = Image.open(path_third).convert("RGB")
        if self.transform is not None:
            img_third = self.transform(img_third)

        path_forth, target_forth = self.imgs_forth[index]
        img_forth = Image.open(path_forth).convert("RGB")
        if self.transform is not None:
            img_forth = self.transform(img_forth)

        path_fifth, target_fifth = self.imgs_fifth[index]
        img_fifth = Image.open(path_fifth).convert("RGB")
        if self.transform is not None:
            img_fifth = self.transform(img_fifth)

        path_sixth, target_sixth = self.imgs_sixth[index]
        img_sixth = Image.open(path_sixth).convert("RGB")
        if self.transform is not None:
            img_sixth = self.transform(img_sixth)

        # path_seventh, target_seventh = self.imgs_seventh[index]
        # img_seventh = Image.open(path_seventh).convert("RGB")
        # if self.transform is not None:
        #     img_seventh = self.transform(img_seventh)

        # path_eigth, target_eigth = self.imgs_eigth[index]
        # img_eigth = Image.open(path_eigth).convert("RGB")
        # if self.transform is not None:
        #     img_eigth = self.transform(img_eigth)

        return img_first, target_first ,img_second,target_second,img_third,target_third,img_forth,target_forth, img_fifth, target_fifth, img_sixth, target_sixth
    def __len__(self):
        return len(self.imgs_first)




class CaffeCrop(object):
    """
    This class take the same behavior as sensenet
    """
    def __init__(self, phase):
        assert(phase=='train' or phase=='test')
        self.phase = phase

    def __call__(self, img):
        # pre determined parameters
        final_size = 224
        final_width = final_height = final_size
        res_img = img.resize( (final_width, final_height) )
        return res_img
