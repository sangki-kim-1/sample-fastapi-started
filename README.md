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
uvicorn main:app --reload
```

## Reference
- [공식문서](https://fastapi.tiangolo.com/ko/)