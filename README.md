# GadgetRent service by Jago team

## Runbook

### Ansible
* Create `venv` and install `ansbile` and requirements
    ```shell
    cd ansible
    python3 -m venv ansible-env
    source ansible-env/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install ansible
    python3 -m pip install yandexcloud
    ```

* Check everything installed correctly
    ```shell
    which ansible
    python3 -m pip list | grep ansible
    ```

* Install necessary roles
    ```shell
    ansible-galaxy role install geerlingguy.docker
    ansible-galaxy install nginxinc.nginx 
    ```

* Check inventories are identified correctly
    ```shell
    ansible-inventory --list
    ``` 

* Install `docker` on hosts
    ```shell
    ansible-playbook playbooks/dev/docker/main.yml
    ``` 

* Install `nginx` on hosts
    ```shell
    ansible-playbook playbooks/dev/nginx/main.yml
    ``` 

* Deactivate `venv`
    ```shell
    deactivate
    ```

* Next time you can just activate this saved `venv` with no need to create it and install requirements:
    ```shell
    cd ansible
    source ansible-env/bin/activate
    ```