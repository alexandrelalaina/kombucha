from models import Item, ItemTipo

def teste():
    item = Item(id=2, nome='TESTE2')
    item.save()

def cargaItemTipo():
    itemTipo = ItemTipo(id=3, descr="Produto Acabado")
    itemTipo.save()

if __name__ == '__main__':
    # teste();
    cargaItemTipo()