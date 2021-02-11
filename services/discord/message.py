from clients import discord_client


def send_message(channel, msg):
    discord_client.send_message_to_channel(channel, msg)
