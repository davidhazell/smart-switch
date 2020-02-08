import logging
import requests
from hue.room import Room
from hue.light import Light


class HueConnection:

    __API_TOKEN__ = 'lOtvw05Dxu175NZg0GrLlXaySxHcD577mbTOjhT7'

    def __init__(self, host, room='Office'):

        self.__logger = logging.getLogger(__name__)
        self.__logger.info("HUE CONNECTION")

        self.__host     = host
        self.__session  = requests.Session()
        self.__base_url = 'http://' + self.__host + '/api/' + self.__API_TOKEN__

        self.__room = Room(room, connection=self)
        self.__light = Light(32, connection=self)  # 41, 32, 25

    @property
    def room(self):
        return self.__room

    @property
    def light(self):
        return self.__light

    @property
    def api(self):
        return self.__base_url

    @property
    def session(self):
        return self.__session
