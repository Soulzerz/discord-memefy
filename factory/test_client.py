import discord
import unittest
from .factory import Discord 

class ClientTestCase(unittest.TestCase):
    def setUp(self):
       self.discord_client = discord.Client()

    def test_can_create_client(self):
        client = Discord(client=self.discord_client)
        self.assertIsInstance(client, Discord)
        self.assertIsInstance(client.client, discord.Client)