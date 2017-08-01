import os
import sys
import numpy
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import torch.nn.functional as F

import matplotlib.pyplot as plt
from learning_args import parse_args
from data.synthetic.box_data import BoxData
from data.synthetic.mnist_data import MnistData
from data.synthetic.box2_data import Box2Data
from data.synthetic.mnist2_data import Mnist2Data
from data.real.robot64_data import Robot64Data
from data.real.mpii64_data import Mpii64Data
from data.real.mpii64_sample import Mpii64Sample
from data.real.nyuv2_data import Nyuv2Data
from base_model import BaseNet, BaseGtNet
from visualize.base_visualizer import BaseVisualizer
import logging
logging.basicConfig(format='[%(levelname)s %(asctime)s %(filename)s:%(lineno)s] %(message)s',
                            level=logging.INFO)


class BaseDemo(object):
    def __init__(self, args):
        self.learning_rate = args.learning_rate
        self.train_epoch = args.train_epoch
        self.test_epoch = args.test_epoch
        self.test_interval = args.test_interval
        self.save_dir = args.save_dir
        self.display = args.display
        self.display_all = args.display_all
        self.best_improve_percent = -1e10
        self.batch_size = args.batch_size
        self.im_size = args.image_size
        self.im_channel = args.image_channel
        self.num_frame = args.num_frame
        self.m_range = args.motion_range
        if args.data == 'box':
            self.data = BoxData(args)
        elif args.data == 'mnist':
            self.data = MnistData(args)
        elif args.data == 'box2':
            self.data = Box2Data(args)
        elif args.data == 'mnist2':
            self.data = Mnist2Data(args)
        elif args.data == 'robot64':
            self.data = Robot64Data(args)
        elif args.data == 'mpii64':
            self.data = Mpii64Data(args)
        elif args.data == 'mpii64_sample':
            self.data = Mpii64Sample(args)
        elif args.data == 'nyuv2':
            self.data = Nyuv2Data(args)
        else:
            logging.error('%s data not supported' % args.data)
        self.visualizer = BaseVisualizer(args, self.data.reverse_m_dict)

    def compare(self):

        width, height = self.visualizer.get_img_size(4, 3)
        img = numpy.ones((height, width, 3))

        base1_loss, base2_loss, interp_loss, extrap_loss= [], [], [], []
        for epoch in range(self.test_epoch):
            if self.data.name in ['box', 'mnist']:
                im, motion, _, _ = self.data.get_next_batch(self.data.test_images)
            elif self.data.name in ['box2', 'mnist2']:
                im, motion, _ = self.data.get_next_batch(self.data.test_images)
            elif self.data.name in ['robot64', 'mpii64', 'nyuv2', 'mpii64_sample']:
                im, motion = self.data.get_next_batch(self.data.test_meta), None
            elif self.data.name in ['mpii64_sample']:
                im, motion = self.data.get_next_batch(self.data.test_meta), None
                im = im[:, -self.num_frame:, :, :, :]
            else:
                logging.error('%s data not supported' % self.data.name)
                sys.exit()
            im = Variable(torch.from_numpy(im).float())
            if torch.cuda.is_available():
                im = im.cuda()
            im1 = im[:, 0, :, :, :]
            im2 = im[:, 1, :, :, :]
            im3 = im[:, 2, :, :, :]

            im = im1[0].cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(1, 1)
            img[y1:y2, x1:x2, :] = im

            im = im2[0].cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(1, 2)
            img[y1:y2, x1:x2, :] = im

            im = im3[0].cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(1, 3)
            img[y1:y2, x1:x2, :] = im

            im_diff = torch.abs(im1[0] - im2[0]).cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(2, 1)
            img[y1:y2, x1:x2, :] = im_diff

            im_diff = torch.abs(im2[0] - im3[0]).cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(2, 2)
            img[y1:y2, x1:x2, :] = im_diff

            base1_loss.append(torch.abs(im1 - im2).sum().data[0])
            im_base = (im1 + im3) / 2
            interp_loss.append(torch.abs(im_base - im2).sum().data[0])

            im = im_base[0].cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(3, 1)
            img[y1:y2, x1:x2, :] = im

            im_diff = torch.abs(im_base[0] - im2[0]).cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(3, 2)
            img[y1:y2, x1:x2, :] = im_diff

            base2_loss.append(torch.abs(im2 - im3).sum().data[0])
            im_base = 2 * im2 - im1
            im_base[im_base < 0] = 0
            im_base[im_base > 1] = 1
            extrap_loss.append(torch.abs(im_base - im3).sum().data[0])

            im = im_base[0].cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(4, 1)
            img[y1:y2, x1:x2, :] = im

            im_diff = torch.abs(im_base[0] - im3[0]).cpu().data.numpy().transpose(1, 2, 0)
            x1, y1, x2, y2 = self.visualizer.get_img_coordinate(4, 2)
            img[y1:y2, x1:x2, :] = im_diff

            plt.figure(1)
            plt.imshow(img)
            plt.axis('off')
            plt.show()

        base1_loss = numpy.mean(numpy.asarray(base1_loss))
        interp_loss = numpy.mean(numpy.asarray(interp_loss))
        base2_loss = numpy.mean(numpy.asarray(base2_loss))
        extrap_loss = numpy.mean(numpy.asarray(extrap_loss))
        print base1_loss, interp_loss
        print base2_loss, extrap_loss



def main():
    args = parse_args()
    logging.info(args)
    demo = BaseDemo(args)
    demo.compare()

if __name__ == '__main__':
    main()

