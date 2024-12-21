# Audio CV

Creating a tool which ask user to upload resume file and this will generate audio file from that resume and also the transcript

> [!Note]
> this project was build during in-person hackathon by peerlist on 21 Dec 2024 at Scaler school of technology, Bengaluru

## How to Start

below are the steps 

### pre-requisite

1. Install python v 3.11 and higher
2. Install virtual environment package `venv`  and other useful package
  
  > pip install venv pipreqs vulture 

### Create virtual environment, which create `.venv` folder

```sh
   python3 -m venv ~/some/path/to/.venv
```

### Activate the virtual environment

```sh
  > source ~/some/path/to/.venv/bin/activate
```

Note: to verify the activation of virtual environment, check does folder name (`.venv`) displayed ahead of terminal prompt.

### Create requirement txt file

```sh
 pipreqs . --force --ignore .venv   
```

this will create **requirements.txt** file

### Install required dependencies

```sh
> python3 -m pip install -r requirements.txt
```

Note: to check all installed package, run `python3 -m pip list`

### Run the application

```sh
  streamlit run app.py
```

Open [http://localhost:8085/](http://localhost:8085/)

Note: to change the port; create `.streamlit/config.toml` file inside `scripts` folder and write below

```toml
[server]
port = 8085
```

Note: to deactivate virtual environment type `source deactivate`

## API Endpoints

below are the APi which will be used

- `resume/list`
- `resume/upload`

## References

- [Python download](https://www.python.org/downloads)
- [Official document for virtual environment](https://docs.python.org/3/library/venv.html)
- [Document on netlify](https://image-generator-doc.netlify.app/)
- [Python tips](https://www.airplane.dev/blog/12-useful-python-scripts-for-developers)
