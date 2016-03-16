telegram-bot
============

Create telegram bot services in python.

Installation
------------

Install through **pip**.

::

    $ pip install telegram-bot

or get from source

::

    $ git clone https://github.com/gravmatt/telegram-bot.git
    $ cd telegram-bot
    $ python setup.py install

Usage
-----

This is just a wrapper for the Telegram Bots API.

The readme just covers the usage of this module.

For more details about the Telegram Bots API, visit `Telegram Bots API
Documentation <https://core.telegram.org/bots/api>`__.

Create a bot
------------

::

    from telegram import Bot, ChatActions

    myBot = Bot('1234:mySuperSecetTokenFromBotFather')

getMe
-----

::

    result = myBot.getMe()

`Telegram Bots API
\| getMe <https://core.telegram.org/bots/api#getme>`__

sendMessage
-----------

::

    result = myBot.sendMessage(chat_id, text, parse_mode='Markdown', disable_web_page_preview=True, disable_notification=False, reply_to_message_id=None, reply_markup=None)

`Telegram Bots API \|
sendMessage <https://core.telegram.org/bots/api#sendmessage>`__

forwardMessage
--------------

::

    result = myBot.forwardMessage(chat_id, from_chat_id, message_id, disable_notification=None)

`Telegram Bots API
\| forwardMessage <https://core.telegram.org/bots/api#forwardmessage>`__

sendPhoto
---------

::

    result = myBot.sendPhoto(chat_id, photopath, caption=None, reply_to_message_id=None, reply_markup=None)

`Telegram Bots API
\| sendPhoto <https://core.telegram.org/bots/api#sendphoto>`__

sendAudio
---------

::

    result = myBot.sendAudio(chat_id, audiopath, duration=None, performer=None, title=None, reply_to_message_id=None, reply_markup=None)

`Telegram Bots API
\| sendAudio <https://core.telegram.org/bots/api#sendaudio>`__

sendDocument
------------

::

    result = myBot.sendDocument(chat_id, documentpath, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

`Telegram Bots API
\| sendDocument <https://core.telegram.org/bots/api#senddocument>`__

sendSticker
-----------

::

    result = myBot.sendSticker(chat_id, stickerpath, disable_notification=None, reply_to_message_id=None, reply_markup=None)

`Telegram Bots API
\| sendSticker <https://core.telegram.org/bots/api#sendsticker>`__

sendVideo
---------

::

    result = myBot.sendVideo(chat_id, videopath, duration=None, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

`Telegram Bots API
\| sendVideo <https://core.telegram.org/bots/api#sendvideo>`__

sendVoice
---------

::

    result = myBot.sendVoice(chat_id, voicepath, duration=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

`Telegram Bots API
\| sendVoice <https://core.telegram.org/bots/api#sendvoice>`__

sendLocation
------------

::

    result = myBot.sendLocation(chat_id, latitude, longitude, disable_notification=None, reply_to_message_id=None, reply_markup=None)

`Telegram Bots API \|
sendLocation <https://core.telegram.org/bots/api#sendlocation>`__

sendChatAction
--------------

::

    result = myBot.sendChatAction(chat_id, action)

    # action = one of the ChatActions (need to be imported first)

    ChatActions.typing
    ChatActions.upload_photo
    ChatActions.record_video
    ChatActions.upload_video
    ChatActions.record_audio
    ChatActions.upload_audio
    ChatActions.upload_document
    ChatActions.find_location

`Telegram Bots API \|
sendChatAction <https://core.telegram.org/bots/api#sendchataction>`__

getUserProfilePhotos
--------------------

::

    result = myBot.getUserProfilePhotos(user_id, offset=None, limit=None)

`Telegram Bots API \|
getUserProfilePhotos <https://core.telegram.org/bots/api#getuserprofilephotos>`__

getFile
-------

::

    result = myBot.getFile(file_id, filename=None, directory=None)

`Telegram Bots API \|
getFile <https://core.telegram.org/bots/api#getfile>`__

Inline module
-------------

**Sorry, but it is currently not supported**

**But it will follow soon!**

Thanks
======

`bottle Project <https://github.com/bottlepy/bottle>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**`Bottle Micro Web Framework -
http://bottlepy.org <http://bottlepy.org>`__**

Licence
-------

The MIT License (MIT)

Copyright (c) 2016 René Tanczos

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
