# PyCoder 

Este proyecto utiliza modelos de Transformers para el entrenamiento y ejecución de un modelo de lenguaje causal. El objetivo es generar código de Python a partir de un prompt establecido.

## Requisitos Previos
- Python 3.6 o superior
- Biblioteca transformers
- Archivo de configuración config.json
- Archivos train.py y main.py

### 1. Instalación de Dependencias

```shell
pip install transformers
```

## ¿ Como se configura ?

1. En la raíz del proyecto existe un archivo `config.json`, ahí debe de poner el nombre del proyecto a ejecutar 


```json
{
	"proyect":"example"
}
```

2. Dentro de ese directorio debe existir otro archivo `config.json` que contendrá la siguiente configuración


```json
{
  "model_name": "Qwen/Qwen2.5-Coder-1.5B-Instruct",
  "prompt": "Hazme un simple ejemplo de un código de Python",
  "settings": {
    "torch_dtype": "auto",
    "device_map": "auto",
    "tokenize": false,
    "add_generation_prompt": true,
    "max_new_tokens": 512,
    "skip_special_tokens": true
  }
}

```


* model_name: Especifica el nombre del modelo que se utilizará.

* prompt: Es el mensaje o instrucción inicial que se le dará al modelo para que genere el código de Python.

* torch_dtype: Define el tipo de datos de PyTorch que se utilizará. En este caso, se ha establecido en "auto", lo que significa que PyTorch seleccionará automáticamente el tipo de datos más adecuado según el contexto.

* device_map: Especifica el dispositivo (GPU, CPU) en el que se ejecutará el modelo. Al igual que con "torch_dtype", se ha establecido en "auto", lo que permite que el modelo elija el dispositivo más apropiado.

* tokenize: Indica si se debe realizar la tokenización del texto de entrada antes de pasarlo al modelo. En este caso, se ha establecido en "false", lo que significa que el texto no será tokenizado previamente.

* addgenerationprompt: Determina si se debe incluir el prompt de generación al texto de entrada para el modelo. En esta configuración, se ha establecido en "true", lo que significa que el prompt se agregará al texto de entrada antes de la generación.

* maxnewtokens: Define el máximo número de tokens nuevos que se pueden generar en la salida del modelo. En este caso, se ha establecido en 512, lo que limita la extensión de la salida generada.

* skipspecialtokens: Indica si se deben omitir los tokens especiales al decodificar la salida del modelo. Cuando se establece en "true", los tokens especiales como los delimitadores de inicio y fin serán omitidos en la salida final.



### 3. Entrenamiento del Modelo
Para entrenar el algoritmo, ejecuta el archivo train.py. Este script se encargará de crear y exportar el modelo en la carpeta especificada.

```shell
python train.py
```

### 4. Ejecución del Modelo
Para ejecutar el modelo y generar código de Python a partir de un prompt, utiliza el archivo main.py.

```shell
python main.py
```