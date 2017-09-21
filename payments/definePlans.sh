
curl https://api.stripe.com/v1/plans \
   -u sk_test_OkmvhmRZyPAUmYtjkrKbonka: \
   -d name="Personal" \
   -d id=Personal \
   -d interval=month \
   -d currency=usd \
   -d amount=5

curl https://api.stripe.com/v1/plans \
   -u sk_test_OkmvhmRZyPAUmYtjkrKbonka: \
   -d name="Professional" \
   -d id=Professional \
   -d interval=month \
   -d currency=usd \
   -d amount=12


curl https://api.stripe.com/v1/plans \
   -u sk_test_OkmvhmRZyPAUmYtjkrKbonka: \
   -d name="Business" \
   -d id=Business \
   -d interval=month \
   -d currency=usd \
   -d amount=24

'
The result should be

{
  "id": "Personal",
  "object": "plan",
  "amount": 5,
  "created": 1501103988,
  "currency": "usd",
  "interval": "month",
  "interval_count": 1,
  "livemode": false,
  "metadata": {},
  "name": "Personal",
  "statement_descriptor": null,
  "trial_period_days": null
}
{
  "id": "Professional",
  "object": "plan",
  "amount": 12,
  "created": 1501103989,
  "currency": "usd",
  "interval": "month",
  "interval_count": 1,
  "livemode": false,
  "metadata": {},
  "name": "Professional",
  "statement_descriptor": null,
  "trial_period_days": null
}
{
  "id": "Business",
  "object": "plan",
  "amount": 24,
  "created": 1501103991,
  "currency": "usd",
  "interval": "month",
  "interval_count": 1,
  "livemode": false,
  "metadata": {},
  "name": "Business",
  "statement_descriptor": null,
  "trial_period_days": null
}
'
