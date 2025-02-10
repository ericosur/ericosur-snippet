phony: help

help:
	@echo use __make build__ to build the dotnet project
	@echo use __make decrypt__ to decrypt file
	@echo use __make encrypt__ to encrypt file

build:
	@echo try to build dotnet project
	@cd DecryptApp ; dotnet build

decrypt:
	@echo decrypt...
	@./wtfsave -d kaede.savedata.json the_dict.json

encrypt:
	@echo decrypt...
	@./wtfsave -c the_dict.json hacked.json
