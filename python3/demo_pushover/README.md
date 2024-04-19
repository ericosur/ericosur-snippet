# readme

demo how to use pushover.net web service to send notification to predefined devices

## pushover

require module: requests

config file from: ```~/Private/pushover-net.json```

### (deprecated) send notification via email gateway

require module: yagmail

config file from: ```~/Private/gmail-app-local.json```

### sounds

request sounds list (GET method)

```bash
curl https://api.pushover.net/1/sounds.json?token=<api token>
```
