#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.67
        self.width = 0.75
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        self.input_size = (1536, 1024)
        self.test_size = (1536, 1024)
        self.data_dir = "/workspaces/kuzusiji1/kobunsho_coco/"
        self.train_ann = "train_annotations.json"
        self.val_ann = "val_annotations.json"

        self.num_classes = 1

        self.eval_interval = 1
