# WifiMicroMusicStation
> WifiMicroMusicStation - устройство в корпусе ретро-радио для автономного проигрывания музыки на ESP8266 и DFPlayerMini

## Стек
- Прошивка
  - MicroPython
    - ntptime
    - network
  - [micropython-dfplayer by ShrimpingIt](https://github.com/ShrimpingIt/micropython-dfplayer)
- Железо
  - ESP8266 (NodeMCU)
  - DF Player Mini
  - Динамик

## Возможности
- Воспроизведение любых mp3 треков с microSD карты
- Синхронизация времени по wifi
- Вопроизведение разной музыки с разной громкостью, в зависимости от времени суток (настраивается в конфигурационном файле)
- Обновление конфигурационного файла по wifi

## Минимальный config.txt
    WLAN_id = network
    WLAN_password = password
    WLAN_static_ip = 192.168.32.240
    WLAN_netmask = 255.255.0.0
    WLAN_gateway = 192.168.32.1
    WLAN_DNS_server = 8.8.8.8

    Folders = 3
    Files = 9, 13, 14
    Volume = 5, 10, 20, 25, 20, 10, 5 
    TimeZone = + 4

    #							 1   2   3   4   5   6   7
    --- PLAY RULES ---									
    !01(Описание папки) 	   = 1 | 1 | 1 | 1 | 1 | 1 | 1
    --- PLAY RULES ---
[Подробный пример config.txt с комментариями](./configs/example_config.txt)

## Подключение DF Player Mini к ESP8266
| NodeMCU	|DFPlayerMini|
|:-----------:|:-----------:|
|	D2 		|	Busy        |
|	D4		|	 RX         |
|	A0		|	DAC_L       |
| VIN(5V)	|	VCC         |
|	GND		|	GNDx2       |

## Запуск
1) Скопировать файлы `boot.py` и `main.py`, а так же `./configs/config.txt` и `./logs/log.txt` в корень виртуальной ФС ESP8266
2) Перезапустить ESP8266
3) Have fun!