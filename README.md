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

## Deployment
- uvicorn
  - https://www.uvicorn.org/deployment/

``` shell
$ uvicorn --help
Usage: uvicorn [OPTIONS] APP

Options:
  --host TEXT                     Bind socket to this host.  [default:
                                  127.0.0.1]
  --port INTEGER                  Bind socket to this port. If 0, an available
                                  port will be picked.  [default: 8000]
  --uds TEXT                      Bind to a UNIX domain socket.
  --fd INTEGER                    Bind to socket from this file descriptor.
  --reload                        Enable auto-reload.
  --reload-dir PATH               Set reload directories explicitly, instead
                                  of using the current working directory.
  --reload-include TEXT           Set glob patterns to include while watching
                                  for files. Includes '*.py' by default; these
                                  defaults can be overridden with `--reload-
                                  exclude`. This option has no effect unless
                                  watchfiles is installed.
  --reload-exclude TEXT           Set glob patterns to exclude while watching
                                  for files. Includes '.*, .py[cod], .sw.*,
                                  ~*' by default; these defaults can be
                                  overridden with `--reload-include`. This
                                  option has no effect unless watchfiles is
                                  installed.
  --reload-delay FLOAT            Delay between previous and next check if
                                  application needs to be. Defaults to 0.25s.
                                  [default: 0.25]
  --workers INTEGER               Number of worker processes. Defaults to the
                                  $WEB_CONCURRENCY environment variable if
                                  available, or 1. Not valid with --reload.
  --loop [auto|asyncio|uvloop]    Event loop implementation.  [default: auto]
  --http [auto|h11|httptools]     HTTP protocol implementation.  [default:
                                  auto]
  --ws [auto|none|websockets|wsproto]
                                  WebSocket protocol implementation.
                                  [default: auto]
  --ws-max-size INTEGER           WebSocket max size message in bytes
                                  [default: 16777216]
  --ws-max-queue INTEGER          The maximum length of the WebSocket message
                                  queue.  [default: 32]
  --ws-ping-interval FLOAT        WebSocket ping interval in seconds.
                                  [default: 20.0]
  --ws-ping-timeout FLOAT         WebSocket ping timeout in seconds.
                                  [default: 20.0]
  --ws-per-message-deflate BOOLEAN
                                  WebSocket per-message-deflate compression
                                  [default: True]
  --lifespan [auto|on|off]        Lifespan implementation.  [default: auto]
  --interface [auto|asgi3|asgi2|wsgi]
                                  Select ASGI3, ASGI2, or WSGI as the
                                  application interface.  [default: auto]
  --env-file PATH                 Environment configuration file.
  --log-config PATH               Logging configuration file. Supported
                                  formats: .ini, .json, .yaml.
  --log-level [critical|error|warning|info|debug|trace]
                                  Log level. [default: info]
  --access-log / --no-access-log  Enable/Disable access log.
  --use-colors / --no-use-colors  Enable/Disable colorized logging.
  --proxy-headers / --no-proxy-headers
                                  Enable/Disable X-Forwarded-Proto,
                                  X-Forwarded-For, X-Forwarded-Port to
                                  populate remote address info.
  --server-header / --no-server-header
                                  Enable/Disable default Server header.
  --date-header / --no-date-header
                                  Enable/Disable default Date header.
  --forwarded-allow-ips TEXT      Comma separated list of IPs to trust with
                                  proxy headers. Defaults to the
                                  $FORWARDED_ALLOW_IPS environment variable if
                                  available, or '127.0.0.1'.
  --root-path TEXT                Set the ASGI 'root_path' for applications
                                  submounted below a given URL path.
  --limit-concurrency INTEGER     Maximum number of concurrent connections or
                                  tasks to allow, before issuing HTTP 503
                                  responses.
  --backlog INTEGER               Maximum number of connections to hold in
                                  backlog
  --limit-max-requests INTEGER    Maximum number of requests to service before
                                  terminating the process.
  --timeout-keep-alive INTEGER    Close Keep-Alive connections if no new data
                                  is received within this timeout.  [default:
                                  5]
  --timeout-graceful-shutdown INTEGER
                                  Maximum number of seconds to wait for
                                  graceful shutdown.
  --ssl-keyfile TEXT              SSL key file
  --ssl-certfile TEXT             SSL certificate file
  --ssl-keyfile-password TEXT     SSL keyfile password
  --ssl-version INTEGER           SSL version to use (see stdlib ssl module's)
                                  [default: 17]
  --ssl-cert-reqs INTEGER         Whether client certificate is required (see
                                  stdlib ssl module's)  [default: 0]
  --ssl-ca-certs TEXT             CA certificates file
  --ssl-ciphers TEXT              Ciphers to use (see stdlib ssl module's)
                                  [default: TLSv1]
  --header TEXT                   Specify custom default HTTP response headers
                                  as a Name:Value pair
  --version                       Display the uvicorn version and exit.
  --app-dir TEXT                  Look for APP in the specified directory, by
                                  adding this to the PYTHONPATH. Defaults to
                                  the current working directory.
  --h11-max-incomplete-event-size INTEGER
                                  For h11, the maximum number of bytes to
                                  buffer of an incomplete event.
  --factory                       Treat APP as an application factory, i.e. a
                                  () -> <ASGI app> callable.
  --help                          Show this message and exit.

```

## Reference
- [공식문서](https://fastapi.tiangolo.com/ko/)