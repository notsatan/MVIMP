import os
import sys

LOC = os.getcwd()
ANIMEGAN_PREFIX = os.path.join(LOC, 'AnimeGAN')
DAIN_PREFIX = os.path.join(LOC, 'DAIN')


def anime_preparation():
    os.chdir(ANIMEGAN_PREFIX)
    pretrain_model_url = "https://github.com/TachibanaYoshino/AnimeGAN/releases/download/Haoyao-style_V1.0/Haoyao-style.zip"
    pretrain_model_file = "./checkpoint/Haoyao-style.zip"
    pretrain_model_dir = "./checkpoint/AnimeGAN_Hayao_lsgan_300_300_1_3_10"
    vgg_url = "https://github.com/TachibanaYoshino/AnimeGAN/releases/download/vgg16%2F19.npy/vgg19.npy"
    vgg_dir = "./vgg19_weight"
    vgg_file = os.path.join(vgg_dir, 'vgg19.npy')

    os.system(f'rm -rf {pretrain_model_dir}')
    os.system(f'rm -rf {vgg_dir}')

    os.makedirs(f'{pretrain_model_dir}')
    os.makedirs(f'{vgg_dir}')

    os.system(f'wget -N {pretrain_model_url} -O {pretrain_model_file}')
    os.system(f'unzip {pretrain_model_file} -d {pretrain_model_dir}')
    os.system(f'wget {vgg_url} -O {vgg_file}')

    os.system(f'rm {pretrain_model_file}')


def dain_preparation():
    os.chdir(DAIN_PREFIX)


def main(argv):
    if argv[1] == '01':
        pass


if __name__ == '__main__':
    main(sys.argv)