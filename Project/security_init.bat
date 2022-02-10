@echo off
 
set /p TOKEN="TOKEN: "
set /p PAYMENT_TOKEN="PAYMENT_TOKEN: "
 
mkdir Security
cd Security
echo TOKEN = r'%TOKEN%' > TOKEN.py
echo PAYMENT_TOKEN = r'%PAYMENT_TOKEN%'>>TOKEN.py
