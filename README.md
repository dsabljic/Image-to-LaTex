# Image-to-LaTex

## App demo

![image](https://github.com/dsabljic/Image-to-LaTex/assets/83828394/98e8b449-1a59-45b3-aea6-d03123e28c19)

## Local setup

```sh
git clone [URL to your repository]
```

```sh
cd Image-to-LaTex
```

### Set up the .env file

```sh
echo OPENAI_API_KEY=your_key_here > .env
```

### Create virtual environment
```sh
python3 -m venv env
```

### Activate the environment

```sh
source env/bin/activate
```

### Install dependencies
```sh
pip3 -r install requirements.txt
```

### Run the app

```sh
uvicorn main:app --reload
```

### // TODO
- [x] Handwritten formula -> LaTex
- [ ] Image/Screenshot -> LaTex
- [ ] Copy the output to clipboard
- [ ] Visual improvements
