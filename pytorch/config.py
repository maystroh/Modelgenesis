import os
import shutil

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG)

log = logging.getLogger()

class models_genesis_config:
    model = "Unet3D"
    suffix = "genesis_oct"
    exp_name = model + "-" + suffix

    # data
    data = "/home/harddrive/Projects/GAMMA_data/model_genesis_data/generated/"
    # train_fold = [0, 1, 2, 3, 4]
    train_fold = [0]
    # valid_fold = [5, 6]
    valid_fold = [1]
    test_fold = [1]
    hu_min = -1000.0
    hu_max = 1000.0
    scale = 32
    input_rows = 96
    input_cols = 96
    input_deps = 96
    nb_class = 1

    # model pre-training
    verbose = 1
    weights = None
    batch_size = 1
    optimizer = "sgd"
    workers = 10
    max_queue_size = workers * 4
    save_samples = "png"
    nb_epoch = 10000
    patience = 50
    lr = 1

    # image deformation
    nonlinear_rate = 0.9
    paint_rate = 0.9
    outpaint_rate = 0.8
    inpaint_rate = 1.0 - outpaint_rate
    local_rate = 0.5
    flip_rate = 0.4

    # logs
    model_path = "../pretrained_weights"
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    logs_path = os.path.join(model_path, "Logs")
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)

    def display(self):
        """Display Configuration values."""
        print("\nConfigurations:")
        for a in dir(self):
            if not a.startswith("__") and not callable(getattr(self, a)):
                log.info("{:30} {}".format(a, getattr(self, a)))
        log.info("\n")
