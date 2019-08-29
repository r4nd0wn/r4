import webview
username = 'derdickeelch'
chathtml = '''
<!DOCTYPE html>
<html>

    <head>
        <meta charset="utf-8">
        <title></title>
        <meta name="author" content="r4nd0wn">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!--<meta http-equiv="refresh" content="100">-->
    </head>
    <body>
        <iframe frameborder="0"
        scrolling="no"
        id="chat_embed"
        src="https://www.twitch.tv/embed/shlorox/chat"
        height="870"
        width="370">
        </iframe>
    </body>
</html>'''
tc = webview.create_window(username + "'s Twitch Chat", html=chathtml, js_api=None, width=400, height=900, resizable=False, fullscreen=False, confirm_close=False)
webview.start(tc)