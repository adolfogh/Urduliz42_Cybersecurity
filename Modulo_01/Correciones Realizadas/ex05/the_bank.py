# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/28 19:35:58 by dgerwig-          #+#    #+#              #
#    Updated: 2023/05/01 11:46:02 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Account(object):
    
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    '''
    The bank
    '''

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        ''' 
        Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        '''
        if isinstance(new_account, Account) and new_account not in self.accounts:
            self.accounts.append(new_account)
        else:
            print('Invalid account.')

    def corrupted_account(self, account):
        '''
        A function to check if an account is corrupted
        A bank account is corrupted when:
            * has an even number of attributes.
            * has an attribute starting with b.
            * has no attribute starting with zip or addr.
            * has no attribute name, id and value.
        '''
        if len(account.__dict__) % 2 == 0:
            return True
        if 'name' not in account.__dict__.keys():
            return True
        if 'id' not in account.__dict__.keys():
            return True
        if 'value' not in account.__dict__.keys():
            return True
        zip_check = 0
        addr_check = 0
        for key in account.__dict__.keys():
            if key.startswith('zip'):
                zip_check = 1
            if key.startswith('addr'):
                addr_check = 1
            if key.startswith('b'):
                return True
        if zip_check == 0 or addr_check == 0:
            return True
        return False

    def transfer(self, origin, dest, amount):
        '''
        Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        '''
        origin_acc = 0
        destin_acc = 0
        for elem in self.accounts:
            if origin == elem.id or origin == elem.name:
                origin_acc = elem
            if dest == elem.id or dest == elem.name:
                destin_acc = elem
        if origin_acc == 0 or destin_acc == 0:
            print("Could not find account.")
            return False
        if self.corrupted_account(origin_acc) or self.corrupted_account(destin_acc):
            print("Corrupted account.")
            return False
        if amount <= 0 or origin_acc.value < amount:
            print("Invalid amount.")
            return False
        origin_acc.transfer(-amount)
        destin_acc.transfer(amount)
        print("Transfer successful.")
        return True

    def fix_account(self, name):
        '''
        Fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        '''
        corrupted = 0
        zip_check = 0
        addr_check = 0
        for elem in self.accounts:
            if name in elem.__dict__.values():
                corrupted = elem
        if corrupted == 0:
            print("Could not find account.")
            return False
        keys = list(corrupted.__dict__.keys())
        if 'name' not in keys:
            corrupted.__dict__['name'] = 'Restored account'
        if 'id' not in keys:
            corrupted.__dict__['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'value' not in keys:
            corrupted.__dict__['value'] = 0
        for key in keys:
            if key.startswith('zip'):
                zip_check = 1
            if key.startswith('addr'):
                addr_check = 1
            if key.startswith('b'):
                corrupted.__dict__.pop(key)
        if zip_check == 0:
            corrupted.__dict__['zip'] = '666-666'
        if addr_check == 0:
            corrupted.__dict__['addr'] = '42 Urduliz'
        if len(corrupted.__dict__) % 2 == 0:
            for key in corrupted.__dict__.keys():
                if key == 'name' or key == 'id' or key == 'value':
                    pass
                elif key.startswith('zip') or key.startswith('addr'):
                    pass
                else:
                    corrupted.__dict__.pop(key)
                    break
        if self.corrupted_account(corrupted):
            print("Fixed account -> ❌ FAIL")
            return False
        else:
            print("Fixed account -> 🟢 SUCCESS")
            return True
