from ..repositories.vgg_16_image_repo import Vgg16ImageRepo


class Vgg16Image:
    def __init__(self, repository=Vgg16ImageRepo()):
        self.repository = repository
