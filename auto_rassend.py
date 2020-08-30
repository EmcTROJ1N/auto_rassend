#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vk_messages import MessagesAPI
from random import randint
from time import sleep
from vk_messages.utils import get_random
import os

auth_data = {
'login': '',
'passwd': ''
}

def check_auth():
    if not os.path.exists('auth_data.log'):
        auth_data['login'] = input('Введите логин: ')
        auth_data['passwd'] = input('Введите пароль: ')
        try:
            messages = MessagesAPI(login = auth_data['login'], password = auth_data['passwd'])
            with open('auth_data.log', 'w') as file:
                file.write(auth_data['login'] + '|' + auth_data['passwd'])
            print('Данные подтверждены')
            trigger = True
        except:
            trigger = False
            print('Данные введены неверно ...')
    else:
        with open("auth_data.log", 'r') as file:
            trigger = True
            for line in file:
                auth_data['login'] = line.split("|")[0]
                auth_data['passwd'] = line.split("|")[1]
                print(auth_data['login'])
                print(auth_data['passwd'])
            print('Данные подтверждены')
    return trigger

def auto_send_30(trig):
    if trig:
        messages = MessagesAPI(login = auth_data['login'], password = auth_data['passwd'])
        users = messages.method('groups.getMembers', group_id = 'zertsalia')
        poslanie = '''
          Здравствуй, дорогой друг!
          Меня зовут – Гордей Лестратов – и я представитель ролевой по книге 'Пардус' Евгения Гаглоева.
          Сейчас у нас объявлен поиск канонного персонажа и я хотел бы тебя пригласить поработать им.
          Если я тебя заинтересовал, то отправь "+" и я тебе обо всём подробно расскажу.
          Если тебе это неинтересно, то прошу, отправь "-".
          Хорошего дня 🥀
        '''
        sended = 0
        if not os.path.exists('data.log'):
            with open('data.log', 'w') as file:
                 pass
        for i in range(30):
            id = generate(users)
            with open('data.log', 'r') as file:
                pass
            sleep(1)
            try:
                messages.method('messages.send', peer_id = int(id), message = poslanie, random_id= get_random())
                print("Сообщение отправлено")
                sended += 1
                with open('data.log', 'a') as file:
                    file.write(str(id) + '\n')
            except:
                print("Личка закрыта,  " + str(id))
        print('Всего сообщений отправлено: ' + str(sended))

def generate(users):
    k = randint(0, 1000)
    id = users['items'][k]
    lines = 0
    pp = 0
    with open('data.log', 'r') as data:
        for line in data:
            lines += 1
    while pp < lines:
        with open('data.log', 'r') as data:
           for line in data:
                if line == id:
                    pp = 0
                    print('Обраружено совпадение!')
                    k = randint(0, 1000)
                    id = users['items'][k]
                    print(id)
                else:
                    pp += 1
    return id
trigger = check_auth()
auto_send_30(trigger)

