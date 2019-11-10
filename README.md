# Python_Study


## Python 설치

* [Python download site](https://www.python.org/downloads/)
* Python 3 권장

## 가상환경 설치

* 아래 예시와 같이 사용

```
➜  Python_Study git:(master) ✗ python3 -m venv python_basic
ls
➜  Python_Study git:(master) ✗ ls
README.md      SourceCode     python_basic   section01.py   section02-1.py section02-2.py
➜  Python_Study git:(master) ✗ cd python_basic
➜  python_basic git:(master) ✗ ls
bin        include    lib        pyvenv.cfg
➜  python_basic git:(master) ✗ cd bin
➜  bin git:(master) ✗ ls
activate         activate.fish    easy_install-3.7 pip3             python
activate.csh     easy_install     pip              pip3.7           python3
➜  bin git:(master) ✗ source ./activate
(python_basic) ➜  bin git:(master) ✗ deactivate
➜  bin git:(master) ✗ source ./activate
(python_basic) ➜  bin git:(master) ✗ deactivate       
➜  bin git:(master) ✗ source ./activate
(python_basic) ➜  bin git:(master) ✗ code```
```

## VSCode 설치 및 설정

* 폴더 설정
* Python 설정
* Python: Select Interpreter
* tasks.json 설정 (단축키 설정)
