import numpy as np

from ..repositories.ilsvrc_info_repository import IlsvrcInfoRepository


class IlsvrcPredictor:
    def __init__(self, repository=IlsvrcInfoRepository()):
        self.repository = repository()

    def predict_max(self, out):
        self.out = out
        """
            確率最大のILSVRCのラベル名を取得する。
            Parameters
            ---
            out: touch.Size([1, 1000])
                Netから出力。

            Returns
            ---
            predicted_label_name: str
                最も予測確率が高いラベルの名前
            """
        maxid = np.argmax(self._out_of_detach().numpy())
        ilsvrc_info = self.repository.find(maxid)
        return ilsvrc_info.label_name

    def _out_of_detach(self):
        if hasattr(self, 'out_of_detach'):
            return self.out_of_detach

        return self.out.detach()
