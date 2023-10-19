import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
grand_dir = os.path.abspath(os.path.join(parent_dir, '..'))
# Add the directories to sys.path
sys.path.extend([script_dir, parent_dir, grand_dir])

from pipeline.translation import Translator
import os
from objects.singleton import Singleton

class ChangeCorpus:
    def __init__(self, area):
        super(ChangeCorpus, self).__init__()
        self.area = area

    def changeCorpus(self, changeTo):
        #translator = Translator(area=changeTo)
        #print(dict(Singleton._instances))
        #if (changeTo != self.area):
        if os.path.exists("data/cache/graph.json"):
            os.remove("data/cache/graph.json")
            
        for cls in dict(Singleton._instances).keys():
            #print(type(cls))
            #if cls != apis.routes.changeCorpus.changeCorpus:
                #print("ChangeCorpus found\n")
                del Singleton._instances[cls]
                cls = None
            
            #print(dict(Singleton._instances))
        newTrans = Translator(area=changeTo)
        print(newTrans)
        
        #print(dict(Singleton._instances))
        print(f"Changed to {changeTo}")
        self.area = changeTo
        
        return newTrans

    def __call__(self, changeTo):
        res = self.changeCorpus(changeTo=changeTo)
        return res

if __name__ == "__main__":
    translator = Translator(area="BinhDinh")
    print(translator("Đồng tiền là vô giá"))
    changeDictCorpus = ChangeCorpus("Gia Lai")
    newTranslator = changeDictCorpus.changeCorpus("GiaLai")
    print(newTranslator("Đồng tiền là vô giá"))

