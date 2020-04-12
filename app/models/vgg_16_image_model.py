import torchvision
from torchvision import models


# VGG-16モデル
# 全て38層で構成されている内、主要な16層の構成
# 3x3サイズの畳み込みフィルダの64チャネル
class Vgg16ImageModel:
    USE_PRETRAINED = True

    def dataset(self):
        return self._net().eval()

# private
    def _net(self):
        if hasattr(self, 'net'):
            return self.net

        return self.models.vgg16(pretrained=Vgg16ImageModel.USE_PRETRAINED)
