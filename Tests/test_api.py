import json
import requests
from pg_testing_utilites import get_last_record_device

from enum import Enum
class Response(Enum):
	InvalidRate = 0
	Ok = 1
	FeedbackReqF = 2
	FeedbackReqT = 3
	MissedField = 4

class HeaderValue(Enum):
	Uncategorized = 0
	Desktop = 1
	Mobile = 2

url = 'http://localhost:58001/nps'

def resolver(request, headers, excepted_response):
	answer = requests.post(url, data=json.dumps(request), headers=headers)
	print(answer)
	response = answer.json()
	print(response)
	assert response == excepted_response

def test_JsonTest_1(case_request, case_response, case_header):
	request = case_request.__getitem__(1)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.InvalidRate.value)
	resolver(request, headers, excepted_response)

def test_JsonTest_2(case_request, case_response, case_header):
	request = case_request.__getitem__(2)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.InvalidRate.value)
	resolver(request, headers, excepted_response)

def test_JsonTest_3(case_request, case_response, case_header):
	request = case_request.__getitem__(3)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.FeedbackReqF.value)
	resolver(request, headers, excepted_response)

def test_JsonTest_4(case_request, case_response, case_header):
	request = case_request.__getitem__(4)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.FeedbackReqT.value)
	resolver(request, headers, excepted_response)

def test_JsonTest_5(case_request, case_response, case_header):
	request = case_request.__getitem__(5)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.InvalidRate.value)
	resolver(request, headers, excepted_response)

def test_JsonTest_6(case_request, case_response, case_header):
	request = case_request.__getitem__(6)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.Ok.value)
	resolver(request, headers, excepted_response)

def test_JsonTest_7(case_request, case_response, case_header):
	request = case_request.__getitem__(7)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.Ok.value)
	resolver(request, headers, excepted_response)

def test_JsonTest_8(case_request, case_response, case_header):
	request = case_request.__getitem__(8)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.MissedField.value)
	resolver(request, headers, excepted_response)

def test_JsonTest_9(case_request, case_response, case_header):
	request = case_request.__getitem__(7)
	headers = case_header.__getitem__(HeaderValue.Desktop.value)
	excepted_response = case_response.__getitem__(Response.Ok.value)
	resolver(request, headers, excepted_response)
	assert 'desktop' == get_last_record_device()


def test_JsonTest_10(case_request, case_response, case_header):
	request = case_request.__getitem__(7)
	headers = case_header.__getitem__(HeaderValue.Mobile.value)
	excepted_response = case_response.__getitem__(Response.Ok.value)
	resolver(request, headers, excepted_response)
	assert 'mobile' == get_last_record_device()

def test_JsonTest_11(case_request, case_response, case_header):
	request = case_request.__getitem__(7)
	headers = case_header.__getitem__(HeaderValue.Uncategorized.value)
	excepted_response = case_response.__getitem__(Response.Ok.value)
	resolver(request, headers, excepted_response)
	assert 'desktop' == get_last_record_device()
