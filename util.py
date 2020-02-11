from models import Item

def teste():
    item = Item(id=2, nome='TESTE2')
    item.save()

if __name__ == '__main__':
    teste();