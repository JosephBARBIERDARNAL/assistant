# AI + PureData + Raspberry Pi = <3

Source code for an exhibition by [Maurice Lebrun](https://mauricelebrun.com) that simulates a virtual assistant, *AI + PureData* powered, of Felix Arnaudin.

The whole set-up was done using a simple Raspberry Pi 4 (Model B, 2GB), PureData and less than a hundred lines of code.

> PureData: 0.54-1

> Python: 3.11.2 (openai==1.12.0, pygame==2.5.2)

### How to reproduce set up?

- Get source code and navigate through it:
```
git clone https://github.com/JosephBARBIERDARNAL/assistant.git
cd assistant
```

- Install PureData:
```
sudo apt-get install puredata
```

- Install PureData packages

TODO

- Create a Python virtual environment:
```
python -m venv venv
source venv/bin/activate
```

- Install required packages
```
pip install openai pygame
```

- Define your API key: in **`ai.py`** change **`os.environ.get("OPENAI_API_KEY")`** with your actual API key (in quotes) from OpenAI, available at their [platform](https://platform.openai.com).

- Run the project

```
puredata VIZUALIZE_NEW_FA.pd
python main.py
```

And that's it!