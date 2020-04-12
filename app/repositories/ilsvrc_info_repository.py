from ..entities.ilsvrc_info import IlsvrcInfo
from ..models.ilsvrc_label_info_model import IlsvrcInfoModel


class IlsvrcInfoRepository:
    def __init__(self,
                 dataset=IlsvrcInfoModel.dataset(),
                 entity=IlsvrcInfo):
        self.dataset = dataset
        self.entity = entity

    def find(self, id=0):
        data = self.dataset[str(id)]
        return self.entity(id=id, label_name=data[0], name=data[1])
