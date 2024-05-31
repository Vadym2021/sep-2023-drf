from apps.cars.models import CarModel
from apps.cars.serizlizers import CarSerializer
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer


class CarConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.room_name = 'cars'
        super().__init__(*args, **kwargs)

    async def connect(self):
        if not self.scope['user']:
            await self.close()
            return
        await self.accept()
        await self.channel_layer.group_add(
            self.room_name,
            self.room_name
        )

    @model_observer(CarModel, serializer_class=CarSerializer)
    async def cars_activity(self, message, action, subscribing_request_ids, **kwargs):
        for request_id in subscribing_request_ids:
            await self.reply(data=message, action=action, request_id=request_id)

    @action()
    async def subscribe_to_car_activity(self, request_id, **kwargs):
        await self.cars_activity.subscribe(request_id=request_id)
