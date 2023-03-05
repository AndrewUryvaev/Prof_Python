from datetime import datetime

import application.db.people

from application.salary import calculate_salary

if __name__ == '__main__':
    print(datetime.now())
    application.db.people.get_employees()
    calculate_salary()