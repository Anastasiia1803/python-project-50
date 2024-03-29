# Вычислитель отличий (gendiff)
![Hexlet Badge](https://img.shields.io/badge/Hexlet-116EF5?logo=hexlet&logoColor=fff&style=for-the-badge)
[![Actions Status](https://github.com/Anastasiia1803/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Anastasiia1803/python-project-50/actions)
[![Check_my_Actions](https://github.com/Anastasiia1803/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/Anastasiia1803/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/494bdd544175e66ad82b/maintainability)](https://codeclimate.com/github/Anastasiia1803/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/494bdd544175e66ad82b/test_coverage)](https://codeclimate.com/github/Anastasiia1803/python-project-50/test_coverage)


#### Поддерживаемые форматы файлов
Проект поддерживает следующие форматы файлов для поиска отличий:

- YAML (.yaml, .yml)
- JSON (.json)
***
## Как найти различия между двумя файлами

1. Поместите два файла, которые вы хотите сравнить.a
2. Выполните команду для поиска различий:
```
poetry run gendiff file1.json file2.json
```
3. Замените file1.json и file2.json на названия ваших файлов
***
## Форматы вывода
Для выбора формата вывода различий, укажите флаг -f с названием форматтера. Возможные форматтеры:

- stylish (по умолчанию)
- plain
- json

#### Примеры команд для разных форматов вывода:

1. Вывод в стиле stylish
```
poetry run gendiff file1.json file2.json
```

2. Вывод в формате plain
```
poetry run gendiff -f plain file1.json file2.json
```

3. Вывод в формате json
```
poetry run gendiff -f json file1.json file2.json
```
***

### Демонстрация работы программы:
https://asciinema.org/a/hxI6GELsnlyPU5gRY8TAvM2PN