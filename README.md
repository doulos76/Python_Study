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

## 가상환경 및 패키지
* [참고](https://docs.python.org/ko/3/tutorial/venv.html)

### pip로 package 관리하기
* 필요 package 검색 예제

```
(tutorial-env) $ pop search simplejson
```

* 설치

```
(tutorial-env) $ pop install simplejson
```

* 내용 확인

```
(tutorial-env) $ pop show simplejson
```

* 가상환경에 설치된 내용 확인

```
(tutorial-env) $ pop list
```

* 설치된 package 삭제

```
(tutorial-env) $ pop uninstall simplejson
```