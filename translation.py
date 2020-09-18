class Translation(object):
    START_TEXT = """Hi!
😬Thank you for using me😬
Enter your Telegram Phone Number
To get the APP-ID from my.telegram.org
"""
    AFTER_RECVD_CODE_TEXT = """I see!!!!
now please send the Telegram code that you received from Telegram
Please note it down that i do not take any information from this bot!
This bot is runned only for the purposes of getting APP_ID and APP_HASH....


This Bot is only used for the purpose of getting the APP ID from my.telegram.org
Do not use it for any illegal purposes

"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n @lolboyisback"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
