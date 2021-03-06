import random

from ...common import *
from ... import module as mod


responses = [
    '''5/7 not bad, but my dog could do better.''',
    '''I didn't know toddlers could spell.''',
    '''Did **you** draw that or did a chimpanzee kick over an inkpot?''',
    '''There are rhynos out there that have more talent.''',
    '''Pro tip: next time don't turn the keyboard upside down.''',
    '''Quick! someone call an ambulance! This person is having a stroke!''',
    '''They say everyone is entitled to their own opinion. But **that** is just objectively wrong.''',
    '''Even a Tippex brush has not seen that many mistakes in its life.''',
]


class StuxxModule(mod.Module):
    async def on_load(self):
        self.last_response = None

    @mod.Module.listener()
    async def on_message(self, msg):
        if msg.content.startswith('stuxx rate my'):
            response = random.choice(responses)

            while response == self.last_response: 
                response = random.choice(responses)
            
            self.last_response = response
            await msg.channel.send(response)
