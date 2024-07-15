# FastAPI

## Version
- Python 3.12

## Installation
- venv 가상환경
``` shell
python3 -m venv .venv
source .venv/bin/activate
```

- FastAPI install
``` shell
pip install fastapi
```

- (Optional) 프로덕션 환경
``` shell
pip install "uvicorn[standard]"
```

## Local Started
``` shell
fastapi dev main.py
```

``` shell
uvicorn main:app --reload
```

## Dot env
```
export ENVIRONMENT=production
uvicorn main:app --reload
```

## Test
- swagger : http://localhost:8000/docs
- api docs : http://localhost:8000/redoc

## 기타
- `requirements.txt` freeze
``` shell
pip freeze > requirements.txt
```

## Reference
- [공식문서](https://fastapi.tiangolo.com/ko/)