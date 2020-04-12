import json


class IlsvrcInfoModel:
    FILEPATH = '../data/imagenet_class_index.json'

    def dataset(self):
        if not hasattr(IlsvrcInfoModel, 'data'):
            self.dataset = json.load(IlsvrcInfoModel.FILEPATH, 'r')

        return self.dataset
