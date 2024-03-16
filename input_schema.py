INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["logo,a logo for a coffe shop, coffe"]
    },
    "negative": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["bad art, ugly, deformed, watermark, duplicated"]
    }
}
