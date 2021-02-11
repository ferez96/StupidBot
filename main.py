# Service Start Point
from clients.discord_client import client

if __name__ == "__main__":

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('>cf-rating'):
            a = message.content.split(" ")
            if len(a) != 2:
                return
            handle = a[1]
            from services.codeforces.rating import get_user_rating
            resp = f"Current rating of {handle} is: {get_user_rating(handle)}"
            await message.channel.send(resp)


    client.run('NzYxOTI4NzIzODIxNDk0MzAy.X3hvaw.8I2iTscW838is4CosBGmhU_dpcE')
