## Before usage

![Aiogram version](https://img.shields.io/badge/Aiogram-2.17.1-informational)
![Project status](https://img.shields.io/badge/Status-WIP-red)

### Why should you do this? -> check [this](https://github.com/Nps-rf/AiogramTB/blob/master/Project/ClientSide.py#:~:text=from%20Security.TOKEN%20import%20PAYMENT_TOKEN) or [this](https://github.com/Nps-rf/AiogramTB/blob/master/Project/create.py#:~:text=from%20Security.TOKEN%20import%20TOKEN)

* **Command line way [<img align="left" width="22px" src="https://cdn2.iconfinder.com/data/icons/ecqlipse2/CMD.png"/>][cmd]**: 
  * `mkdir Security`
  * `cd Security`
  * `echo TOKEN = r'YOUR:TOKEN'  > TOKEN.py`
  * `echo PAYMENT_TOKEN = r'YOUR:TOKEN'>>TOKEN.py`
* **Manual method [<img align="left" width="22px" src="https://cdn1.iconfinder.com/data/icons/support-centre-hand-drawn-design/512/hand_book_support_centre-256.png"/>][manual]**
  * **Create `Security` directory in project folder**
  * **In this directory, create new file `TOKEN.py`**
  * **In `TOKEN.py` create `TOKEN` variable with raw string value of your bot token**
  * **Then, create `PAYMENT_TOKEN` variable with raw string value of your payment token**
* **Or just use `security_init.bat`**


[cmd]: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
[manual]: https://compass-ssl.microsoft.com/assets/a9/0e/a90e9ef3-402e-4258-a31f-0a023989d4f1.pdf?n=Windows_10_Desktop_QS.pdf
