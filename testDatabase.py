import os
import unittest
import datetime
from app import db, models

def register(name, username, password):
    if name and username and password:
        account = models.Account(name=name, username=username, password=password)
        db.session.add(account)

        return True
    else:
        return False

def login(username, password):
    if username and password:
        accounts = models.Account.query.all()

        for i in accounts:
            if i.username == username:
                if i.password == password:
                    return True

        return False
    else:
        return False

def find(username):
    return models.Account.query.filter_by(username=username).all()


def change(id, old, new):
    if old and new:
        account = models.Account.query.get(id)

        if account.password == old:
            account.password = new

            return account.password

        return False
    else:
        return False

def favourite(postId, accountId):
    post = models.Post.query.get(postId)
    account = models.Account.query.get(accountId)
    post.comments.append(account)

    return True

# tests registering accounts
class Register(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        db.session.rollback()
        pass

    def test_register_correct(self):
        assert register('Mona Lisa', 'Mona', 'Lisa') == True

    def test_missing_all(self):
        assert register('', '', '') == False

    def test_only_name(self):
        assert register('Mona Lisa', '', '') == False

    def test_only_username(self):
        assert register('', 'Mona', '') == False

    def test_only_password(self):
        assert register('', '', 'Lisa') == False

    def test_no_name(self):
        assert register('', 'Mona', 'Lisa') == False

    def test_no_username(self):
        assert register('Mona Lisa', '', 'Lisa') == False

    def test_no_password(self):
        assert register('Mona Lisa', 'Mona', '') == False

# tests logging in
class Login(unittest.TestCase):
    def setUp(self):
        account = models.Account(name='Mona Lisa', username='Mona', password='Lisa')
        db.session.add(account)
        pass

    def tearDown(self):
        db.session.rollback()
        pass

    def test_login_correct(self):
        assert login('Mona', 'Lisa') == True

    def test_missing_all(self):
        assert login('', '') == False

    def test_missing_username(self):
        assert login('', 'Lisa') == False

    def test_missing_password(self):
        assert login('Mona', '') == False

    def test_both_incorrect(self):
        assert login('Van', 'Gough') == False

    def test_username_incorrect(self):
        assert login('Van', 'Lisa') == False

    def test_password_incorrect(self):
        assert login('Mona', 'Gough') == False

# tests changing password
class Change(unittest.TestCase):
    def setUp(self):
        account = models.Account(name='Mona Lisa', username='Mona', password='Lisa')
        db.session.add(account)
        pass

    def tearDown(self):
        db.session.rollback()
        pass

    def test_change_correct(self):
        account = find('Mona')
        assert change(account[0].id, 'Lisa', 'Gough') == 'Gough'

    def test_missing_all(self):
        account = find('Mona')
        assert change(account[0].id, '', '') == False

    def test_missing_old(self):
        account = find('Mona')
        assert change(account[0].id, '', 'Gough') == False

    def test_missing_new(self):
        account = find('Mona')
        assert change(account[0].id, 'Lisa', '') == False

    def test_old_incorrect(self):
        account = find('Mona')
        assert change(account[0].id, 'Van', 'Gough') == False

# tests adding a favourite post to an account
class Favourite(unittest.TestCase):
    def setUp(self):
        account = models.Account(name='Mona Lisa', username='Mona', password='Lisa')
        post = models.Post(title='Test', date=datetime.datetime(2018, 6, 25))
        db.session.add(account)
        db.session.add(post)
        pass

    def tearDown(self):
        db.session.rollback()
        pass

    def test_favourite_correct(self):
        posts = models.Post.query.all()
        postId = posts[-1].id
        account = find('Mona')
        assert favourite(postId=postId, accountId=account[0].id) == True

if __name__ == '__main__':
    unittest.main()
