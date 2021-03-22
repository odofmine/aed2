import logging
import subprocess

from config import Config


enable_git_pull = Config.root()['enable_git_pull']
enable_git_push = Config.root()['enable_git_push']


def pull(git_dir):
    logging.info('')
    logging.info(f'git pull from {git_dir}')

    if not enable_git_pull:
        logging.info('git pull disabled')
        return

    result = subprocess.check_output(f'cd {git_dir} && git pull origin main', shell=True)
    logging.info(result.decode('utf-8'))


def push(git_dir):
    if not enable_git_push:
        logging.info('git push disabled')
        return

    result = subprocess.check_output(f'cd {git_dir} && git add . && git commit -m "update"', shell=True)
    logging.info(result.decode('utf-8'))
    result = subprocess.check_output(f'cd {git_dir} && git push origin main', shell=True)
    logging.info(result.decode('utf-8'))
