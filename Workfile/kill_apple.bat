@echo off

net stop "iPod �A��"
taskkill /im AppleMobileDeviceService.exe /f
taskkill /im iTunesHelper.exe /f
taskkill /im applemobiledeviceservice.exe /f
