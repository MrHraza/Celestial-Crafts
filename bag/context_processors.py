from .bag_operations import Bag


def bag_total(request):
    bag = Bag(request)
    return {
        'grand_total': bag.get_total_cost()
    }
