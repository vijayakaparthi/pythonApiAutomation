import requests

def test_getusers():
    response=requests.get("https://reqres.in/api/users?page=2")
    print(response.status_code)
    json_data=response.json()
    assert(json_data['page']==2)
    assert(json_data['data'][1]['id']==8)

def test_updateuser():
   json_data= {
    "name": "morpheus",
    "job": "zion resident"
    }

   response=requests.post("https://reqres.in/api/users/2",data=json_data)
   print(response.status_code)
    