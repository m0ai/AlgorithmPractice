#!/usr/bin/python3
'''
 제가 알고 있는 일반적인 엘레베이터는 엘레베이터 내부에서 가려고하는 n층의 버튼을 눌러 이동하는 엘레베이터 입니다.
하지만.. 최근에 큰 빌딩(건물)을 놀러갈일이 생겨 높은 빌딩을 갈일이 생겼습니다.
그 건물 엘레베이터는 각 층마다 타기전에 터치패널을 통해 미리 가야하는 층을 눌러놓고
엘레베이터를 기달린 후 열기/닫기 버튼만 있는 엘레베이터를 타는 구조였습니다.

그것을 보고 컬쳐쇼크를 먹어 도대체 이건 어떻게 동작하는 것일까 궁금증이 생겨
"간지 엘레베이터"를 작성하게 되었습니다. \(*-*)/

'''

import string


NONE = 0
UP = 1
DOWN = 2

class Building:
    def __init__(self, top_floor, lowest_floor):
        self.top_floor = top_floor
        self.lowest_floor = lowest_floor
        self.selector = Selector(top_floor, lowest_floor)
        self.elevators = self.selector.elevators
        return

    def create_new_elevator(self):
        elevator_alias = string.ascii_uppercase[len(self.elevators)]
        elevator_object = Elevator(self.top_floor, self.lowest_floor)
        self.selector.append_new_elevator(elevator_alias, elevator_object)
        return elevator_alias

    def call_at_to_go(self, current_floor, dest_foor ):
        alias = selector.get_optimal_elevator()
        return alias


class Selector:
    def __init__(self, top_floor, lowest_floor):
        self.top_floor = top_floor
        self.lowest_floor = lowest_floor
        self._elevators = dict()

    def get_optimal_elevator(self, src, dest):
        vector = NONE
        if current_floor < dest_floor:
            vector = UP
        elif current_floor > dest_floor:
            vector = DOWN
        pass

    def __get_not_working_elevators(self):
        pass

    def __get_upping_elevators(self):
        pass

    def __get_downing_elevators(self):
        pass

    def append_new_elevator(self, elevator, alias):
        elevator_alias = string.ascii_uppercase[len(self._elevators)]
        elevator = Elevator(self.top_floor, self.lowest_floor)
        self._elevators[elevator_alias] = elevator

    @property
    def elevators(self):
        return self._elevators

    pass


class Elevator:
    def __init__(self, top_floor, lowest_floor=1):
        self.top_floor = top_floor
        self.lowest_floow = lowest_floor
        self.reservated_queue = list()
        self.vector = bool()


if __name__ == '__main__':
    top_floor = 1
    lowest_floor = 10
    building = Building(top_floor, lowest_floor)
    building.create_new_elevator()
    building.create_new_elevator()
    building.create_new_elevator()
    #building.call_at(current_floor, destination_floor)

    building.call_at(1, 10)

    print(building.elevators)
