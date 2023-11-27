# программа для создания меню приложения
from dataclasses import dataclass, field
from dataclasses import asdict
import json
import os

from dbase import data_object as DB



class navi_dicts():

    def __init__(self):

        self.files = {
                        "menu": "menu_structure.json",
                        "sample": "menu_samples.json",
                        "button": "navi_buttons.json"
                        }

        self.start_menu = {
                        "создание меню": {
                                "navi_point": "create_menu",
                                        },
                        "создание кнопки": {
                                "navi_point": "create_button"
                                    },
                        "редактирование": {
                                "navi_point": "edit_structeres"
                                    },
                        }
        self.create_menu = {
                        "dialog": {
                            "добавьте краткое описание": {
                                    "key_result_dict": "descript",
                                    "list_samples": None,
                                    "type_answer": str
                                            },
                            "выберите шаблон": {
                                    "key_result_dict": "ids_samples",
                                    "list_samples": get_list_samples_names,
                                    "type_answer": "list_int"
                                            },
                            "добавьте кнопки": {
                                    "key_result_dict": "ids_buttons",
                                    "list_samples": get_list_buttons_names,
                                    "type_answer": "list_int"
                                            },
                            "каким группам доступно": {
                                    "key_result_dict": "ids_groups",
                                    "list_samples": get_list_groups_names,
                                    "type_answer": "list_int"
                                            }
                                    },
                        "data": {"filename": self}
                                }
        self.create_button = {
                        "Текст кнопки": {
                                "key_result_dict": "text_button",
                                "list_samples": None,
                                "type_answer": str
                                        },
                        "каким группам доступно": {
                                "key_result_dict": "ids_groups",
                                "list_samples": get_list_groups_names,
                                "type_answer": "list_int"
                                        },
                        "команда": {
                                "key_result_dict": "command",
                                "list_samples": get_list_groups_names,
                                "type_answer": str
                                        },
                        "ссылка на дочернее меню": {
                                "key_result_dict": "id_next_menu",
                                "list_samples": get_list_groups_names,
                                "type_answer": "list_int"
                                        },
                        "добавьте краткое описание": {
                                "key_result_dict": "descript",
                                "list_samples": None,
                                "type_answer": str
                                        }
                         }


def screen_empty():
    os.system('clear')


def add_object_to_file(filename, dict):
    with open(filename, "a") as file:
        json.dump(dict, file, indent=4)
        print("\n", file=file)
        return file

#11111111111111111111111111111111111111111111111111111111111111111111111
# запись созданного обьекта в файл json
def save_new_object(dict_button, navi):
    try:
        add_object_to_file(file_buttons, dict_button)
        return True
    except:
        print("Ошибка записи в файл!")
        return False



# проверка введенных данных
def get_user_data(type_return=None):
    user_text = input()
    if type_return:
        try:
            if type_return == "list_int":
                return [int(num) for num in user_text.split()]
            else:
                return type_return(user_text)
        except:
            return 999
    return user_text


# список для выбора шаблонных кнопок и блоков кнопок
def get_list_samples_names():
    return "в разработке"


# список созданных кнопок
def get_list_buttons_names():
    return "в разработке"


# список активных пользовательских групп
def get_list_groups_names():
    return "в разработке"


if __name__ == "__main__":

    navi_dict = navi_dicts()
    navi = "main"

    while True:
        screen_empty()

        match navi:
            # главное меню
            case "main":
                dialog = navi_dict.start_menu
                while True:
                    data = {id_call: quest for id_call, quest in enumerate(dialog.keys())}
                    [print(f'{id_answer}: {quest}') for id_answer, quest in data.items()]
                    answer_input = get_user_data(int)
                    if answer_input in data.keys():
                        navi = dialog[data[answer_input]]["navi_point"]
                        break
            # создание меню
            case "create_menu":
                result_dict = {}
                dialog = navi_dict.create_menu
                for step in dialog.keys():
                    while True:
                        print(f'{step}', end=': ')
                        answer = get_user_data(dialog[step]["type_answer"])
                        if answer != 999:
                            result_dict[dialog[step]["key_result_dict"]] = answer
                            break

                if save_new_object(result_dict, navi, dialog):
                    print("Меню создано, нажмите Enter для продолжения")
                    input()

                navi = "main"
            # создание кнопки
            case "create_button":
                result_dict = {}
                dialog = navi_dict.create_button

                for step in dialog.keys():
                    while True:
                        print(f'{step}', end=': ')
                        answer = get_user_data(dialog[step]["type_answer"])
                        if answer != 999:
                            result_dict[dialog[step]["key_result_dict"]] = answer
                            break

                if save_new_object(result_dict, navi, dialog):
                    print("Меню создано, нажмите Enter для продолжения")
                    input()

                navi = "main"
            # редкактирование обьектов
            case "edit_structeres":
                screen_empty()
                input("в разработке")
                navi="main"

            # создание шаблона
            case "create sample":
                screen_empty()
                input("в разработке")
                navi="main"



        # выход из программы
        if navi == "exit":
            breake
