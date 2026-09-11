# Contact Form Backend

I kept telling people to "just email me" on my portfolio, but there was no actual form — just a mailto link that half the time didn't even open properly. So I built this: a real contact form backend that sends messages straight to my inbox, without me running any server for it.

## How it works

Someone fills out a form (name, email, a message) → that hits an API Gateway endpoint → which wakes up a small Lambda function → which asks Amazon SES to actually send the email → and it lands in my inbox a couple seconds later.

Nothing is "always on." The whole thing costs nothing until someone actually submits the form.

## A wrinkle worth mentioning: sandbox mode

New AWS accounts start SES in "sandbox mode" — you can only send email *to* addresses you've manually verified first. That's AWS's way of stopping brand-new accounts from being used to spam people. For this project it's a non-issue, since every message is meant to land in my own inbox anyway — but it's the reason this can't (yet) send email to just anyone without requesting production access from AWS first.

## Endpoint

`POST /contact`
```json
{
  "name": "...",
  "email": "...",
  "message": "..."
}
```

## Stack


- Python 3.12 + boto3
- Lambda
- API Gateway
- SES

## Where this is going


Eventually this replaces the placeholder contact section on my portfolio site — a real working form instead of a dead mailto link.


## Status
- [x] Lambda function written
- [ ] SES email verified
- [ ] Lambda deployed
- [ ] API Gateway configured
- [ ] Live and tested