import time


class TrafficLight:
    _color: str = 'Red'

    def running(self):
        '''
        Метод переключает свет светофора по истечению заданного промежутка времени
        '''
        operation_mode = {
            self._color: 4,
            'Yellow': 2,
            'Green': 3
        }
        for key, value in operation_mode.items():
            print(f'{key} light is running {value} seconds')
            time.sleep(int(value))


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
