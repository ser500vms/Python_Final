"""

Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.

"""

import doctest
import logging


FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.ERROR, filemode='a', filename='my_log_file.log',
                    encoding='utf-8')
logger = logging.getLogger('task_1')


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        """
        Тестирование атрибута last_name.
        Убедитесь, что атрибут last_name возвращается в верхнем регистре, то есть "Ivanov".

        >>> em = Employee('ivanov', 'ivan', 'ivanovich', 30, 'manager', 50000)
        >>> em.last_name
        'Ivanov'

        """
        try:
            self.last_name = last_name.title()
        except AttributeError:
            logger.error(f'Вы ввели неверный атрибут - last_name. Ваш ввод - {last_name}')
        try:
            self.first_name = first_name.title()
        except AttributeError:
            logger.error(f'Вы ввели неверный атрибут - first_name. Ваш ввод - {first_name}')
        try:
            self.patronymic = patronymic.title()
        except AttributeError:
            logger.error(f'Вы ввели неверный атрибут - patronymic. Ваш ввод - {patronymic}')
        try:
            self._age = int(age)
        except ValueError:
            logger.error(f'Вы ввели неверный атрибут - age. Ваш ввод - {age}')
    def full_name(self):
        """
        Тестирование метода full_name().
        Убедитесь, что метод full_name() возвращает правильное полное имя в формате "Ivanov Ivan Ivanovich".

        >>> em = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        >>> em.full_name()
        'Ivanov Ivan Ivanovich'

        """
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        """
        Тестирование метода birthday().
        Вызовите метод birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.

        >>> em = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        >>> em.birthday()
        >>> em.get_age()
        31

        """
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        try:
            self.position = position.title()
        except AttributeError:
            logger.error(f'Вы ввели неверный атрибут - position. Ваш ввод - {position}')
        try:
            self.salary = float(salary)
        except ValueError:
            logger.error(f'Вы ввели неверный атрибут - salary. Ваш ввод - {salary}')

    def raise_salary(self, percent: float):
        """
        Тестирование метода raise_salary().
        Вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.

        >>> emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        >>> emp.raise_salary(10)
        >>> emp.salary
        55000.0

        """
        self.salary += self.salary * (percent / 100)

    def __str__(self):
        """
        Тестирование метода __str__().
        Убедитесь, что метод __str__() возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".

        >>> em = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
        >>> print(em)
        Ivanov Ivan Ivanovich (Manager)

        """
        try:
            return f'{self.full_name()} ({self.position})'
        except AttributeError:
            logger.error(f'Ошибка в вызове метода __str__. передан неверный атрибут')


if __name__ == '__main__':
    emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
    emp2 = Employee(12,13,134,'sds', 24, '23')
    # doctest.testmod(verbose=True)
    print(emp)
