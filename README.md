
This scripts is use to check web url status, if HTTP status code is not `200`,
it will send an notification to slack channel that you want:

## Requirements
AWS account and permissions to use AWS Lambda , or
you can run this on your local by cronjob

## Usage
Following to fill in information that scripts need :

```
HOOK_URL = "<slack_url>"

'channel': "<channel_name>"

'username':'<slack_username>'

target = [
    "https://www.exsample.com",
    "https://www.123.com"
]
```

Find `<slack_url>`, `channel_name`, `<slack_username>` and `target url` in the script

Replace all information that you want , and we are good to go !
