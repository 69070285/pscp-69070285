"""Max Number"""

m_number = -2e9

for i in range(3):
    if i >= 0:
        number = int(input())
        if number > m_number:
            m_number = number

print(m_number)
