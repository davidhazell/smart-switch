import logging
import requests
import json
import queue
import threading


class Light:

    def __init__(self, id_, connection):
        # Setup Logger
        self.__logger     = logging.getLogger(__name__)
        self.__logger.info('LIGHT')
        # Create variables
        self.__connection = connection
        self.__id         = None
        self.__check_id(id_)
        # Setup Queue
        self.__queue      = queue.Queue()
        self.__logger.debug(self.__queue.qsize())
        # Setup Thread
        self.__thread     = threading.Thread(target=self.__watch_queue)
        self.__thread.setDaemon(True)
        self.__thread.start()
        self.transitiontime(0)

        self.__logger.debug(self.__state())

    @property
    def state(self):
        return self.__state()

    @property
    def name(self):
        return self.__state()['name']

    def on(self):
        self.__queue.put_nowait({'on': True})

    def bri(self, value=254):
        if value not in range(0, 254):
            self.__logger.error('Incorrect brightness value (%s).  Must be between 0 and 254.' % str(value))
        self.__queue.put_nowait({'bri': value})

    def hue(self, value):
        if value not in range(0, 65535):
            self.__logger.error('Incorrect value (%s).  Must be between 0 and 65535.' % str(value))
        self.__queue.put_nowait({'hue': value})

    def sat(self, value=254):
        if value not in range(0, 254):
            self.__logger.error('Incorrect sat value (%s). Must be between 0 and 254.' % str(value))
        self.__queue.put_nowait({'sat': value})

    def xy(self, value_x, value_y):
        if value_x not in [0, 1] or value_y not in [0, 1]:
            self.__logger.error('Incorrect xy values (%s, %s)' % (str(value_x), str(value_y)))
        self.__queue.put_nowait({'xy': [value_x, value_y]})

    def ct(self, value):
        if value not in range(153, 500):
            self.__logger.error('Incorrect ct value (%s). Must be between 153 and 500.' % str(value))
        self.__queue.put_nowait({'xy': value})

    def alert(self, value='none'):
        if value not in ['none', 'select', 'lselect']:
            self.__logger.error('Incorrect alert value (%s)' % str(value))
        self.__queue.put_nowait({'xy': value})

    def effect(self, value='none'):
        if value not in ['none', 'colorloop']:
            self.__logger.error('Incorrect effect value (%s)' % str(value))
        self.__queue.put_nowait({'xy': value})

    def transitiontime(self, value=1000):
        if value not in range(0, 100000):
            self.__logger.error('Incorrect effect value (%s)' % str(value))
        self.__queue.put_nowait({'transitiontime': value})

    def bri_inc(self, value=26):
        if value not in range(-254, 254):
            self.__logger.error('Incorrect bri_inc value (%s). Must be between -254 and 254.' % str(value))
        self.__logger.debug('Placing item on queue: {\'bri_inc\': %s}' % str(value))
        self.__queue.put_nowait({'bri_inc': value})

    def sat_inc(self, value=26):
        if value not in range(-254, 254):
            self.__logger.error('Incorrect sat_inc value (%s). Must be between -254 and 254.' % str(value))
        self.__queue.put_nowait({'sat_inc': value})

    def hue_inc(self, value=656):
        if value not in range(-65534, 65534):
            self.__logger.error('Incorrect hue_inc value (%s). Must be between -254 and 254.' % str(value))
        self.__queue.put_nowait({'hue_inc': value})

    def ct_inc(self, value=656):
        if value not in range(-65534, 65534):
            self.__logger.error('Incorrect hue_inc value (%s). Must be between -254 and 254.' % str(value))
        self.__queue.put_nowait({'ct_inc': value})

    def xy_inc(self, value=656):
        if value < -0.5 or value > 0.5:
            self.__logger.error('Incorrect hue_inc value (%s). Must be between -0.5 and 0.5.' % str(value))
        self.__queue.put_nowait({'bri_inc': value})

    def scene(self, value):
        self.__queue.put_nowait({'scene': value})

    def __watch_queue(self):
        self.__logger.info('Starting HueRoom queue thread...')
        while True:
            if not self.__queue.empty():
                action = self.__queue.get()
                self.__logger.debug('Removing item from queue: %s' % str(action))
                # self.__action(action)

    def __check_id(self, id_):
        self.__logger.debug('Checking Room name...')
        try:
            request = requests.get(self.__connection.api + '/lights')
            lights  = json.loads(request.text)
            found = False
            for key, value in lights.items():
                self.__logger.debug(str(type(key)) + ': ' + str(key))
                self.__logger.debug(str(type(value)) + ': ' + str(value))
                if key == str(id_):
                    self.__logger.debug('Found light with id \'%s\' and name \'%s\'.' % (id_, value['name']))
                    self.__id   = key
                    found = True
                    break
            if not found:
                self.__logger.error('Not found')
        except requests.exceptions.RequestException as e:
            self.__logger.error(e)
            # Stop thread

    def __action(self, data):
        try:
            self.__logger.debug('request start')
            request = requests.put(self.__connection.api+'/lights/'+self.__id+'/state', data=json.dumps(data))
            self.__logger.debug('request end')
            if not request.ok:
                self.__logger.error(request.text)
        except requests.exceptions.RequestException as e:
            self.__logger.error(e)

    def __state(self):
        try:
            request = self.__connection.session.get(self.__connection.api + '/lights/' + self.__id + '/state')
            self.__logger.debug(request.text)
            return json.loads(request.text)
        except requests.exceptions.RequestException as e:
            self.__logger.error(e)
            return None
