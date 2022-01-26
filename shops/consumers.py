from channels.generic.websocket import  import AsyncWebsocketConsumer

class ClientsCounterConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.product_ = self.scope['url_route']['kwargs']['product_id']
        self.product_group_name = f'product_{self.product_}'

        # connect to channel layer
        await self.channel_layer.group_add(
            self.product_group_name,
            self.channel_name
        )
        print('connected')
        # work with connection
        await self.accept()

    # if disconnect: расформ group
    async def disconnect(self,code):
        await self.channel_layer.group_discard(
            self.product_group_name,
            self.channel_name

        )

