import subprocess
from delegator import RepoActions


class Manager():
    action = None

    def __init__(self, action):
        if isinstance(action, RepoActions):
            self.action = action
        else:
            raise ValueError('Please send a RepoAction')

    def do(self):
	str_env = 'source %s/activate && ' % str(self.action.env)
        str_cmd = str_env + u'cd %s && git pull origin %s' % (self.action.base_dir, self.action.branch)
        print 'RUNNING: ' + str_cmd
        subprocess.call(str_cmd,executable='bash', shell=True)
        for cmd in self.action.cmds:
            print 'RUNNING %s %s' % (str_env, str(cmd))
            subprocess.call(str_env + str(cmd),executable='bash', shell=True)
