from models import Item
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ItemLista(Resource):
    def get(self):
        item = Item.query.all()
        response = [{'id': i.id, 'nome': i.nome} for i in item]
        return response

    def post(self):
        dados = request.json
        item = Item(id=dados["id"], nome=dados["nome"])
        item.save()
        response = {'id': item.id,
                    'nome': item.nome}
        return response

    def put(self):
        dados = request.json
        item = Item.query.all()
        print(item)
        print(dados)
        item = Item.query.filter_by(id=dados["id"]).first()
        item.nome = dados["nome"]
        print(item)
        item.save()
        response = {'id':item.id,
                    'nome':item.nome}
        # response = [{'id':i.id,
        #             'nome':i.nome} for i in item]

        # response = [{'id': i.id, 'nome': i.nome} for i in item]

        return response

    def delete(self):
        print("<<<delete>>>")
        dados = request.json
        item = Item.query.filter_by(id=dados["id"]).first()
        item.delete()
        itemLista = Item.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in itemLista]
        return response

api.add_resource(ItemLista, '/item/')

if __name__ == '__main__':
    app.run(debug=True)
