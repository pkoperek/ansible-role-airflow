#!/usr/bin/python3

# Copyright (c) 2018-present eyeo GmbH
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser


def has_user(session, username):
    users = session.query(models.User)
    with_name = users.filter(models.User.username == username)
    return with_name.count() > 0


username = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

session = settings.Session()

if not has_user(session, username):
    new_user = PasswordUser(models.User())
    new_user.username = username
    new_user.email = email
    new_user.password = password

    session.add(new_user)
    session.commit()

    print('user created')

session.close()
