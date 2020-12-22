### Это web-интерфейс для расчета коэффициента теплопередачи от грунта к сезонно-охлаждающим устройствам

#### Расчет выполняется в соответствии с Приложением Б СТО Газпром 2-2.1-390-2009 "Руководство по проектированию и применению сезонно-охлаждающих устройств для термостабилизации грунтов оснований фундаментов"

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Build Status](https://www.travis-ci.com/LeorFinkelberg/termostablizator.svg?branch=master)](https://www.travis-ci.com/LeorFinkelberg/termostablizator)
[![DeepSource](https://deepsource.io/gh/LeorFinkelberg/termostablizator.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/LeorFinkelberg/termostablizator/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/LeorFinkelberg/termostablizator.svg/?label=resolved+issues&show_trend=true)](https://deepsource.io/gh/LeorFinkelberg/termostablizator/?ref=repository-badge)

#### Запуск приложения

Для запуска приложения достаточно вызывать управляющий сценарий ```sou.py``` с помощью утилиты командной строки библиотеки [Streamlit](https://www.streamlit.io/)
```sh
$ pip install streamlit # установка библиотеки Streamlit
$ streamlit run sou.py
```
После запуска в окне командной оболочки появится сообщение
```sh
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.247:8501
```
и приложение запустится в браузере.
Чтобы остановить приложение нужно просто закрыть соответствующую вкладку браузера, а в командной оболочке завершить процесс с помощью ```Ctrl+C```.
