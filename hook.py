from delegator import Delegator
from manager import Manager
import web

urls = ('/.*', 'hooks')
app = web.application(urls, globals())


class hooks:
    def POST(self):
        # Json from github
        payload = web.data()
        print
        print 'DATA RECEIVED:'
        print payload
        print
        # send payload to delegator
        delegator = Delegator(payload)
        print 'DELEGATOR PARSED'
        if delegator.action:
            print 'REPO FOUND'
            man = Manager(delegator.action)
            print 'RUNNING CMDS'
            man.do()


if __name__ == '__main__':
    print 'running'
    app = web.application(urls, globals())
    app.run()