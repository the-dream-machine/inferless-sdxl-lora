INPUT_SCHEMA = {
    "model_id":{
      'datatype': 'STRING',
      'required': True,
      'shape': [1],
      'example': ["stable-diffusion-xl-base-1.0"]
    },
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["a logo for a coffe shop, coffe"]
    },
    "negative_prompt": {
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
