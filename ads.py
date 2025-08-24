from vk_api import *
from vk_api.utils import get_random_id
authorize = vk_api.VkApi(token = "deb669035093ff633fee8e9271a4aba21bef38143bec8135b903e2c6a0d2f0c67a75aed3981d360fe2a89")
def write_message(id, message):
    authorize.method('messages.send', {'user_id': id, 'message': message, 'random_id': get_random_id()})

write_message(463379321,"Test")