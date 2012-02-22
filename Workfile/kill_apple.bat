@echo off

net stop "iPod ªA°È"
taskkill /im AppleMobileDeviceService.exe /f
taskkill /im iTunesHelper.exe /f
taskkill /im applemobiledeviceservice.exe /f
