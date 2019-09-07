from .models import Item


def get_items():
    items = []
    for item in Item.objects.all():
        items.append(item)
    return items

def grab_item(uuid):
    item = Item.objects.get(uuid=uuid)
    return item.is_worthy
