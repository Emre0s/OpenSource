from requests import request

end_points = {
    'api_key': "VzrKCzj5QnK5TzCMYFpy4rJ9kRrqep",
    'from': input("Sizdeki birim:").upper(),
    'to': input("Dönüşecek birim:").upper(),
    'amount': int(input("Kaç birim:")),
}

print(request("GET", params=end_points, url="https://www.amdoren.com/api/currency.php").json())