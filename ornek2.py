from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        data = pd.read_csv('employees.csv')
        data = data.to_dict('records')
        return {'veri': data}, 200

    def post(self):
        json = request.get_json()
        req_data = pd.DataFrame({
            'isim': [json['isim']],
            'yas': [json['yas']],
            'departman': [json['departman']],
            'maas': [json['maas']]
        })
        data = pd.read_csv('employees.csv')
        data = pd.concat([data, req_data], ignore_index=True)
        data.to_csv('employees.csv', index=False)
        return {'mesaj': 'Çalışan kaydı başarıyla eklendi.'}, 200

    def delete(self):
        isim = request.args.get('isim')
        data = pd.read_csv('employees.csv')

        if isim in data['isim'].values:
            data = data[data['isim'] != isim]
            data.to_csv('employees.csv', index=False)
            return {'mesaj': 'Çalışan kaydı başarıyla silindi.'}, 200
        else:
            return {'mesaj': 'Çalışan kaydı bulunamadı.'}, 404


api.add_resource(Employees, '/employees')
api.add_resource(Name, '/<string:name>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)