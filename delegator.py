import json


EXECUTABLE_BRANCHES = ['refs/heads/master']

class Delegator():
    # Github payload
    payload_repo = None
    payload_committer = None
    payload_branch = None
    # Local Repo
    local_branch = None
    local_base_dir = None
    local_json = None
    # Actions
    action = None

    def __init__(self, payload):
        payload_json = json.loads(payload)

        self.payload_repo = payload_json['repository']['name']
        self.payload_committer = payload_json['commits'][0]['author']['name']
        self.payload_branch = payload_json['ref']

        self.local_json = self.parse_repo()
        if self.local_json:
            self.local_base_dir = self.local_json['base_dir']
            self.local_branch = self.local_json['branch']

            if self.payload_branch == self.local_branch or self.payload_branch in self.local_branch:
                self.action = RepoActions(self.payload_repo, self.local_base_dir, self.local_branch, self.local_json['cmds'])
            else:
                # Take no action
                self.action = False
        else:
            # Take no action
            self.action = False

    @staticmethod
    def get_repos():
        with open('repos') as data:
            json_data = json.load(data)
            data.close()
            return json_data

    def parse_repo(self):
        if self.payload_repo in Delegator.get_repos():
            return Delegator.get_repos()[self.payload_repo]
        return False

class RepoActions(object):
    repo_name = None
    base_dir = None
    branch = None
    cmds = []

    def __init__(self, name, base, branch, cmds):
        self.repo_name = name
        self.base_dir = base
        self.branch = branch
        for cmd in cmds:
            self.cmds.append(Commands(cmd['dir'], cmd['cmd']))


class Commands(object):
    directory = None
    cmd = None

    def __init__(self, directory, cmd):
        self.directory = directory
        self.cmd = cmd

    def cmd(self):
        return u'cd %s & %s' % (self.directory, self.cmd)

    def __str__(self):
        return u'cd %s & %s' % (self.directory, self.cmd)