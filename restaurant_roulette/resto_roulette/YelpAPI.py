import requests

#  defining the API Key, Endpoint, and header
API_KEY = 'Hmh3X44EOndrwanfrC5AdftCTWwD4TrvIO7xkS3WfE4XejMYUY0DsGiBM6WRV6K5HhdjjIsIa12XWGSlC1InJQSHS_F-jO03c_jxgREbESESKaqDXwc-8CZ-tbbHXHYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#  defining query parameters
PARAMETERS = {'term': 'mexican', 'location': 'Portland, OR',
              'limit': 5,
              'radius': 10000}

#  making a request
response = requests.get(url=ENDPOINT, params=PARAMETERS, headers=HEADERS)


#  converting JSON to a dictionary
business_data = response.json()

for biz in business_data['businesses']:
    address = ','.join(biz['location']['display_address'])
    biz_id = 'id'
    print(biz['name'], address)

# making review request
#
# for biz in business_data['businesses']:
#
#     REVIEW_ENDPOINT = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(biz_id)
#     review_response = requests.get(url=REVIEW_ENDPOINT, headers=HEADERS)
#     review_data = response.json()
