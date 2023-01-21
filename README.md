
# :robot: Playwright 	

## Create Virtual Environment 
```bash
python -m venv ./venv
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Run Tests
Include `allure-dir` argument to generate test reporting files. Remove argument if not needed.
```bash
pytest --allure-dir=./results
```

## Generate Test report
```bash
allure serve ./results
```

## Run Parallel Tests
```bash
pytest -n <NUM>
```

## :wrench:	Troubleshooting

### :warning: Allure not recognized
```bash
allure : The term 'allure' is not recognized as the name of a cmdlet, 
function, script file, or operable        
```
### :heavy_check_mark: Solution
```bash
npm install -g allure-commandline --save-dev
```

### :warning: Actions failing due ```Missing X server or $DISPLAY```
This is because the container/VM running the Actions does not have a display/GPU.<br>

### :heavy_check_mark: Solution
Run tests on headless mode by setting:
``` python
browser = playwright.chromium.launch(headless=False)
```
