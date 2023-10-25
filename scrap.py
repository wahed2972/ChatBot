import requests
from bs4 import BeautifulSoup

url = "https://brainlox.com/courses/category/technical"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    course_data = []

    course_containers = soup.find_all('div', class_='courses-content')

    for container in course_containers:
        title_element = container.find('h3').find('a')
        description_element = container.find('p')
        url = "https://brainlox.com" + title_element['href']

        if title_element and description_element:
            title = title_element.text.strip()
            description = description_element.text.strip()

            course_info = {
                'title': title,
                'description': description,
                'url': url,
            }

            course_data.append(course_info)

    for course in course_data:
        print("Title:", course['title'])
        print("Description:", course['description'])
        print("URL:", course['url'])
        print()

except requests.exceptions.RequestException as e:
    print("Error: Failed to retrieve the webpage.")
    print(e)
except Exception as e:
    print("An error occurred:")
    print(e)
