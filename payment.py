from instances import p2p
_lifetime = 15

def create_billing():
    new_bill = p2p.bill(amount=1, lifetime=_lifetime)
    bill_id = new_bill.bill_id
    pay_url = new_bill.pay_url
    return bill_id, pay_url

def get_billing_status(bill_id):
    if p2p.check(bill_id=bill_id).status == "PAID":
        return True
    else: 
        return False
