def send_email(your_email, your_password, recepient_email):
    import yagmail
    from datetime import datetime

    def outer(fn):
        def inner(*args, **kwargs):
            result = fn()
            subject = f"Share Market News {datetime.now().strftime('%Y-%m-%d')}"
            try:
                yag = yagmail.SMTP(your_email, your_password)
                yag.send(recepient_email,
                         subject=subject, contents=result)
                print('Emails Sent')
            except Exception as e:
                print(e)
                exit()
        return inner
    return outer
