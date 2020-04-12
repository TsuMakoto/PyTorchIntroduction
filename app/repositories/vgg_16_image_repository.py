from ..entities.vgg_16_image import Vgg16Image
from ..models.vgg_16_image_model import Vgg16ImageModel


class Vgg16ImageRepository:
    def __init__(self,
                 model=Vgg16ImageModel.dataset(),
                 entity=Vgg16Image):
        self.model = model
        self.entity = entity
