# -*- coding: utf-8 -*-

import http, json, os, re


class Command:
    def __init__(self, command='', args=None, fn=None):
        self.command = command
        self.args = args
        self.fn = fn


class Commander:
    def __init__(self):
        self.commands = {}

    def add(self, command, args, fn):
        self.commands[command] = Command(command, args, fn)

    def getCommand(self, command):
        return self.commands[command] if command in self.commands else None


class ChatActions:
    typing = 'typing'
    upload_photo = 'upload_photo'
    record_video = 'record_video'
    upload_video = 'upload_video'
    record_audio = 'record_audio'
    upload_audio = 'upload_audio'
    upload_document = 'upload_document'
    find_location = 'find_location'


class Bot:

    ChatActions = ChatActions

    def __init__(self, token):
        self.baseurl = 'https://api.telegram.org/bot'
        self.token = token
        self.commander = Commander()
        self.hook = None
        self.hookport = None
        self.hookhost = None


    def addCommand(self, command, args, fn):
        self.commander.add(command, args, fn)


    def setWebhook(self, hook=None):
        self.hook = hook or ''
        return http.request(self.baseurl + self.token + '/setWebhook', method='POST', body=json.dumps({'url': hook}), headers={'Content-Type': 'application/json'})


    def sendMessage(self, chat_id, text, parse_mode=True, disable_web_page_preview=True, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        data = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'disable_web_page_preview': disable_web_page_preview, 'disable_notification': disable_notification}
        if(reply_to_message_id): data['reply_to_message_id'] = reply_to_message_id
        if(reply_markup): data['reply_markup'] = reply_markup
        return http.request(self.baseurl + self.token + '/sendMessage', method='POST', body=json.dumps(data), headers={'Content-Type': 'application/json'})


    def sendFile(self, method, chat_id, filepath, **optional):
        data = {'chat_id': chat_id}
        for key in optional:
            data[key] = optional[key]
        with open(filepath, 'rb') as file:
            binary = file.read()
        filename = os.path.basename(filepath)
        return http.multipartFormData(self.baseurl + self.token + method, data, files=[(method.replace('/send', '').lower(), filename, photo)])


    def sendPhoto(self, chat_id, photopath, caption=None, reply_to_message_id=None, reply_markup=None):
        return sendFile('/sendPhoto', chat_id, photopath, caption, reply_to_message_id, reply_markup)


    def sendAudio(self, chat_id, audiopath, duration=None, performer=None, title=None, reply_to_message_id=None, reply_markup=None):
        return sendFile('/sendAudio', chat_id, audiopath, duration, performer, title, reply_to_message_id, reply_markup)


    def sendDocument(self, chat_id, documentpath, reply_to_message_id=None, reply_markup=None):
        return sendFile('/sendDocument', chat_id, documentpath, reply_to_message_id, reply_markup)


    def sendSticker(self, chat_id, stickerpath, reply_to_message_id=None, reply_markup=None):
        return sendFile('/sendSticker', chat_id, stickerpath, reply_to_message_id, reply_markup)


    def sendVideo(self, chat_id, videopath, duration=None, caption=None, reply_to_message_id=None, reply_markup=None):
        return sendFile('/sendVideo', chat_id, videopath, duration, caption, reply_to_message_id, reply_markup)


    def sendVoice(self, chat_id, voicepath, duration=None, reply_to_message_id=None, reply_markup=None):
        return sendFile('/sendVoice', chat_id, voicepath, duration, reply_to_message_id, reply_markup)


    def sendLocation(self, chat_id, latitude, longitude, reply_to_message_id=None, reply_markup=None):
        data = {}
        data['chat_id'] = chat_id
        data['latitude'] = latitude
        data['longitude'] = longitude
        if(reply_to_message_id): data['reply_to_message_id'] = reply_to_message_id
        if(reply_markup): data['reply_markup'] = reply_markup
        return http.request(self.baseurl + self.token + '/sendLocation', method='POST', body=json.dumps(data), headers={'Content-Type': 'application/json'})


    def sendChatAction(self, chat_id, action):
        data = {}
        data['chat_id'] = chat_id
        data['action'] = action
        return http.request(self.baseurl + self.token + '/sendChatAction', method='POST', body=json.dumps(data), headers={'Content-Type': 'application/json'})


    def getUserProfilePhotos(self, user_id, offset=None, limit=None):
        data = {}
        data['user_id'] = user_id
        if(offset): data.append(('offset', offset))
        if(limit): data.append(('limit', limit))
        return http.request(self.baseurl + self.token + '/getUserProfilePhotos', method='POST', body=json.dumps(data), headers={'Content-Type': 'application/json'})


    def getFile(self, file_id, filename=None, directory=None):
        data = {}
        data['file_id'] = file_id
        response = http.request(self.baseurl + self.token + '/getFile', method='POST', body=json.dumps(data), headers={'Content-Type': 'application/json'})
        if(response[0] != 200):
            return False
        jsonRespone = json.loads(response[2])
        if(jsonRespone['ok']):
            filepath = jsonRespone['result']['file_path']
            extension = filepath.split('.')[-1]
            import uuid, urllib
            basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), extension)
            savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
            downloadlink = 'https://api.telegram.org/file/bot%s/%s' % (self.token, filepath)
            urllib.urlretrieve(downloadlink, savefile)
            return True
        else:
            return False


    def getKeyboard(self, keyboard, resize_keyboard=None, one_time_keyboard=None, selective=None):
        data = {'keyboard': keyboard}
        if(resize_keyboard): data['resize_keyboard'] = resize_keyboard
        if(one_time_keyboard): data['one_time_keyboard'] = one_time_keyboard
        if(selective): data['selective'] = selective
        return data


    def getHiddenKeyboard(self, selective=None):
        data = {'hide_keyboard': True}
        if(selective): data['selective'] = selective
        return data


    def getForcedReplyKeyboard(self, selective=None):
        data = {'force_reply': True}
        if(selective): data['selective'] = selective
        return data


    def getUpdates(self, offset=None, limit=None, timeout=None):
        data = {}
        if(offset): data['offset'] = offset
        if(limit): data['limit'] = limit
        if(timeout): data['timeout'] = timeout
        return http.request(self.baseurl + self.token + '/getUpdates', method='GET', body=json.dumps(data), headers={'Content-Type': 'application/json'})


    def __onTextMessage(self, message):
        regex = re.compile(r'^(/[a-zA-Z0-9]+)')
        text = message['text']
        match = regex.search(text)
        cmd = None
        if(match):
            command = match.group(1)
            args = text[len(match.group(1)):].strip().split(' ')
            cmd =  self.commander.getCommand(command)
            if(cmd):
                cmd.fn(message, *args)
            else:
                self.onCommandNotFound(command)
        else:
            self.onTextMessage(text)


    def onCommandNotFound(self, command):
        print 'Command \'%s\' not found!' % command


    def onTextMessage(self, text):
        print 'message:', text

    def onPhotoMessage(self, message):
        print 'photo detected'


    def onVideoMessage(self, message):
        print 'video detected'


    def onDocumentMessage(self, message):
        print 'document detected'


    def onStickerMessage(self, message):
        print 'sticker detected'


    def onLocationMessage(self, message):
        print 'location detected'


    def onVoiceMessage(self, message):
        print 'voice detected'


    def startHookServer(self, host='127.0.0.1', port=3737, hookurl=None, verbose=False, webdebug=False, webverbose=False):
        self.hookhost = host
        self.hookport = port
        if(hookurl):
            self.hook = hookurl
            self.setWebhook()
        try:
            from bottle import Bottle, route, error, run, request, response, BaseRequest, static_file, HTTPResponse
        except Exception as e:
            raise

        class RequestDump(object):
            name = 'request_dump'
            api = 2

            def apply(self, fn, context):
                def _request_dump(*args, **kwargs):
                    print json.dumps(json.loads(request.body.read()), indent=4, separators=(',', ': '))
                    return fn(*args, **kwargs)
                return _request_dump

        def jsonResponse(data, headers=None, code=200):
            _headers = headers or {key: response.headers.get(key) for key in response.headers.keys()}
            _headers['content-type'] = 'application/json'
            _data = json.dumps(data) if type(data) == dict else data
            return HTTPResponse(_data, code, _headers)

        def hook():
            try:
                data = json.loads(request.body.read())

                message = data['message']
                if('text' in message):
                    self.__onTextMessage(message)
                elif('photo' in message):
                    self.onPhotoMessage(message)
                elif('video' in message):
                    self.onVideoMessage(message)
                elif('document' in message):
                    self.onDocumentMessage(message)
                elif('sticker' in message):
                    self.onStickerMessage(message)
                elif('location' in message):
                    self.onLocationMessage(message)
                elif('voice' in message):
                    self.onVoiceMessage(message)
                else:
                    print 'can\'t detect the message type'

            except Exception as e:
                raise
                # print '[ERROR] %s' % e
                # bot.sendMessage(data['message']['chat']['id'], '[ERROR] %s' % e)  # , data['message']['message_id'])
            return jsonResponse({'status': 'ok'})

        app = Bottle()
        app.route('/', method='POST', callback=hook)

        if(verbose): app.install(RequestDump())

        run(app, host=self.hookhost, port=self.hookport, debug=webdebug, quiet=not webverbose)
