# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""SSD300 for object detection on MSCOCO."""

from composer.models.ssd.ssd import SSD as SSD

_task = 'Object Detection'
_dataset = 'COCO'
_name = 'SSD'
_hparams = 'ssd.yaml'
