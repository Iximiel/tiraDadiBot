from os import environ
#qui sono presente i valori che estraggo dalle variabili d'ambiente
TELEGRAM_TOKEN = environ["TELEGRAM_TOKEN"]
#in caso decidessi di cambiarlo
TELEGRAM_HOOK = TELEGRAM_TOKEN
OPENSHIFT_GEAR_DNS = environ["OPENSHIFT_GEAR_DNS"]
OPENSHIFT_REPO_DIR = environ["OPENSHIFT_REPO_DIR"]
OPENSHIFT_PYTHON_IP = environ["OPENSHIFT_PYTHON_IP"]
OPENSHIFT_PYTHON_PORT = environ["OPENSHIFT_PYTHON_PORT"]
TELEGRAM_URL_HOOK = 'https://{}/{}'.format(OPENSHIFT_GEAR_DNS,TELEGRAM_HOOK)