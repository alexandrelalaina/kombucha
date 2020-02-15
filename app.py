from models import Item, Tipo
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class ItemLista(Resource):
    def get(self):
        print("<<<ItemLista>>>")
        item = Item.query.all()
        print(item)
        for i in item:
            print(format(i.tipo))

        print("fazer response")
        response = []
        for i in item:
            response.append({'id': i.id, 'nome': i.nome, 'tipo': i.tipo.descr })
        return response

    def post(self):
        print("<<<ItemLista post>>>")
        dados = request.json
        print(dados)
        item = Item(id=dados['id'], nome=dados['nome'])
        tipo = Tipo.query.filter_by(id=dados['tipo']).first()
        item.tipo = tipo
        item.save()
        response = {'id': item.id,
                    'nome': item.nome,
                    'tipo': item.tipo}
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


class ItemTipoLista(Resource):
    def get(self):
        tipo = Tipo.query.all()
        response = [{'id':x.id, 'descr':x.descr} for x in tipo]
        return response


api.add_resource(ItemLista, '/item/')
api.add_resource(ItemTipoLista, '/itemTipo/')

if __name__ == '__main__':
    app.run(debug=True)
