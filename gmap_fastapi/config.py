import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="gmap_fastapi",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="gmap_fastapi_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from gmap_fastapi.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export gmap_fastapi_KEY=value
export gmap_fastapi_KEY="@int 42"
export gmap_fastapi_KEY="@jinja {{ this.db.uri }}"
export gmap_fastapi_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
gmap_fastapi_ENV=production gmap_fastapi run
```

Read more on https://dynaconf.com
"""
