import requests as rq
import smtplib


def sendmail(f):
    if f.status_code == 200:
        with smtplib.SMTP('smtp.outlook.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login('user', 'password')

            subject = 'Test mail sent by Python script'
            body = 'Mail sent successfully'

            msg = f'Subject : {subject}\n\n{body}'

            smtp.sendmail('possumtree452@hotmail.com', 'prathmeshshinde1998@gmail.com', msg)


if __name__ == "__main__":
    #r = rq.get('https://www.skyscanner.co.in/transport/flights/pnq/blr/240818/config/15466-2408181940--32671-0-10002-2408182110?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false')
    # sendmail(r) # sends mail
    #print(r.content)
    prices = ['₹ 9,113', '₹ 9,155', '₹ 9,166', '₹ 9,196', '₹ 9,196']
    subject = 'SkyScanner price check '
    body = f'Top 5 prices are {prices}'
    msg = f'Subject: {subject}\n\n {body}'
    encoded_price = [s.encode for s in prices]
    print(msg)
    clean_price = [s[2:] for s in prices]
    print(clean_price)

