from flask_restful import Resource, request

class Password(Resource):

    def get(self):
        psw=request.args.get('password')
        if psw=="myCheck":
            return True, 200
        return False, 200
