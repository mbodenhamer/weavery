from fabric.tasks import execute
from fabric.state import env
from fabric.api import settings
from dockerman import container
from syn.base_utils import assign

from weavery import groups, users, success, success_sudo

#-------------------------------------------------------------------------------

def test1():
    with container('rastasheep/ubuntu-sshd') as c:
        with assign(env, 'host_string', c.status.ip_addr):
            with assign(env, 'user', 'root'):
                with assign(env, 'password', 'root'):
                    c.poll(22)

                    assert success('true')
                    with settings(warn_only=True):
                        assert not success('false')

#-------------------------------------------------------------------------------
