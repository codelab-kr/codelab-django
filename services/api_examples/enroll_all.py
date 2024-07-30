import requests

username = 'st1'
password = 'wish0929'

base_url = 'http://127.0.0.1:8000/api/'
url = f'{base_url}courses/'
available_courses: list[str] = []

while url:
    print(f'Loading courses from {url}')
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Failed to retrieve data: {r.status_code}')
        break

    response = r.json()
    # print(response)

    # 다음 페이지의 URL을 가져옵니다. 없으면 None을 반환합니다.
    url = response.get('next')

    # 현재 페이지의 코스 데이터를 가져옵니다.
    courses = response.get('results', [])
    available_courses.extend(course['title'] for course in courses)

print(f"Available courses: {', '.join(available_courses)}")

auth_url = f'{base_url}auth/'
token = requests.post(auth_url, data={'username': username, 'password': password})
token = token.json()['token']
# print(token)

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(
        f'{base_url}courses/{course_id}/enroll/',
        headers={'Authorization': f'Token {token}'},
    )
    if r.status_code == 200:
        # successful request
        print(f'Successfully enrolled in {course_title}')
