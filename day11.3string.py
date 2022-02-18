web='***www.gmail.com***'
#strip(element) it will return a string by removing given character or pattern from exterme left and right
# if element not found it will return original string
#by default strip() remove whitespaces
email=web.strip('*')
#lstrip(element) it will remove string for extemeleft only
lweb=web.lstrip('*')
print('string after left strip',lweb)
#rstrip(element) remove given string from exteme right only
rweb=web.rstrip("*")
print('string after right strip',rweb)

print('email is',email)
