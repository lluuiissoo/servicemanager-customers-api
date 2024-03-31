
from dynaconf import Dynaconf
from dotenv import load_dotenv


# load_dotenv()  # take environment variables from .env.

settings = Dynaconf(
    load_dotenv=True,
    envvar_prefix="DYNACONF",
    settings_files=['settings.dev.toml', 'settings.qa.toml', '.secrets.toml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
