from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

import json


app = Flask(__name__, static_folder=".")
api = Api(app)
CORS(app)


class status (Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}

    def post(self):
        try:
            data = str(request.json)
            headers = str(request.headers)
            history = []
            with open("./history.json") as fp:
                history = json.load(fp)            
            history = [{ "headers": headers, "data": data }] + history
            with open("./history.json", "w") as fp:
                json.dump(history, fp)
            return { "headers": headers, "data": "OK" }
        except:
            return {'request': 'An Error Occurred during fetching Api'}


class History(Resource):
    def get(self):
        history = []
        with open("./history.json") as fp:
            history = json.load(fp)
        return { "history": history }


class ClearHistory(Resource):
    def get(self):
        with open("history.json", "w") as fp:
            json.dump([], fp)

    def post(self):
        with open("history.json", "w") as fp:
            json.dump([], fp)


class Command(Resource):
    def get(self):
        command = {}
        with open("command.json") as fp:
            command = json.load(fp)
        with open("command.json", "w") as fp:
            json.dump({}, fp)
        return command

    def post(self):
        command = {}
        with open("command.json") as fp:
            command = json.load(fp)
        with open("command.json", "w") as fp:
            json.dump({}, fp)
        return command


class CommandLock(Resource):
    def post(self):
        command = { }
        with open("command.json") as fp:
            command = json.load(fp)
        command["lock"] = True
        with open("command.json", "w") as fp:
            json.dump(command, fp)
        return command


class CommandUnlock(Resource):
    def post(self):
        command = { }
        with open("command.json") as fp:
            command = json.load(fp)
        command["unlock"] = True
        with open("command.json", "w") as fp:
            json.dump(command, fp)
        return command

class CommandShutdown(Resource):
    def post(self):
        command = { }
        with open("command.json") as fp:
            command = json.load(fp)
        command["shutdown"] = True
        with open("command.json", "w") as fp:
            json.dump(command, fp)
        return command

class CommandTurnOn(Resource):
    def post(self):
        command = { }
        with open("command.json") as fp:
            command = json.load(fp)
        command["turnon"] = True
        with open("command.json", "w") as fp:
            json.dump(command, fp)
        return command

class CommandBuzz(Resource):
    def post(self):
        command = { }
        with open("command.json") as fp:
            command = json.load(fp)
        command["buzz"] = True
        with open("command.json", "w") as fp:
            json.dump(command, fp)
        return command

class CommandDebug(Resource):
    def post(self):
        command = { }
        with open("command.json") as fp:
            command = json.load(fp)
        command["debug"] = True
        with open("command.json", "w") as fp:
            json.dump(command, fp)
        return command

class CommandReprogram(Resource):
    def post(self):
        command = { }
        with open("command.json") as fp:
            command = json.load(fp)
        command["reprogram"] = True
        with open("command.json", "w") as fp:
            json.dump(command, fp)
        return command

class BikeRegistry(Resource):
    def post(self):
        req = request.json
        print(req)
        if req and "IMEI" in req:
            return {
                "IMEI": req["IMEI"],
                "BIKERFID": "b9db8c947a",
                "REGISTRY": "C0240",
                "BIKETYPE": "CONVENTIONAL"
            }
        else:
            return {
                "error": "Need IMEI"
            }

    def get(self):
        req = request.json
        print(req)
        if req and "IMEI" in req:
            return {
                "IMEI": req["IMEI"],
                "BIKERFID": "b9db8c947a",
                "REGISTRY": "C0240",
                "BIKETYPE": "CONVENTIONAL"
            }
        else:
            return {
                "error": "Need IMEI"
            }

class Gps(Resource):
    def post(self):
        gps_data = request.json
        with open("gps.json", "w") as fp:
            json.dump(gps_data, fp)
        return gps_data

    def get(self):
        gps_data = {}
        with open("gps.json") as fp:
            gps_data = json.load(fp)
        return gps_data



api.add_resource(ClearHistory, '/api/clear_history')
api.add_resource(History, '/api/history')
api.add_resource(Command, "/api/command")
api.add_resource(CommandLock, "/api/lock")
api.add_resource(CommandUnlock, "/api/unlock")
api.add_resource(CommandShutdown, "/api/shutdown")
api.add_resource(CommandTurnOn, "/api/turnon")
api.add_resource(CommandBuzz, "/api/buzz")
api.add_resource(CommandDebug, "/api/debug")
api.add_resource(BikeRegistry, "/api/bike_registry")
api.add_resource(CommandReprogram, "/api/reprogram")
api.add_resource(Gps, "/api/gps")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")


if __name__ == '__main__':
    app.run()