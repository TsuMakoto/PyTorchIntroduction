import torchvision
from torchvision import transforms


class BaseTransform:
    def __init__(self, resize, mean, std):
        self.resize = resize
        self.mean = mean
        self.std = std

    def __call__(self, img):
        return self._transforms()(img)

    def _transforms(self):
        if hasattr(self, 'transforms'):
            return self.transforms

        return transforms.Compose([
            transforms.Resize(self.resize),
            transforms.CenterCrop(self.resize),
            transforms.ToTensor(),
            transforms.Normalize(self.mean, self.std)
        ])
