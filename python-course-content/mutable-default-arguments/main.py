"""
def create_account(name: str, holder: str, account_holders: list = []):
    print(id(account_holders))

    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


acc1 = create_account('checking', 'Rolf')
acc2 = create_account('savings', 'Jen')
print(acc2)
"""

"""
Option 1:
"""
# def create_account(name: str, holder: str, account_holders: list):
#     print(id(account_holders))

#     account_holders.append(holder)

#     return {
#         'name': name,
#         'main_account_holder': holder,
#         'account_holders': account_holders
#     }


# acc1 = create_account('checking', 'Rolf', [])
# acc2 = create_account('savings', 'Jen', [])
# print(acc1)
# print(acc2)

def create_account(name: str, holder: str, account_holders = None):
    # account_holders = account_holders or []
    if not account_holders:
        account_holders = []

    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


acc1 = create_account('checking', 'Rolf', [])
acc2 = create_account('savings', 'Jen')
print(acc1)
print(acc2)
