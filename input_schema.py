INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["a logo for a coffe shop, coffe"]
    },
    "negative": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["bad art, ugly, deformed, watermark, duplicated, multiple images"]
    },
     "color": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["orange, yellow, black, purple"]
    }
}
