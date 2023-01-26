# APIs

## sign up
method: POST \
jwt token required: No \
url: localhost:8000/api/users/register \
request body(form data): \
username: foo \
password: bar

## login
method: POST \
jwt token required: No \
url: localhost:8000/api/users/login/ \
request body(form data): \
username: foo \
password: bar

## add new endpoint
method: POST \
jwt token required: Yes \
localhost:8000/api/urls/new/ \
request body(form data): \
url: https://foo.bar \
threshold: 123

## get endpoint id
method: GET \
jwt token required: Yes \
localhost:8000/api/urls/id/ \
request body(form data): \
url: https://foo.bar

## remove an endpoint
method: DELETE \
jwt token required: Yes \
localhost:8000/api/urls/<url_id>/

## get warnings
method: GET \
jwt token required: Yes \
localhost:8000/api/warnings/
