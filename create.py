import os
import time

import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class Create:

    def __init__(self):
        self.url = 'https://web.whatsapp.com'
        option = Options()
        self.driver = webdriver.Firefox(options=option)

    def create(self):
        self.driver.get(self.url)
        input('-' * 20 + '\n1 - Escaneie o código QR e aperte alguma tecla para continuar ')

    def define_params(self, group, user):
        link = []
        for i in range(len(group)):
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[3]/div').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div').click()
            for l in range(len(user)):
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input').send_keys(
                    user[i])
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[1]/div/div/div/div/div').click()
            if i == 0:
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/span/div').click()
            else:
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input').send_keys(
                    Keys.RETURN)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/span/div').click()
            img = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/input')
            img.send_keys("/home/ricardo/Documentos/SBCopy/Projects/bot/group-bot-whatsapp/create-group/img.jpg")
            time.sleep(3)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[1]/div[1]/div[2]').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[1]/div[1]/div[2]').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[1]/div[1]/div[2]').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[1]/div[1]/div[2]').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]').send_keys(
                group[i])
            time.sleep(3)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div').click()
            time.sleep(6)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[4]/div/header/div[2]').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[2]/div/div/span[2]/div').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]').send_keys(
                'asdasdas')
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]').send_keys(
                Keys.RETURN)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[3]').click()
            time.sleep(2)
            link.append(self.driver.find_element_by_xpath(
                '//*[@id="group-invite-link-anchor"]').text)

        print(link)

    @staticmethod
    def group():
        group_name_qtd = []
        group_qtd = int(input('Qual a quantidade de grupos? '))
        info = input('Os grupos tem nomes diferentes? S/N  ')
        if info.upper() == 'S' or info.upper() == 'SIM':
            for i in range(group_qtd):
                print('-' * 45)
                group_name_qtd.append(input('Qual nome do grupo #{} ? '.format(str(i))))
        else:
            name_default = input('Qual o nome padrão? ')
            index_group = int(input('Qual o indice inicial do grupo? ex:35 \n'))
            for i in range(group_qtd):
                group_name_qtd.append(name_default + '#' + str(index_group))
                index_group = index_group + 1

        return group_name_qtd

    @staticmethod
    def user():
        group_user = []
        qtd = int(input('Qual a quantidade de participantes desse grupo? '))
        for i in range(qtd):
            print('-' * 45)
            group_user.append(input('Digite o nome exato do contato: '))

        return group_user

    @staticmethod
    def image():
        data = {}
        data['img'] = input('Qual a localização completa da imagem do grupo?\n')
        data['describe'] = input('Qual a descrição completa do grupo?\n')

        return data


c = Create()
group = c.group()
user = c.user()
# c.image()
c.create()
c.define_params(group, user)
