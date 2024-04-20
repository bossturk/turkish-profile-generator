@echo off
rem Adım 1: Python paketini oluştur
echo Adım 1: Python paketini oluştur
python setup.py sdist bdist_wheel

rem Adım 2: Oluşturulan paketi yükle
echo Adım 2: Oluşturulan paketi yükle
twine upload dist/* --verbose

rem İşlem tamamlandı
echo İşlem tamamlandı
pause
