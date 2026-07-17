"""Min Number"""

amount = int(input())
m_number = 2e9

for i in range(amount):
    if i >= 0:
        number = int(input())
        if number < m_number:
            m_number = number

print(m_number)
