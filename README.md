# PYTHON

Here is python scripts for ZAP API and scripts for posting results to
SLACK, redmine and defectDojo

Version of python: `python > 3.8`

**WARNING!:** If you can't connect to zap API, you should setup  **hostname zap** in your instance.
On the host with python scripts  you **should** edit `/etc/hosts` with `zap` line and IP API ZAP. If scripts working into Docker you can edit `/etc/hosts` by `--add-host` parameter into `docker run` command.

## Dependences

Please if you run it into host, install dependeces:
    `pip3 install -r requirements.txt`

## Scripts
`zap_regression_scan.py` uses for scanning after regression qa tests.
`api_scan.py` uses for scanning with open api url

##### Running
Edit:
```
/scripts/configs/reports_config.py
/scripts/configs/config_regression.py
/scripts/scan_core/api_conf.py
```
For run into Docker please use:
```
git clone
docker build -t zap-scripts .
docker run --rm zap-scripts
```
For run into host:
`python regression_scan.py`

### Usage
regression_scan.py have an arguments. Please get help it by:
`python regression_scan.py --help`
If you usage the docker, you can edit entrypoint in `Dockerfile` for change parameters of regular scans. After it you should build docker image again.
You can usage `--entrypoint`  parameter into `docker run` command.
For example:
`docker run --rm --entrypoint /usr/local/bin/python3 zap-scripts regression_scan.py --help`
