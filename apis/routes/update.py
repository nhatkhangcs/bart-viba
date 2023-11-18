from GraphTranslation.apis.routes.base_route import BaseRoute
from objects.data import ModifyData
import yaml
# import Adder
from pipeline.updateword import Update
from apis.routes.translation import TranslateRoute

class updateWord(BaseRoute):
    def __init__(self, area):
        super(updateWord, self).__init__(prefix="/updateword")
        self.area = area
        self.pipeline = Update(self.area)

    def update_word(self, data: ModifyData):
        with open('data/cache/info.yaml', 'r+') as f:
            # if the "area" field is not KonTum then delete
            data = yaml.safe_load(f)
            area = data.get('area', None)
            self.area = area
        success = self.pipeline(data.word, data.translation)
        if success:
            TranslateRoute.changePipelineRemoveGraph(area=self.area)
            return "Word updated successfully"
        else:
            return "Could not find word or new meaning is unchanged"
    
    def create_routes(self):
        router = self.router

        @router.post("/vi_ba")
        async def add_word(data: ModifyData):
            return await self.wait(self.update_word, data)