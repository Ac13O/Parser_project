# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




ua = UserAgent()
headers = {'accept': '*/*', 'user-agent': ua.firefox}

def without_post(url, headers):
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		soup = bs(response.text, 'html.parser')
		links = {}
		for i in soup.find_all('a', {'class': 'post__title_link'}):
			links.update({i.text: i.get('href')})
		return links
	else:
		print("Connection Error")

url = "https://habr.com/ru/all/"
links = without_post(url, headers)
with open('parsed.txt', 'w') as f_obj:
	for name, href in links.items():
		f_obj.write(name + ':\n' + href + '\n\n')