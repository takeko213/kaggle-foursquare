# https://qiita.com/akeome/items/e1e0fecf2e754436afc8
def send(notification_message):
    """
    LINEに通知する
    """
    import slackweb
    import os
    from dotenv import load_dotenv
    load_dotenv

    slack_url = os.getenv('SLACK_URL')
    s = slackweb.Slack(url=slack_url)
    s.notify(text=notification_message)