import pexpect as p
from delegator import RepoActions


class Manager():
    action = None

    def __init__(self, action):
        if isinstance(action, RepoActions):
            self.action = action
        else:
            raise ValueError('Please send a RepoAction')

    def do(self):
        bash = p.spawn('bash') # Initialize a shell
        print 'bash shell created'
        str_env = 'source %s/bin/activate' % str(self.action.env)
        bash.sendline(str_env) # Workon the environment
        print 'environment sourced'
        str_cmd = str_env + u'cd %s && git pull origin %s' % (self.action.base_dir, self.action.branch)
        bash.sendline(str_cmd)
        print 'branch %s pulled' % self.action.branch
        for cmd in self.action.cmds:
            print 'RUNNING %s' % str(cmd)
            bash.sendline(str(cmd))
