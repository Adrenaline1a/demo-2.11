#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    def pattern(surname, firstname):
        return "Уважаемый {} {}! Вы делаете работу по замыканиям функций.".format(surname, firstname)
    return pattern


if __name__ == '__main__':
    print(main()(input('Введите фамилию: '), input('Введите имя: ')))
