import torchvision
from torchvision import models


class Vgg16ImageRepo:
    def __init__(self, use_pretrained=True):
        self.use_pretrained = use_pretrained

    def call(self):
        return self._net().eval()

    def _models(self):
        if hasattr(self, 'models'):
            return self.models
        else:
            return models

    def _net(self):
        if hasattr(self, 'net'):
            return self.net
        else:
            return self._models().vgg16(pretrained=self.use_pretrained)
