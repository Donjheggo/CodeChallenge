def fitsInOneBox(boxes):
    boxes.sort(key=lambda x: (x['l']*x['w']*x['h']), reverse=True)
    for i in range(1, len(boxes)):
        if boxes[i]['l'] >= boxes[i-1]['l'] or boxes[i]['w'] >= boxes[i-1]['w'] or boxes[i]['h'] >= boxes[i-1]['h']:
            return False

    return True



boxes = [
    {'l': 8, 'w': 8, 'h': 8},
    {'l': 5, 'w': 7, 'h': 6},
    {'l': 3, 'w': 2, 'h': 3}
]

print(fitsInOneBox(boxes))
