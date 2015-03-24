import subprocess
from delegator import RepoActions


class Manager():
    action = None

    def __init__(self, action):
        if action is RepoActions:
            self.action = action
        else:
            raise ValueError('Please send a RepoAction')

    def do(self):
        subprocess.call('cd %s & git pull origin %s' % (self.action.base_dir, self.action.branch))
        for cmd in self.action.cmds:
            subprocess.call(str(cmd))